"""
Strategy Design Pattern Implementation - AppImage Manager Example

This module demonstrates the Strategy design pattern, which:
1. Defines a family of algorithms and makes them interchangeable
2. Allows the algorithm to vary independently from clients that use it
3. Enables selecting different algorithms at runtime

Why use the Strategy Pattern?
----------------------------
- FLEXIBILITY: Algorithms can be selected at runtime
- ENCAPSULATION: Implementation details of algorithms are hidden
- OPEN/CLOSED: New strategies can be added without modifying existing code
- COMPOSITION: Favors composition over inheritance for behavior reuse

Key Components in Strategy Pattern:
---------------------------------
1. Strategy: Interface/Protocol that defines how algorithms will be used
2. Concrete Strategies: Specific implementations of the strategy interface
3. Context: Class that uses the strategies and may allow switching between them
4. Client: Code that creates the concrete strategy and context objects

Additional Design Principles Demonstrated:
----------------------------------------
- Dependency Injection: Strategies are injected into the context
- Single Responsibility: Each strategy handles one specific algorithm
- Interface Segregation: Clients only depend on the methods they need
- Liskov Substitution: Different strategies can be used interchangeably

This example shows how to implement the Strategy pattern for download and verification
algorithms in an AppImage management system, allowing flexible selection of different
methods based on requirements or preferences.
"""

from dataclasses import dataclass
from typing import Any, Protocol


# Reusing the AppImageData class concept from our previous examples
@dataclass
class AppImageData:
    """Common data model for AppImage entities."""

    name: str
    arch_keyword: str
    download_url: str
    sha_download_url: str
    version: str
    display_name: str
    sha_file_name: str
    owner: str = ""
    repo: str = ""


@dataclass
class AppImage:
    """Base appimage class."""

    data: AppImageData

    def __post_init__(self):
        """Initialize additional attributes after dataclass initialization."""
        # For convenience, expose common fields directly
        self.name = self.data.name
        self.download_url = self.data.download_url
        self.version = self.data.version
        self.display_name = self.data.display_name


# Download Strategy Protocol (Interface)
class DownloadStrategy(Protocol):
    """Download strategy interface - This is the 'Strategy' in the Strategy Pattern.

    In the Strategy Pattern, this Protocol defines the common interface that all
    concrete download strategies must implement. This allows the context class
    to work with any download strategy without knowing its specific implementation.

    Why use a Protocol?
    - Defines a contract for all download strategies
    - Enables loose coupling between algorithms and their users
    - Supports duck typing while providing type hinting benefits

    Different download strategies can be swapped at runtime as long as they
    implement this interface, following the Strategy Pattern principles.
    """

    def download(self, appimage: AppImage, destination_dir: str) -> str:
        """Download the AppImage to the specified destination directory.

        Args:
            appimage: The AppImage to download
            destination_dir: Directory to download the file to

        Returns:
            str: The path to the downloaded file
        """
        ...


# Verification Strategy Protocol (Interface)
class VerificationStrategy(Protocol):
    """Verification strategy interface - This is another 'Strategy' in the Strategy Pattern.

    This Protocol defines how all verification strategies should behave. By separating
    verification from download, we follow the Single Responsibility Principle and
    allow independent selection of verification methods.

    This demonstrates how the Strategy Pattern can be applied to multiple aspects
    of the same system, creating a flexible, modular design.
    """

    def verify(self, file_path: str, appimage: AppImage) -> bool:
        """Verify the downloaded file's integrity.

        Args:
            file_path: Path to the downloaded file
            appimage: The AppImage with verification data

        Returns:
            bool: True if verification passes, False otherwise
        """
        ...


# Concrete Download Strategies
class HTTPDownloadStrategy:
    """HTTP Download Strategy - This is a 'Concrete Strategy' in the Strategy Pattern.

    This class implements the DownloadStrategy interface for HTTP downloads.
    It encapsulates all the logic specific to HTTP downloads, separating it
    from other concerns in the system.

    In the Strategy Pattern, concrete strategies implement the algorithm interface
    and can be used interchangeably by the context.
    """

    def __init__(self, user_agent: str = "AppImageManager/1.0", timeout: int = 30):
        """Initialize with HTTP-specific parameters.

        Args:
            user_agent: User agent string to use for HTTP requests
            timeout: Connection timeout in seconds
        """
        self.user_agent = user_agent
        self.timeout = timeout

    def download(self, appimage: AppImage, destination_dir: str) -> str:
        """Download the AppImage using HTTP.

        Args:
            appimage: The AppImage to download
            destination_dir: Directory to download to

        Returns:
            str: The path to the downloaded file
        """
        # In a real implementation, this would use requests, urllib, or another HTTP library
        file_path = f"{destination_dir}/{appimage.name}.AppImage"
        print(f"[HTTP] Downloading {appimage.name} from {appimage.download_url}")
        print(f"[HTTP] Using User-Agent: {self.user_agent}, timeout: {self.timeout}s")
        print(f"[HTTP] Downloaded to {file_path}")
        return file_path


