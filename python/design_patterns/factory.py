"""
Factory Method Design Pattern Implementation - AppImage Manager Example

This module demonstrates the Factory Method design pattern, which:
1. Creates objects without exposing the instantiation logic to the client
2. Refers to the newly created object through a common interface
3. Allows subclasses to decide which class to instantiate

Why use the Factory Pattern?
---------------------------
- SEPARATION OF CONCERNS: Separates object creation from its use
- FLEXIBILITY: Makes adding new types of objects easy without changing existing code
- DECOUPLING: Client code doesn't need to know concrete implementations
- CONSISTENCY: All objects are created through a unified interface

Key Components in Factory Pattern:
---------------------------------
1. Product (AppImage): The interface/base class for objects the factory creates
2. Concrete Products (GithubAppImage, GitlabAppImage): Specific implementations
3. Creator (AppImageFactory): Declares the factory method
4. Concrete Creator (AppImageFactory methods): Implements factory methods to create products

Additional Design Principles Demonstrated:
----------------------------------------
- Dependency Injection: Dependencies are passed explicitly rather than created internally
- Composition Over Inheritance: Using data objects shared between classes
- DRY (Don't Repeat Yourself): Common data model to avoid duplication
- Single Responsibility: Each class has one clear purpose

This example shows how to handle app images from different sources (GitHub, GitLab)
while maintaining a consistent interface and providing persistence capabilities.
"""

import json
import os
from dataclasses import asdict, dataclass, field
from typing import Any, Dict


# Common data model shared between AppImage and AppConfig
@dataclass
class AppImageData:
    """Common data model for AppImage entities.

    This class demonstrates the "composition over inheritance" principle by providing
    a shared data structure that can be used by multiple classes. Instead of duplicating
    these fields in multiple classes, we define them once and reuse them.

    Why use a shared data class?
    - Avoids duplication of fields and methods across related classes
    - Creates a single source of truth for data structure
    - Makes changes to the data model easier (change in one place only)
    - Improves maintainability of the codebase

    Attributes:
        name (str): Unique identifier for the AppImage
        arch_keyword (str): Architecture type (e.g., x86_64)
        download_url (str): URL to download the AppImage from
        sha_download_url (str): URL to download the checksum file
        version (str): Version string of the AppImage
        display_name (str): User-friendly name to display
        sha_file_name (str): Filename of the checksum file
        owner (str, optional): Repository owner. Defaults to empty string.
        repo (str, optional): Repository name. Defaults to empty string.
    """

    name: str
    arch_keyword: str
    download_url: str
    sha_download_url: str
    version: str
    display_name: str
    sha_file_name: str
    owner: str = ""
    repo: str = ""


# Refactored Config classes
@dataclass
class GlobalConfig:
    """Configuration settings class."""

    config_dir: str
    config_file: str
    settings: Dict[str, Any]

    @classmethod
    def create_default(cls, config_dir=None):
        """Create a GlobalConfig with default settings."""
        config_dir = config_dir or os.path.expanduser("~/.config/appimages")
        config_file = os.path.join(config_dir, "global_config.json")

        # Default global settings
        settings = {
            "download_dir": os.path.expanduser("~/Downloads/AppImages"),
            "auto_update": True,
            "update_check_interval_days": 7,
            "default_arch": "x86_64",
        }

        return cls(config_dir=config_dir, config_file=config_file, settings=settings)

    @classmethod
    def load(cls, config_dir=None):
        """Load configuration from file."""
        config = cls.create_default(config_dir)

        # Create config directory if it doesn't exist
        if not os.path.exists(config.config_dir):
            os.makedirs(config.config_dir, exist_ok=True)

        # Load existing config if available
        if os.path.exists(config.config_file):
            try:
                with open(config.config_file, "r") as f:
                    loaded_settings = json.load(f)
                    config.settings.update(loaded_settings)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {config.config_file}, using defaults")

        return config

    def save(self):
        """Save global configuration to file."""
        # Ensure directory exists
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir, exist_ok=True)

        with open(self.config_file, "w") as f:
            json.dump(self.settings, f, indent=2)
        print(f"Global config saved to {self.config_file}")

    def get_setting(self, key, default=None):
        """Get a global setting."""
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        """Set a global setting."""
        self.settings[key] = value
        return self


# Base Config class
@dataclass
class BaseConfig:
    """Base configuration class."""

    name: str


