"""
Decorator Design Pattern Implementation - AppImage Manager Example

This module demonstrates the Decorator design pattern, which:
1. Attaches additional responsibilities to objects dynamically
2. Provides a flexible alternative to subclassing for extending functionality
3. Follows the Open/Closed Principle by allowing extension without modification

Why use the Decorator Pattern?
----------------------------
- FLEXIBILITY: Add or remove responsibilities at runtime
- SINGLE RESPONSIBILITY: Each decorator has one specific job
- COMPOSITION: Uses object composition instead of inheritance
- NON-INVASIVE: Adds functionality without modifying the original class

Key Components in Decorator Pattern:
---------------------------------
1. Component: The interface that the decorator and concrete components implement
2. Concrete Component: The original object that will be decorated
3. Decorator: Abstract class that implements the Component interface and holds a reference to a Component
4. Concrete Decorator: Adds functionality to the component while maintaining its interface

Additional Design Principles Demonstrated:
----------------------------------------
- Composition Over Inheritance: Using composition to extend behavior
- Open/Closed Principle: Classes are open for extension but closed for modification
- Interface Segregation: Components only depend on methods they need
- Least Knowledge: Decorators only interact with the component interface

This example shows how to implement the Decorator pattern to dynamically add features
like logging, caching, validation, and progress tracking to AppImage objects without
modifying their core implementation.
"""

import os
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict


# Reusing AppImageData from previous examples
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


# Base AppImage class - This is the 'Component' in the Decorator pattern
@dataclass
class AppImage:
    """Base appimage class - This is the 'Component' in the Decorator pattern.

    In the Decorator pattern, this class defines the interface that all
    concrete components and decorators must implement. This allows clients
    to work with any decorated or undecorated component through this interface.

    Why is this important?
    - Defines consistent methods that all decorators must support
    - Clients work with the same interface regardless of decoration
    - Allows decorators to be stacked in any order

    Attributes:
        data (AppImageData): The core data for this AppImage
    """

    data: AppImageData

    def __post_init__(self):
        """Initialize attributes after dataclass initialization."""
        # For convenience, expose common fields directly
        self.name = self.data.name
        self.download_url = self.data.download_url
        self.version = self.data.version
        self.display_name = self.data.display_name

    def download(self, download_dir: str) -> str:
        """Download the AppImage - This is a 'Component Method' in the Decorator pattern.

        This method defines part of the component interface that decorators
        can enhance or modify.

        Args:
            download_dir: Directory to download the file to

        Returns:
            str: Path to the downloaded file
        """
        file_path = os.path.join(download_dir, f"{self.name}-{self.version}.AppImage")
        print(f"Downloading {self.name} from {self.download_url}...")
        print(f"Downloaded to {file_path}")
        return file_path

    def get_info(self) -> Dict[str, Any]:
        """Get information about the AppImage - Another 'Component Method'.

        This method returns metadata about the AppImage, which decorators
        might enhance with additional information.

        Returns:
            Dict[str, Any]: Dictionary of AppImage information
        """
        return {
            "name": self.name,
            "version": self.version,
            "display_name": self.display_name,
            "download_url": self.download_url,
        }

    def verify(self, file_path: str) -> bool:
        """Verify the downloaded AppImage file - Another 'Component Method'.

        This method verifies the integrity of a downloaded file, which
        decorators might enhance with additional checks.

        Args:
            file_path: Path to the downloaded file

        Returns:
            bool: True if verification is successful
        """
        print(f"Verifying {self.name}...")
        # Basic verification logic
        return True