class FTPDownloadStrategy:
    """FTP Download Strategy - Another 'Concrete Strategy'.

    This class implements the DownloadStrategy interface for FTP downloads.
    It demonstrates how different algorithms can implement the same interface
    but have completely different internal implementations.
    """

    def __init__(self, active_mode: bool = False, timeout: int = 60):
        """Initialize with FTP-specific parameters.

        Args:
            active_mode: Whether to use active mode FTP (vs passive)
            timeout: Connection timeout in seconds
        """
        self.active_mode = active_mode
        self.timeout = timeout

    def download(self, appimage: AppImage, destination_dir: str) -> str:
        """Download the AppImage using FTP.

        Args:
            appimage: The AppImage to download
            destination_dir: Directory to download to

        Returns:
            str: The path to the downloaded file
        """
        # In a real implementation, this would use ftplib or another FTP client
        file_path = f"{destination_dir}/{appimage.name}.AppImage"
        mode = "Active" if self.active_mode else "Passive"
        print(f"[FTP] Downloading {appimage.name} from {appimage.download_url}")
        print(f"[FTP] Using {mode} mode, timeout: {self.timeout}s")
        print(f"[FTP] Downloaded to {file_path}")
        return file_path


class TorrentDownloadStrategy:
    """Torrent Download Strategy - Another 'Concrete Strategy'.

    Implements peer-to-peer download via torrent protocol.
    This demonstrates how the Strategy Pattern allows for completely
    different algorithms to be added without modifying existing code.
    """

    def __init__(self, max_peers: int = 50, max_upload_rate: int = 100):
        """Initialize with torrent-specific parameters.

        Args:
            max_peers: Maximum number of peers to connect to
            max_upload_rate: Maximum upload rate in KB/s
        """
        self.max_peers = max_peers
        self.max_upload_rate = max_upload_rate

    def download(self, appimage: AppImage, destination_dir: str) -> str:
        """Download the AppImage using BitTorrent.

        Args:
            appimage: The AppImage to download
            destination_dir: Directory to download to

        Returns:
            str: The path to the downloaded file
        """
        # In a real implementation, this would use libtorrent or another torrent library
        file_path = f"{destination_dir}/{appimage.name}.AppImage"
        print(f"[TORRENT] Downloading {appimage.name}")
        print(
            f"[TORRENT] Using max peers: {self.max_peers}, upload limit: {self.max_upload_rate}KB/s"
        )
        print(f"[TORRENT] Downloaded to {file_path}")
        return file_path


# Concrete Verification Strategies
class ChecksumVerificationStrategy:
    """Checksum Verification Strategy - A 'Concrete Strategy' for verification.

    This class implements the VerificationStrategy interface for checksum-based
    verification, commonly used to verify file integrity.
    """

    def __init__(self, algorithm: str = "sha256"):
        """Initialize with verification-specific parameters.

        Args:
            algorithm: Hash algorithm to use (sha256, md5, etc.)
        """
        self.algorithm = algorithm

    def verify(self, file_path: str, appimage: AppImage) -> bool:
        """Verify the file using a checksum.

        Args:
            file_path: Path to the downloaded file
            appimage: AppImage with verification information

        Returns:
            bool: True if verification passes
        """
        # In a real implementation, this would calculate and compare checksums
        print(f"[CHECKSUM] Verifying {file_path} using {self.algorithm}")
        print(f"[CHECKSUM] Verification passed for {appimage.name}")
        return True


class SignatureVerificationStrategy:
    """Signature Verification Strategy - Another 'Concrete Strategy' for verification.

    This class implements the VerificationStrategy interface for signature-based
    verification, which is more secure than checksum verification.
    """

    def __init__(self, keyserver: str = "keys.openpgp.org"):
        """Initialize with verification-specific parameters.

        Args:
            keyserver: Server to fetch public keys from
        """
        self.keyserver = keyserver

    def verify(self, file_path: str, appimage: AppImage) -> bool:
        """Verify the file using a digital signature.

        Args:
            file_path: Path to the downloaded file
            appimage: AppImage with verification information

        Returns:
            bool: True if verification passes
        """
        # In a real implementation, this would verify using GPG or similar
        print(f"[SIGNATURE] Verifying {file_path} using keys from {self.keyserver}")
        print(f"[SIGNATURE] Verification passed for {appimage.name}")
        return True


