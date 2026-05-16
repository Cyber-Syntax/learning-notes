from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


# ============================================================
# NOTE:
# We DO NOT want verification logic inside GithubService,
# GitlabService, WebsiteService etc.
#
# Why?
#
# Because:
#
# - some github projects provide checksum
# - some github projects do not
# - some github projects use checksum files
# - some github projects use api hashes
# - some website projects provide checksum
# - some website projects provide nothing
#
# So verification is NOT tied to the source itself.
#
# Instead:
#
# source     -> responsible for fetching release/assets
# detector   -> responsible for finding verification method
# verifier   -> responsible for actual verification
#
# This is composition over inheritance.
# ============================================================


# ============================================================
# Fake asset model returned from APIs
# ============================================================

@dataclass
class Asset:
    name: str
    download_url: str


# ============================================================
# Release info returned from github/gitlab/website
# ============================================================

@dataclass
class Release:
    version: str
    assets: list[Asset]


# ============================================================
# NOTE:
# This strategy is ONLY responsible for downloading/fetching
# release metadata.
#
# It should NOT verify anything.
# ============================================================

class ReleaseProvider(ABC):

    @abstractmethod
    def get_latest_release(self, package_name: str) -> Release:
        pass


# ============================================================
# GitHub implementation
# ============================================================

class GithubReleaseProvider(ReleaseProvider):

    def get_latest_release(self, package_name: str) -> Release:

        # Imagine this data came from GitHub API
        github_json = {
            "tag_name": "v1.0.0",
            "assets": [
                {
                    "name": "app-linux-amd64.tar.gz",
                    "browser_download_url": "https://github.com/app.tar.gz"
                },
                {
                    "name": "app-linux-amd64.tar.gz.sha256",
                    "browser_download_url": "https://github.com/app.sha256"
                }
            ]
        }

        assets = []

        # Convert raw API json into our internal model
        for asset in github_json["assets"]:
            assets.append(
                Asset(
                    name=asset["name"],
                    download_url=asset["browser_download_url"]
                )
            )

        return Release(
            version=github_json["tag_name"],
            assets=assets
        )


# ============================================================
# GitLab implementation
# ============================================================

class GitlabReleaseProvider(ReleaseProvider):

    def get_latest_release(self, package_name: str) -> Release:

        # Fake example response
        gitlab_json = {
            "tag_name": "v2.0.0",
            "assets": [
                {
                    "name": "tool.deb",
                    "url": "https://gitlab.com/tool.deb"
                },
                {
                    "name": "SHA256SUMS.txt",
                    "url": "https://gitlab.com/SHA256SUMS.txt"
                }
            ]
        }

        assets = []

        for asset in gitlab_json["assets"]:
            assets.append(
                Asset(
                    name=asset["name"],
                    download_url=asset["url"]
                )
            )

        return Release(
            version=gitlab_json["tag_name"],
            assets=assets
        )


# ============================================================
# NOTE:
# Detector responsibility:
#
# Figure out WHICH verification strategy should be used.
#
# This is important because APIs DO NOT say:
#
#   "this is checksum file"
#
# They just return a list of assets.
#
# So we must inspect filenames/extensions ourselves.
# ============================================================

class VerificationDetector:

    # Common checksum related filenames/extensions
    CHECKSUM_PATTERNS = [
        ".sha256",
        ".sha512",
        ".md5",
        "sha256sum",
        "sha512sum",
        "checksums.txt",
        "sha256sums.txt",
        "sha512sums.txt",
        "latest-linux.yml",
    ]

    def detect(self, release: Release) -> "VerificationStrategy":

        # Loop over every asset from release API
        for asset in release.assets:

            # Convert filename to lowercase for safer matching
            asset_name = asset.name.lower()

            # Check if filename matches known checksum patterns
            for pattern in self.CHECKSUM_PATTERNS:

                # Example:
                # app.tar.gz.sha256
                # SHA256SUMS.txt
                # latest-linux.yml
                if pattern in asset_name:

                    print(f"[Detector] Found checksum asset: {asset.name}")

                    # Return checksum verification strategy
                    return ChecksumFileVerification(asset)

        # If no checksum asset found
        print("[Detector] No checksum asset found")

        # Return strategy that represents unverified install
        return NoVerification()