# Base Decorator class - This is the 'Decorator' in the Decorator pattern
class AppImageDecorator(AppImage):
    """Base decorator for AppImage - This is the 'Decorator' in the Decorator pattern.

    This class maintains a reference to a component object and implements
    the same interface. It forwards all requests to the component while
    potentially adding behavior before or after the forwarded calls.

    In the Decorator pattern, this class:
    - Implements the same interface as the component
    - Holds a reference to a component object
    - Delegates responsibilities to the component
    - May add behavior before or after delegating

    This allows for a chain of responsibility where multiple decorators
    can be stacked to add cumulative functionality.

    Attributes:
        _app_image: The wrapped AppImage component

    Note:
        This class doesn't need most of the usual dataclass initialization since
        it gets its data from the wrapped component. Instead, it overrides
        attribute access to transparently forward to the wrapped component.
    """

    def __init__(self, app_image: AppImage):
        """Initialize with the component to decorate.

        Args:
            app_image: The AppImage component to wrap
        """
        # Store the wrapped component
        self._app_image = app_image

        # For convenience, expose the same properties as AppImage
        # This is not typically needed in Python thanks to __getattr__,
        # but it makes the decorators type-compatible with AppImage
        self.data = app_image.data
        self.name = app_image.name
        self.download_url = app_image.download_url
        self.version = app_image.version
        self.display_name = app_image.display_name

    def __getattr__(self, name):
        """Forward attribute access to the wrapped component.

        This allows the decorator to transparently pass through
        any attribute access that it doesn't handle explicitly.

        Args:
            name: The name of the attribute to access

        Returns:
            The attribute from the wrapped component
        """
        return getattr(self._app_image, name)

    def download(self, download_dir: str) -> str:
        """Forward download request to the wrapped component.

        This base decorator simply delegates to the wrapped component
        without adding behavior. Concrete decorators will override this
        to add functionality before or after delegation.

        Args:
            download_dir: Directory to download the file to

        Returns:
            str: Path to the downloaded file
        """
        return self._app_image.download(download_dir)

    def get_info(self) -> Dict[str, Any]:
        """Forward get_info request to the wrapped component.

        Args:
            None

        Returns:
            Dict[str, Any]: Dictionary of AppImage information
        """
        return self._app_image.get_info()

    def verify(self, file_path: str) -> bool:
        """Forward verify request to the wrapped component.

        Args:
            file_path: Path to the downloaded file

        Returns:
            bool: True if verification is successful
        """
        return self._app_image.verify(file_path)