# Context class that uses the strategies
@dataclass
class AppImageDownloader:
    """AppImage downloader - This is the 'Context' in the Strategy Pattern.

    The Context maintains a reference to a Strategy object and delegates
    the algorithm execution to it. This class doesn't implement the algorithm
    itself but relies on the Strategy to do so.

    This class demonstrates several key aspects of the Strategy Pattern:
    - It accepts strategies through dependency injection
    - It delegates work to the strategies rather than implementing it
    - It allows for changing strategies at runtime

    Attributes:
        download_strategy: The strategy used to download AppImages
        verification_strategy: The strategy used to verify downloads
        download_dir: Directory where AppImages will be downloaded
    """

    download_strategy: Any  # Using Any to accommodate duck typing
    verification_strategy: Any  # Using Any to accommodate duck typing
    download_dir: str

    def download_and_verify(self, appimage: AppImage) -> bool:
        """Download and verify an AppImage using the configured strategies.

        This method demonstrates how the Context delegates to the strategies
        without knowing their implementation details.

        Args:
            appimage: The AppImage to download and verify

        Returns:
            bool: True if download and verification succeeded
        """
        try:
            # Use the download strategy to download the file
            file_path = self.download_strategy.download(appimage, self.download_dir)

            # Use the verification strategy to verify the downloaded file
            if self.verification_strategy.verify(file_path, appimage):
                print(f"Successfully downloaded and verified: {appimage.name}")
                return True
            else:
                print(f"Verification failed for: {appimage.name}")
                return False

        except Exception as e:
            print(f"Error downloading {appimage.name}: {e}")
            return False

    def set_download_strategy(self, download_strategy: Any) -> None:
        """Change the download strategy at runtime.

        This demonstrates a key benefit of the Strategy Pattern:
        the ability to switch algorithms at runtime.

        Args:
            download_strategy: The new download strategy to use
        """
        print(f"Changing download strategy to: {download_strategy.__class__.__name__}")
        self.download_strategy = download_strategy

    def set_verification_strategy(self, verification_strategy: Any) -> None:
        """Change the verification strategy at runtime.

        Args:
            verification_strategy: The new verification strategy to use
        """
        print(
            f"Changing verification strategy to: {verification_strategy.__class__.__name__}"
        )
        self.verification_strategy = verification_strategy


def main():
    """Example of the Strategy Design Pattern in action.

    This demonstrates:
    1. Creating different strategies for download and verification
    2. Using these strategies with a context class
    3. Changing strategies at runtime
    4. How new strategies can be added without modifying existing code

    The Strategy pattern enables selecting different algorithms at runtime,
    making the system more flexible and extensible.
    """
    print("\n=== STRATEGY PATTERN DEMONSTRATION ===\n")

    # Create sample AppImage
    github_data = AppImageData(
        name="github-app",
        arch_keyword="x86_64",
        download_url="https://github.com/owner/repo/releases/download/v1.0/app.AppImage",
        sha_download_url="https://github.com/owner/repo/releases/download/v1.0/app.AppImage.sha256",
        version="1.0",
        display_name="GitHub App",
        sha_file_name="app.AppImage.sha256",
        owner="owner",
        repo="repo",
    )
    github_image = AppImage(data=github_data)

    # Create strategies
    print("1. Creating download and verification strategies...")
    http_strategy = HTTPDownloadStrategy(user_agent="AppImageManager/2.0", timeout=60)
    ftp_strategy = FTPDownloadStrategy(active_mode=True)
    torrent_strategy = TorrentDownloadStrategy(max_peers=100)

    checksum_strategy = ChecksumVerificationStrategy(algorithm="sha256")
    signature_strategy = SignatureVerificationStrategy(keyserver="keys.gnupg.net")

    # Create downloader with initial strategies
    print("\n2. Creating downloader with HTTP and checksum strategies...")
    downloader = AppImageDownloader(
        download_strategy=http_strategy,
        verification_strategy=checksum_strategy,
        download_dir="/tmp/appimages",
    )

    # Download using initial strategies
    print("\n3. Downloading with HTTP strategy and checksum verification...")
    downloader.download_and_verify(github_image)

    # Change download strategy at runtime
    print("\n4. Changing to FTP download strategy...")
    downloader.set_download_strategy(ftp_strategy)
    downloader.download_and_verify(github_image)

    # Change verification strategy at runtime
    print("\n5. Changing to signature verification strategy...")
    downloader.set_verification_strategy(signature_strategy)
    downloader.download_and_verify(github_image)

    # Use torrent strategy
    print("\n6. Changing to torrent download strategy...")
    downloader.set_download_strategy(torrent_strategy)
    downloader.download_and_verify(github_image)

    print("\n=== STRATEGY PATTERN BENEFITS ===")
    print("* Algorithms can be selected at runtime")
    print("* New algorithms can be added without modifying existing code")
    print("* Different algorithms can be used in different contexts")
    print("* Algorithm implementations are encapsulated and isolated")

    print("\n=== END OF STRATEGY PATTERN DEMONSTRATION ===\n")


if __name__ == "__main__":
    main()
