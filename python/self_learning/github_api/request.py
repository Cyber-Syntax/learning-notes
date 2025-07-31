import argparse
import getpass
import hashlib
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, TypedDict, cast
from urllib.parse import urlparse

import keyring
import requests

# TODO: use asyncio for better performance
# learn aiohttp


class GitHubAsset(TypedDict):
    name: str
    size: int
    digest: str
    browser_download_url: str


class GitHubReleaseDetails(TypedDict):
    owner: str
    repo: str
    version: str
    prerelease: bool
    assets: list[GitHubAsset]


class GitHubReleaseFetcher:
    def __init__(self, owner: str, repo: str) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.auth_manager: GitHubAuthManager = GitHubAuthManager()
        self.api_url: str = (
            f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        )

    def fetch_latest_release(self) -> GitHubReleaseDetails:
        headers = GitHubAuthManager.apply_auth({})
        response = requests.get(url=self.api_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def to_github_asset(self, asset: dict[str, Any]) -> GitHubAsset | None:
        try:
            return {
                "name": cast(str, asset.get("name")),
                "digest": cast(str, asset.get("digest")),
                "size": cast(int, asset.get("size")),
                "browser_download_url": cast(str, asset.get("browser_download_url")),
            }
        except Exception:
            return None

    def extract_appimage_asset(
        self, release_data: dict[str, Any]
    ) -> GitHubAsset | None:
        assets = cast(list[dict[str, Any]], release_data.get("assets", []))
        for asset in assets:
            if asset.get("name", "").endswith(".AppImage"):
                return self.to_github_asset(asset)
        return None


# Global lock to synchronize terminal output
progress_lock = threading.Lock()

# Tracks which filename should print on which line
progress_lines: dict[str, int] = {}


class Installer:
    _line_counter: int = 0

    def __init__(self, asset: GitHubAsset) -> None:
        self.asset: GitHubAsset = asset
        self.filename: str = Path(urlparse(asset["browser_download_url"]).path).name

        with progress_lock:
            if self.filename not in progress_lines:
                Installer._line_counter += 1
                progress_lines[self.filename] = Installer._line_counter

        # line relative to reserved block
        self.line: int = progress_lines[self.filename]

    def download(self) -> Path:
        headers: dict[str, str] = GitHubAuthManager.apply_auth({})
        response = requests.get(
            url=self.asset["browser_download_url"], headers=headers, stream=True
        )
        response.raise_for_status()
        total = int(response.headers.get("Content-Length", 0))
        downloaded = 0
        chunk_size = 8192

        with open(self.filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    self.print_progress(downloaded, total)

        self.print_done()
        return Path(self.filename)

    def print_progress(self, downloaded: int, total: int) -> None:
        percent = int(downloaded / total * 100) if total else 0
        bar_length = 30
        filled = int(bar_length * percent // 100)
        bar = "#" * filled + "-" * (bar_length - filled)

        with progress_lock:
            sys.stdout.write(move_cursor(self.line, 0) + clear_line())
            sys.stdout.write(f"{self.filename:<40} [{bar}] {percent:>3}%\n")
            sys.stdout.flush()

    def print_done(self) -> None:
        # clear the progress bar when done
        with progress_lock:
            sys.stdout.flush()

    def make_executable(self, path: Path) -> None:
        os.chmod(path, 0o755)

    def install(self) -> Path:
        path = self.download()
        self.make_executable(path)
        return path


class Verifier:
    def __init__(self, asset: GitHubAsset, file_path: Path) -> None:
        self.asset: GitHubAsset = asset
        self.file_path: Path = file_path

    def get_expected_hash(self) -> str:
        algo, _, hash_value = self.asset["digest"].partition(":")
        if algo != "sha256":
            raise ValueError("Unsupported digest algorithm")
        return hash_value

    def compute_actual_hash(self) -> str:
        sha256 = hashlib.sha256()
        with open(self.file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def verify(self) -> None:
        expected = self.get_expected_hash()
        actual = self.compute_actual_hash()
        if expected != actual:
            raise ValueError(
                f"Digest mismatch!\nExpected: {expected}\nActual:   {actual}"
            )


class GitHubAuthManager:
    KEY_NAME: str = "github_appimage_installer"

    @staticmethod
    def save_token() -> None:
        token: str = getpass.getpass(prompt="Enter your GitHub token (input hidden): ")
        keyring.set_password(GitHubAuthManager.KEY_NAME, "token", token)
        print("✅ Token securely saved to keyring.")

    @staticmethod
    def remove_token() -> None:
        keyring.delete_password(GitHubAuthManager.KEY_NAME, "token")
        print("🗑️ Token removed from keyring.")

    @staticmethod
    def get_token() -> str | None:
        return keyring.get_password(GitHubAuthManager.KEY_NAME, "token")

    @staticmethod
    def apply_auth(headers: dict[str, str]) -> dict[str, str]:
        token: str | None = GitHubAuthManager.get_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers


def move_cursor(row: int, col: int = 0) -> str:
    return f"\033[{row};{col}H"


def move_cursor_to_line(line: int) -> str:
    # Move up N lines, then to beginning
    return f"\033[{line}F"  # ANSI "Cursor to beginning of Nth previous line"


def move_cursor_to_bottom() -> None:
    sys.stdout.write("\033[999B")  # Move cursor way down
    sys.stdout.flush()


def clear_line() -> str:
    return "\033[2K"


# Reserve space at current position and track starting row
def reserve_progress_lines(count: int) -> int:
    print("\n" * count, end="")
    sys.stdout.flush()
    return count


def install_and_verify_appimage(repo: str) -> tuple[str, str, bool]:
    try:
        owner, repo_name = repo.split("/", 1)
        fetcher = GitHubReleaseFetcher(owner, repo_name)
        release_data = fetcher.fetch_latest_release()

        appimage = fetcher.extract_appimage_asset(release_data)
        if not appimage:
            return repo, "❌ No AppImage found", False

        installer = Installer(appimage)
        path = installer.install()

        verifier = Verifier(appimage, path)
        verifier.verify()

        return repo, "✅ Downloaded and verified", True

    except Exception as e:
        return repo, f"❌ Failed: {e}", False


def parse_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Concurrent AppImage Installer")

    parser.add_argument(
        "--repo",
        action="append",
        help="GitHub repo in owner/repo format (can repeat)",
    )
    parser.add_argument(
        "--concurrency", type=int, default=4, help="Max parallel installs"
    )
    parser.add_argument(
        "--save-token", action="store_true", help="Save GitHub token to keyring"
    )
    parser.add_argument(
        "--remove-token", action="store_true", help="Remove GitHub token from keyring"
    )

    args = parser.parse_args()

    # Validate repo only if needed
    if not args.save_token and not args.remove_token:
        if not args.repo:
            parser.error(
                "--repo is required unless using --save-token or --remove-token"
            )

    return args


def main():
    args: argparse.Namespace = parse_cli_args()

    if args.save_token:
        GitHubAuthManager.save_token()
        sys.exit(0)
    elif args.remove_token:
        GitHubAuthManager.remove_token()
        sys.exit(0)

    repos: list[str] = args.repo or []

    move_cursor_to_bottom()

    print("\n" * len(repos))  # reserve vertical space for progress bars

    results: list[tuple[str, str, bool]] = []

    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = [executor.submit(install_and_verify_appimage, repo) for repo in repos]
        for future in as_completed(futures):
            results.append(future.result())

    print("\n📦 Installation Summary:\n")
    for repo, message, success in results:
        print(f"{repo:<30} {message}")


if __name__ == "__main__":
    main()