# Concrete Decorator implementations
class LoggingAppImageDecorator(AppImageDecorator):
    """Decorator that adds logging to AppImage operations.

    This 'Concrete Decorator' adds logging behavior to any
    AppImage component method that it wraps. It demonstrates how
    decorators can add behavior before and after method calls.

    By extending AppImageDecorator, it inherits the ability to
    wrap any AppImage component while maintaining the AppImage interface.
    """

    def __init__(self, app_image: AppImage, log_file: str = None):
        """Initialize with component and optional log file.

        Args:
            app_image: The AppImage component to wrap
            log_file: File path for logs (defaults to console logging)
        """
        super().__init__(app_image)
        self.log_file = log_file

    def _log(self, message: str):
        """Log a message to the configured destination.

        Args:
            message: The message to log
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"

        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{log_entry}\n")
        else:
            print(f"LOG: {log_entry}")

    def download(self, download_dir: str) -> str:
        """Add logging before and after download.

        This demonstrates how decorators can enhance behavior while
        maintaining the original method signature.

        Args:
            download_dir: Directory to download the file to

        Returns:
            str: Path to the downloaded file
        """
        self._log(f"Starting download of {self.name} version {self.version}")
        try:
            file_path = super().download(download_dir)
            self._log(f"Successfully downloaded {self.name} to {file_path}")
            return file_path
        except Exception as e:
            self._log(f"Error downloading {self.name}: {e}")
            raise

    def verify(self, file_path: str) -> bool:
        """Add logging to verification process.

        Args:
            file_path: Path to the downloaded file

        Returns:
            bool: True if verification is successful
        """
        self._log(f"Verifying {self.name} at {file_path}")
        result = super().verify(file_path)

        if result:
            self._log(f"Verification of {self.name} successful")
        else:
            self._log(f"Verification of {self.name} failed")

        return result

    def get_info(self) -> Dict[str, Any]:
        """Add logging when info is requested.

        Returns:
            Dict[str, Any]: Dictionary of AppImage information
        """
        self._log(f"Info requested for {self.name}")
        return super().get_info()


class CachingAppImageDecorator(AppImageDecorator):
    """Decorator that adds caching to AppImage operations.

    This 'Concrete Decorator' adds caching behavior to prevent
    redundant downloads of the same AppImage version. This shows
    how decorators can maintain state to optimize operations.
    """

    # Class-level cache shared across instances
    _download_cache: Dict[str, str] = {}

    def download(self, download_dir: str) -> str:
        """Add caching to download process.

        This method checks if the AppImage is already in the cache
        and returns the cached path if available, otherwise performs
        the download and caches the result.

        Args:
            download_dir: Directory to download the file to

        Returns:
            str: Path to the downloaded file
        """
        # Use a cache key that distinguishes different versions
        cache_key = f"{self.name}-{self.version}"

        # Check if this AppImage is already downloaded
        if cache_key in self._download_cache:
            cached_path = self._download_cache[cache_key]
            if os.path.exists(cached_path):
                print(f"Using cached version of {self.name} at {cached_path}")
                return cached_path

        # Not in cache or file doesn't exist, perform download
        file_path = super().download(download_dir)

        # Cache the result
        self._download_cache[cache_key] = file_path
        print(f"Cached {self.name} at {file_path}")

        return file_path

    def get_info(self) -> Dict[str, Any]:
        """Add cache information to info dictionary.

        Enhances the original info dictionary with caching status.

        Returns:
            Dict[str, Any]: Enhanced dictionary of AppImage information
        """
        info = super().get_info()

        # Add cache information
        cache_key = f"{self.name}-{self.version}"
        info["cached"] = cache_key in self._download_cache
        if info["cached"]:
            info["cache_path"] = self._download_cache[cache_key]

        return info


class ValidationAppImageDecorator(AppImageDecorator):
    """Decorator that adds extended validation to AppImage operations.

    This 'Concrete Decorator' enhances the verification process with
    additional validation steps beyond the basic verification.
    """

    def __init__(self, app_image: AppImage, strict_mode: bool = False):
        """Initialize with component and validation options.

        Args:
            app_image: The AppImage component to wrap
            strict_mode: Whether to use strict validation rules
        """
        super().__init__(app_image)
        self.strict_mode = strict_mode

    def verify(self, file_path: str) -> bool:
        """Add extra validation steps to verification.

        This method extends the basic verification with additional
        checks like file size, permissions, and signature validation.

        Args:
            file_path: Path to the downloaded file

        Returns:
            bool: True if all verification steps pass
        """
        # First, perform the basic verification
        if not super().verify(file_path):
            return False

        print(f"Performing extended validation for {self.name}...")

        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} does not exist")
            return False

        # Check file size
        file_size = os.path.getsize(file_path)
        if file_size < 1024:  # Just for demonstration
            print(f"Error: File size too small: {file_size} bytes")
            return False

        # Additional checks in strict mode
        if self.strict_mode:
            print(f"Performing strict validation for {self.name}...")

            # Simulate additional checks like executable permission and signature
            # In a real implementation, these would be actual checks
            print("Checking executable permissions and signature...")

        print(f"Extended validation passed for {self.name}")
        return True

    def get_info(self) -> Dict[str, Any]:
        """Add validation information to info dictionary.

        Returns:
            Dict[str, Any]: Enhanced dictionary with validation info
        """
        info = super().get_info()
        info["validation_level"] = "strict" if self.strict_mode else "standard"
        return info


class ProgressAppImageDecorator(AppImageDecorator):
    """Decorator that adds progress tracking to AppImage operations.

    This 'Concrete Decorator' adds progress reporting for long-running
    operations like downloads, showing how decorators can enhance
    user experience without changing the component interface.
    """

    def download(self, download_dir: str) -> str:
        """Add progress reporting to download process.

        This simulates a download with progress updates, demonstrating
        how decorators can add user feedback to operations.

        Args:
            download_dir: Directory to download the file to

        Returns:
            str: Path to the downloaded file
        """
        print(f"Starting download of {self.name} with progress tracking...")

        # Simulate progress updates
        for progress in range(0, 101, 20):
            # In a real implementation, this would update based on actual download progress
            print(f"Downloading {self.name}: {progress}% complete")
            time.sleep(0.1)  # Simulate time passing

        # Perform the actual download
        file_path = super().download(download_dir)

        print(f"Download of {self.name} completed: 100%")
        return file_path


# Example function that creates decorated AppImages
def create_decorated_appimage(
    name: str,
    arch_keyword: str,
    download_url: str,
    sha_download_url: str,
    version: str,
    display_name: str,
    sha_file_name: str,
    decoration_flags: Dict[str, bool],
    owner: str = "",
    repo: str = "",
) -> AppImage:
    """Create an AppImage with optional decorators based on flags.

    This demonstrates how decorators can be applied conditionally
    and in different combinations based on runtime parameters.

    Args:
        name: AppImage name
        arch_keyword: Architecture type
        download_url: URL to download from
        sha_download_url: URL for checksum file
        version: Version string
        display_name: Display name
        sha_file_name: Checksum filename
        decoration_flags: Dictionary of flags for each decorator type
        owner: Repository owner (optional)
        repo: Repository name (optional)

    Returns:
        An AppImage, possibly wrapped with decorators
    """
    # Create the base AppImage
    data = AppImageData(
        name=name,
        arch_keyword=arch_keyword,
        download_url=download_url,
        sha_download_url=sha_download_url,
        version=version,
        display_name=display_name,
        sha_file_name=sha_file_name,
        owner=owner,
        repo=repo,
    )

    app_image = AppImage(data=data)

    # Apply decorators based on flags
    if decoration_flags.get("logging", False):
        app_image = LoggingAppImageDecorator(app_image)

    if decoration_flags.get("caching", False):
        app_image = CachingAppImageDecorator(app_image)

    if decoration_flags.get("validation", False):
        strict = decoration_flags.get("strict_validation", False)
        app_image = ValidationAppImageDecorator(app_image, strict_mode=strict)

    if decoration_flags.get("progress", False):
        app_image = ProgressAppImageDecorator(app_image)

    return app_image


def main():
    """Example of the Decorator Design Pattern in action.

    This demonstrates:
    1. Creating a base AppImage component
    2. Applying various decorators individually
    3. Combining multiple decorators in different ways
    4. How the client code works with the same interface regardless of decoration

    The Decorator pattern allows for flexible enhancement of objects at runtime.
    """
    print("\n=== DECORATOR PATTERN DEMONSTRATION ===\n")

    # Create a basic AppImage
    print("1. Creating a basic undecorated AppImage...")
    basic_data = AppImageData(
        name="basic-app",
        arch_keyword="x86_64",
        download_url="https://example.com/downloads/basic-app.AppImage",
        sha_download_url="https://example.com/downloads/basic-app.AppImage.sha256",
        version="1.0",
        display_name="Basic App",
        sha_file_name="basic-app.AppImage.sha256",
    )
    basic_app = AppImage(data=basic_data)

    # Use the basic app
    print("\nUsing basic undecorated AppImage:")
    basic_app.download("/tmp/appimages")
    basic_app.verify("/tmp/appimages/basic-app-1.0.AppImage")
    print(f"Info: {basic_app.get_info()}")

    # Add a single decorator
    print("\n2. Adding a single decorator (logging)...")
    logging_app = LoggingAppImageDecorator(basic_app)

    # Use the app with logging decorator
    print("\nUsing AppImage with logging decorator:")
    logging_app.download("/tmp/appimages")
    logging_app.verify("/tmp/appimages/basic-app-1.0.AppImage")
    print(f"Info: {logging_app.get_info()}")

    # Combine multiple decorators
    print("\n3. Combining multiple decorators...")

    # First add logging, then caching
    print("\nUsing AppImage with logging and caching decorators:")
    logging_caching_app = CachingAppImageDecorator(logging_app)
    logging_caching_app.download("/tmp/appimages")  # Will log and cache
    logging_caching_app.download("/tmp/appimages")  # Will use cache and log

    # Different combination: validation and progress
    print("\nUsing AppImage with validation and progress decorators:")
    validation_progress_app = ProgressAppImageDecorator(
        ValidationAppImageDecorator(basic_app, strict_mode=True)
    )
    validation_progress_app.download("/tmp/appimages")  # Will show progress
    validation_progress_app.verify(
        "/tmp/appimages/basic-app-1.0.AppImage"
    )  # Will do strict validation

    # Using the convenience function for conditional decoration
    print("\n4. Using conditional decoration based on flags...")

    # Create with specific decorators enabled
    decorated_app = create_decorated_appimage(
        name="decorated-app",
        arch_keyword="x86_64",
        download_url="https://example.com/downloads/decorated-app.AppImage",
        sha_download_url="https://example.com/downloads/decorated-app.AppImage.sha256",
        version="2.0",
        display_name="Decorated App",
        sha_file_name="decorated-app.AppImage.sha256",
        decoration_flags={
            "logging": True,
            "caching": True,
            "validation": True,
            "strict_validation": False,
            "progress": True,
        },
    )

    # Use the fully decorated app
    print("\nUsing a fully decorated AppImage:")
    decorated_app.download("/tmp/appimages")
    decorated_app.verify("/tmp/appimages/decorated-app-2.0.AppImage")

    # Inspect the info to see the effect of decorators
    print("\n5. Inspecting info from decorated AppImage...")
    info = decorated_app.get_info()
    print(f"Decorated info: {info}")

    print("\n=== DECORATOR PATTERN BENEFITS ===")
    print("* Add responsibilities dynamically at runtime")
    print("* Add multiple responsibilities in different combinations")
    print("* Single Responsibility Principle: Each decorator has one job")
    print("* Open/Closed Principle: Extend functionality without modifying classes")
    print("* Composition over inheritance: More flexible than subclassing")

    print("\n=== END OF DECORATOR PATTERN DEMONSTRATION ===\n")


if __name__ == "__main__":
    main()