# Refactored AppConfig - now using AppImageData
@dataclass
class AppConfig(BaseConfig):
    """Application-specific configuration."""

    data: AppImageData
    app_settings: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        # Ensure name is consistent
        self.name = self.data.name

    def save(self, config_dir):
        """Save the app config to a .json file."""
        app_config_dir = os.path.join(config_dir, "apps")
        os.makedirs(app_config_dir, exist_ok=True)

        # Convert to dict for serialization
        serialized_data = {
            "name": self.name,
            "data": asdict(self.data),
            "app_settings": self.app_settings,
        }

        file_path = os.path.join(app_config_dir, f"{self.name}.json")
        with open(file_path, "w") as f:
            json.dump(serialized_data, f, indent=2)
        print(f"App config saved to {file_path}")

    @classmethod
    def load(cls, name, config_dir):
        """Load app config from a .json file."""
        file_path = os.path.join(config_dir, "apps", f"{name}.json")

        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data_dict = json.load(f)

            # Convert back to AppImageData
            image_data = AppImageData(**data_dict["data"])
            return cls(
                name=data_dict["name"],
                data=image_data,
                app_settings=data_dict["app_settings"],
            )
        return None


# ConfigFactory class - simplified
@dataclass
class ConfigFactory:
    """Factory for creating configuration objects."""

    def create_app_config(self, data: AppImageData, app_settings=None):
        """Create an app-specific config."""
        return AppConfig(name=data.name, data=data, app_settings=app_settings or {})


# Refactored AppImage class - now using AppImageData
@dataclass
class AppImage:
    """Base appimage class - This is the 'Product' in the Factory Pattern.

    In the Factory Pattern, this base class defines the interface that all
    'products' (different types of AppImages) must implement. This allows
    client code to work with any AppImage object without knowing its specific type.

    Why is this important?
    - ABSTRACTION: Client code only needs to know about this interface, not concrete implementations
    - POLYMORPHISM: Different AppImage types can be used interchangeably
    - EXTENSIBILITY: New AppImage types can be added without changing existing code

    Think of this as a blueprint that all specific AppImage types must follow.

    Attributes:
        data (AppImageData): Common data for all AppImage types using composition pattern

    Note:
        The __post_init__ method exposes common fields directly for convenience,
        demonstrating how composition can provide the benefits of inheritance
        without tight coupling.
    """

    data: AppImageData

    def __post_init__(self):
        """Initialize additional attributes after dataclass initialization.

        This is called automatically after the object is created and
        exposes commonly used fields from the data object directly on the
        AppImage for convenience.
        """
        # For convenience, expose common fields directly
        self.name = self.data.name
        self.download_url = self.data.download_url
        self.version = self.data.version
        self.display_name = self.data.display_name

    def download(self, download_dir):
        """Download the appimage file.

        This is the interface method that all concrete AppImage classes must implement.
        It represents the common behavior expected from all AppImage types.

        Args:
            download_dir (str): Directory where the AppImage should be downloaded
        """
        print(f"Downloading {self.name} to {download_dir} from {self.download_url}...")
        # Simulate download
        print(f"{self.name} downloaded successfully.")

    def to_config(self):
        """Convert appimage to a config object for persistence.

        This method demonstrates how objects can be converted to a different
        representation for storage/serialization purposes.

        Returns:
            AppConfig: Configuration object for storing AppImage data
        """
        return AppConfig(name=self.data.name, data=self.data)


# Specialized AppImages
@dataclass
class GithubAppImage(AppImage):
    """Github-specific appimage implementation - This is a 'Concrete Product' in the Factory Pattern.

    In the Factory Pattern, concrete products are specific implementations of the
    abstract product (AppImage). This class handles GitHub-specific behavior while
    maintaining the same interface as the base class.

    Why have specific implementations?
    - SPECIALIZATION: Each source may have unique requirements for downloading
    - ENCAPSULATION: Keeps source-specific details isolated in their own classes
    - SINGLE RESPONSIBILITY: Each class handles one specific type of AppImage

    Without modifying client code, we can add new AppImage sources by just creating
    new concrete product classes like this one.
    """

    def download(self, download_dir):
        """Download the appimage file from GitHub.

        Overrides the base download method with GitHub-specific implementation.
        This polymorphic behavior is key to the Factory Pattern - clients can call
        the same method on any AppImage without knowing the concrete type.

        Args:
            download_dir (str): Directory where the AppImage should be downloaded
        """
        print(f"Downloading {self.name} from GitHub to {download_dir}...")
        # GitHub-specific download logic would go here
        # For example: using GitHub API, handling GitHub rate limits, etc.
        print(f"{self.name} downloaded successfully from GitHub.")