# ============================================================
# NOTE:
# Verification strategy ONLY verifies.
#
# It does NOT:
# - fetch releases
# - detect files
# - download binaries
#
# Single Responsibility Principle.
# ============================================================

class VerificationStrategy(ABC):

    @abstractmethod
    def verify(self, package_file: str) -> bool:
        pass


# ============================================================
# Verification using checksum file
# ============================================================

class ChecksumFileVerification(VerificationStrategy):

    def __init__(self, checksum_asset: Asset):
        self.checksum_asset = checksum_asset

    def verify(self, package_file: str) -> bool:

        print("[Verifier] Downloading checksum file")
        print(f"[Verifier] Source: {self.checksum_asset.download_url}")

        # Normally:
        #
        # 1. download checksum file
        # 2. parse hashes
        # 3. calculate local hash
        # 4. compare hashes
        #
        # Skipped here for simplicity

        print(f"[Verifier] Verifying {package_file}")

        return True


# ============================================================
# Used when project provides NO verification support
# ============================================================

class NoVerification(VerificationStrategy):

    def verify(self, package_file: str) -> bool:

        print("[Verifier] No verification available")

        return False


# ============================================================
# Main installer service
# ============================================================

class Installer:

    def __init__(
        self,
        provider: ReleaseProvider,
        detector: VerificationDetector
    ):
        self.provider = provider
        self.detector = detector

    def install(
        self,
        package_name: str,
        allow_unverified: bool = False
    ):

        # Step 1:
        # Fetch release metadata from provider
        release = self.provider.get_latest_release(package_name)

        print(f"[Installer] Latest version: {release.version}")

        # Step 2:
        # Detect which verification strategy should be used
        verifier = self.detector.detect(release)

        # Step 3:
        # Find actual package asset
        #
        # NOTE:
        # Here we skip checksum files and only grab binaries
        package_asset = self._find_package_asset(release)

        if not package_asset:
            raise Exception("No installable package found")

        print(f"[Installer] Downloading {package_asset.name}")

        # Step 4:
        # Verify package
        verified = verifier.verify(package_asset.name)

        # Step 5:
        # Block installation if verification failed
        if not verified and not allow_unverified:

            print("[Installer] Installation blocked")
            print("[Installer] Package is unverified")

            return

        # Step 6:
        # Continue installation
        print("[Installer] Installing package")

    def _find_package_asset(
        self,
        release: Release
    ) -> Optional[Asset]:

        # Very naive example
        #
        # Real project would:
        # - detect platform
        # - detect architecture
        # - detect package type
        #
        # etc.

        for asset in release.assets:

            asset_name = asset.name.lower()

            # Skip checksum related files
            if (
                ".sha256" in asset_name
                or ".sha512" in asset_name
                or "sha256sum" in asset_name
                or "checksums" in asset_name
            ):
                continue

            # Return first non-checksum file
            return asset

        return None


# ============================================================
# GitHub install example
# ============================================================

github_installer = Installer(
    provider=GithubReleaseProvider(),
    detector=VerificationDetector()
)

github_installer.install("bat")


print()

# ============================================================
# GitLab install example
# ============================================================

gitlab_installer = Installer(
    provider=GitlabReleaseProvider(),
    detector=VerificationDetector()
)

gitlab_installer.install("neovim")


print()

# ============================================================
# Example:
# user explicitly allows unverified install
# ============================================================

class WebsiteReleaseProvider(ReleaseProvider):

    def get_latest_release(self, package_name: str) -> Release:

        # Website provides NO checksum files
        return Release(
            version="v3.0.0",
            assets=[
                Asset(
                    name="cool-app.zip",
                    download_url="https://example.com/cool-app.zip"
                )
            ]
        )


website_installer = Installer(
    provider=WebsiteReleaseProvider(),
    detector=VerificationDetector()
)

website_installer.install(
    "cool-app",
    allow_unverified=True
)