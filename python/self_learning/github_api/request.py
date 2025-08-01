import argparse
import asyncio
import getpass
import hashlib
import os
import sys
from pathlib import Path
from typing import Any, TypedDict, cast
from urllib.parse import urlparse

import aiohttp
import keyring
import uvloop
from tqdm.asyncio import tqdm


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
    def __init__(self, owner: str, repo: str, session: aiohttp.ClientSession) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.auth_manager: GitHubAuthManager = GitHubAuthManager()
        self.api_url: str = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        self.session = session

    async def fetch_latest_release(self) -> GitHubReleaseDetails:
        headers = GitHubAuthManager.apply_auth({})
        async with self.session.get(url=self.api_url, headers=headers) as response:
            response.raise_for_status()
            return await response.json()

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

    def extract_appimage_asset(self, release_data: dict[str, Any]) -> GitHubAsset | None:
        assets = cast(list[dict[str, Any]], release_data.get("assets", []))
        for asset in assets:
            if asset.get("name", "").endswith(".AppImage"):
                return self.to_github_asset(asset)
        return None


class Installer:
    def __init__(self, asset: GitHubAsset, session: aiohttp.ClientSession) -> None:
        self.asset: GitHubAsset = asset
        self.session = session
        self.filename: str = Path(urlparse(asset["browser_download_url"]).path).name

    async def download(self) -> Path:
        headers: dict[str, str] = GitHubAuthManager.apply_auth({})
        async with self.session.get(
            url=self.asset["browser_download_url"], headers=headers
        ) as response:
            response.raise_for_status()
            total = int(response.headers.get("Content-Length", 0))
            chunk_size = 8192
            downloaded = 0

            with (
                open(self.filename, "wb") as f,
                tqdm(total=total, unit="B", unit_scale=True, desc=self.filename) as pbar,
            ):
                async for chunk in response.content.iter_chunked(chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        pbar.update(len(chunk))

        return Path(self.filename)

    def make_executable(self, path: Path) -> None:
        os.chmod(path, 0o755)

    async def install(self) -> Path:
        path = await self.download()
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
            raise ValueError(f"Digest mismatch!\nExpected: {expected}\nActual:   {actual}")


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


async def install_and_verify_appimage(
    repo: str, session: aiohttp.ClientSession
) -> tuple[str, str, bool]:
    try:
        owner, repo_name = repo.split("/", 1)
        fetcher = GitHubReleaseFetcher(owner, repo_name, session)
        release_data = await fetcher.fetch_latest_release()

        appimage = fetcher.extract_appimage_asset(release_data)
        if not appimage:
            return repo, "❌ No AppImage found", False

        installer = Installer(appimage, session)
        path = await installer.install()

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
    parser.add_argument("--concurrency", type=int, default=4, help="Max parallel installs")
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
            parser.error("--repo is required unless using --save-token or --remove-token")

    return args


async def main():
    args: argparse.Namespace = parse_cli_args()

    if args.save_token:
        GitHubAuthManager.save_token()
        sys.exit(0)
    elif args.remove_token:
        GitHubAuthManager.remove_token()
        sys.exit(0)

    repos: list[str] = args.repo or []

    results: list[tuple[str, str, bool]] = []

    async with aiohttp.ClientSession() as session:
        tasks = [install_and_verify_appimage(repo, session) for repo in repos]
        results = await asyncio.gather(*tasks)

    print("\n📦 Installation Summary:\n")
    for repo, message, success in results:
        print(f"{repo:<30} {message}")


if __name__ == "__main__":
    uvloop.run(main())