@dataclass
class GitlabAppImage(AppImage):
    """GitLab-specific appimage implementation - This is another 'Concrete Product'.

    This class implements the AppImage interface for GitLab sources.
    Having multiple concrete products demonstrates the power of the Factory Pattern:
    the client code can work with any of these products through the common interface.

    The Factory Pattern allows us to add as many concrete products as needed without
    changing how clients interact with them.
    """

    def download(self, download_dir):
        """Download the appimage file from GitLab.

        Implements GitLab-specific download functionality while maintaining
        the same method signature as the base class.

        Args:
            download_dir (str): Directory where the AppImage should be downloaded
        """
        print(f"Downloading {self.name} from GitLab to {download_dir}...")
        # GitLab-specific download logic would go here
        # For example: using GitLab API authentication, handling GitLab CI artifacts, etc.
        print(f"{self.name} downloaded successfully from GitLab.")


# AppImageFactory - simplified
@dataclass
class AppImageFactory:
    """Factory for creating appimage objects - This is the 'Creator' in the Factory Pattern.

    The Factory class is the heart of the Factory Pattern. It's responsible for:
    - Creating and returning different product objects
    - Hiding the details of object instantiation from clients
    - Centralizing the object creation logic in one place

    Why use a Factory class?
    - CENTRALIZATION: All creation logic is in one place, easier to maintain
    - ENCAPSULATION: Hides how objects are created from client code
    - FLEXIBILITY: Can change how objects are created without affecting clients
    - CONDITIONAL CREATION: Can create different objects based on conditions

    In real applications, this factory might:
    - Query APIs to determine the best download location
    - Check system compatibility before creating objects
    - Apply additional validation or processing
    """

    def create_appimage(self, data: AppImageData):
        """Create an appimage object based on the download URL.

        This is the key 'factory method' that decides which concrete product to create.
        It examines the data and makes a decision about which specific class to instantiate.

        The client code doesn't need to know HOW to create different AppImage types,
        it just provides the data and gets back the appropriate object.

        Args:
            data (AppImageData): The data needed to create an AppImage

        Returns:
            AppImage: A concrete implementation of AppImage (GithubAppImage, GitlabAppImage, etc.)
        """
        # This decision logic could be more sophisticated in a real application
        # For example, checking for API tokens, user preferences, etc.
        if "github" in data.download_url:
            return GithubAppImage(data=data)
        elif "gitlab" in data.download_url:
            return GitlabAppImage(data=data)
        else:
            # Default case - use base AppImage
            return AppImage(data=data)

    def create_from_config(self, config: AppConfig):
        """Create an AppImage from a config object.

        This is a convenience method that demonstrates how a factory can provide
        multiple creation pathways while maintaining the same interface.

        Args:
            config (AppConfig): Configuration to create an AppImage from

        Returns:
            AppImage: A concrete implementation based on the config data
        """
        return self.create_appimage(data=config.data)


# AppImageManager - using the simplified classes
@dataclass
class AppImageManager:
    """Manager for appimages - This coordinates the Factory Pattern components.

    The AppImageManager demonstrates several good design principles:

    1. DEPENDENCY INJECTION: Dependencies are passed in, not created internally
    2. FACADE PATTERN: Provides a simplified interface to complex subsystems
    3. SINGLE RESPONSIBILITY: Manages the workflow without creating objects directly

    Why use a Manager class with a Factory?
    - SEPARATION OF CONCERNS: Factory focuses on creation, Manager on orchestration
    - ABSTRACTION LAYERING: Provides higher-level operations to the client
    - WORKFLOW MANAGEMENT: Handles the complete lifecycle from creation to persistence

    Attributes:
        factory (AppImageFactory): Factory for creating AppImage objects
        config_factory (ConfigFactory): Factory for creating configuration objects
        global_config (GlobalConfig): Application global configuration
    """

    factory: AppImageFactory
    config_factory: ConfigFactory
    global_config: GlobalConfig

    def download_appimage(
        self,
        name,
        arch_keyword,
        download_url,
        sha_download_url,
        version,
        display_name,
        sha_file_name,
        owner="",
        repo="",
    ):
        """Download an AppImage using the factory pattern.

        This method demonstrates how client code interacts with the factory.
        It creates the data, passes it to the factory, and uses the resulting object.

        The client never needs to know which concrete AppImage class is created.

        Args:
            name (str): Unique identifier for the AppImage
            arch_keyword (str): Architecture type (e.g., x86_64)
            download_url (str): URL to download the AppImage from
            sha_download_url (str): URL to download the checksum file
            version (str): Version string of the AppImage
            display_name (str): User-friendly name to display
            sha_file_name (str): Filename of the checksum file
            owner (str, optional): Repository owner. Defaults to empty string.
            repo (str, optional): Repository name. Defaults to empty string.

        Returns:
            AppImage: A concrete implementation of AppImage created by the factory
        """
        # Create data object
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

        # Create and download appimage - notice how we don't care about the concrete type!
        appimage = self.factory.create_appimage(data)
        download_dir = self.global_config.get_setting("download_dir")
        appimage.download(download_dir)
        return appimage

    def save_appimage_config(self, appimage, app_settings=None):
        """Save AppImage configuration with optional settings.

        Shows how objects created by the factory can be persisted for later use.

        Args:
            appimage (AppImage): The AppImage to save configuration for
            app_settings (dict, optional): Application-specific settings. Defaults to None.

        Returns:
            AppConfig: The saved configuration object
        """
        config = appimage.to_config()
        if app_settings:
            config.app_settings = app_settings
        config.save(self.global_config.config_dir)
        return config

    def load_appimage_from_config(self, name):
        """Load AppImage from saved configuration.

        Shows the full circle of the Factory Pattern - creating objects from saved data.
        This demonstrates how the factory can create objects from different sources
        (direct parameters or saved configurations).

        Args:
            name (str): The name of the AppImage to load

        Returns:
            AppImage: A concrete implementation of AppImage created by the factory,
                     or None if configuration not found
        """
        config = AppConfig.load(name, self.global_config.config_dir)
        if config:
            return self.factory.create_from_config(config)
        return None


# Update the main function
def main():
    """Example of the Factory Design Pattern in action.

    This demonstrates:
    1. Creating different types of AppImages through a factory
    2. Using dependency injection instead of global state
    3. How configs work with the factory pattern
    4. The complete lifecycle of object creation, saving, and loading
    """
    print("\n=== FACTORY PATTERN DEMONSTRATION ===\n")

    # Setup phase - create dependencies
    print("1. Setting up configurations...")
    global_config = GlobalConfig.create_default(
        "./python/design_patterns/example_config"
    )
    global_config.set_setting("download_dir", "./python/design_patterns/downloads")
    global_config.save()

    config_factory = ConfigFactory()
    app_factory = AppImageFactory()
    manager = AppImageManager(
        factory=app_factory, config_factory=config_factory, global_config=global_config
    )

    # Factory pattern in action - creating different concrete implementations
    print("\n2. Using factory to create different AppImage types...")

    # GitHub implementation
    github_image = manager.download_appimage(
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

    # GitLab implementation
    gitlab_image = manager.download_appimage(
        name="gitlab-app",
        arch_keyword="x86_64",
        download_url="https://gitlab.com/owner/repo/-/releases/v1.0/app.AppImage",
        sha_download_url="https://gitlab.com/owner/repo/-/releases/v1.0/app.AppImage.sha256",
        version="2.0",
        display_name="GitLab App",
        sha_file_name="app.AppImage.sha256",
        owner="owner",
        repo="repo",
    )

    # Verify factory created proper concrete implementations
    print(
        f"\nFactory created: {github_image.__class__.__name__} and {gitlab_image.__class__.__name__}"
    )

    # Demonstrate config saving and loading
    print("\n3. Demonstrating config persistence...")
    github_settings = {"auto_update": True, "launch_at_startup": False}
    gitlab_settings = {"auto_update": False, "launch_at_startup": True}

    manager.save_appimage_config(github_image, github_settings)
    manager.save_appimage_config(gitlab_image, gitlab_settings)

    # Load from config - factory creates the right objects
    print("\n4. Loading apps from saved configurations...")
    loaded_github = manager.load_appimage_from_config("github-app")
    loaded_gitlab = manager.load_appimage_from_config("gitlab-app")

    if loaded_github and loaded_gitlab:
        print(
            f"Loaded: {loaded_github.__class__.__name__} version {loaded_github.version}"
        )
        print(
            f"Loaded: {loaded_gitlab.__class__.__name__} version {loaded_gitlab.version}"
        )

    print("\n=== END OF FACTORY PATTERN DEMONSTRATION ===\n")


if __name__ == "__main__":
    main()
