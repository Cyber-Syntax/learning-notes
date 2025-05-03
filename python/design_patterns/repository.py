"""
Repository Design Pattern Implementation - AppImage Manager Example

This module demonstrates the Repository design pattern, which:
1. Separates the domain model from the data access logic
2. Provides an abstraction layer over the data storage mechanism
3. Centralizes data access operations in specific repository classes
4. Allows switching between different storage implementations transparently

Why use the Repository Pattern?
-----------------------------
- ABSTRACTION: Hides data storage details from the domain model
- TESTABILITY: Makes domain logic easier to test with mock repositories
- MAINTAINABILITY: Centralizes data access code in one place
- FLEXIBILITY: Allows changing storage mechanisms without affecting domain code

Key Components in Repository Pattern:
----------------------------------
1. Repository Interface: Defines methods for accessing and manipulating domain objects
2. Concrete Repositories: Implementations for specific storage mechanisms
3. Domain Model: Business objects that the repositories store and retrieve
4. Query Objects: Optional specifications that describe what data to retrieve

Additional Design Principles Demonstrated:
----------------------------------------
- Separation of Concerns: Domain logic vs. data access
- Interface Segregation: Clients depend only on methods they need
- Dependency Inversion: Domain depends on repository abstraction, not implementation
- Single Responsibility: Each repository handles one domain entity type

This example shows how to implement the Repository pattern for AppImage management,
providing different storage mechanisms (file-based, in-memory, SQLite) while keeping
the domain logic clean and unaware of storage details.
"""

import json
import os
import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Protocol


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


@dataclass
class AppImage:
    """AppImage domain entity - The main business object the repository manages.

    This class represents the domain entity that repositories will store and retrieve.
    It's focused on domain behavior and business rules, not on how it's stored.

    In the Repository Pattern, domain entities should be persistence-ignorant,
    meaning they don't know or care about how they're stored.
    """

    data: AppImageData
    last_updated: Optional[datetime] = None

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # For convenience, expose common fields directly
        self.name = self.data.name
        self.download_url = self.data.download_url
        self.version = self.data.version
        self.display_name = self.data.display_name

        # Set last_updated if not provided
        if not self.last_updated:
            self.last_updated = datetime.now()


# Repository interface - defines common operations across all repository implementations
class AppImageRepository(Protocol):
    """Repository interface for AppImage entities - This defines the Repository Pattern contract.

    In the Repository Pattern, this interface defines the operations that any
    concrete repository must support, regardless of the underlying storage mechanism.

    The domain code depends on this abstraction rather than concrete implementations,
    following the Dependency Inversion Principle.

    This interface shows the standard CRUD operations (Create, Read, Update, Delete)
    plus additional query methods typical in a repository.
    """

    def add(self, app_image: AppImage) -> None:
        """Add an AppImage to the repository.

        Args:
            app_image: The AppImage to store
        """
        ...

    def update(self, app_image: AppImage) -> None:
        """Update an existing AppImage in the repository.

        Args:
            app_image: The AppImage with updated data
        """
        ...

    def remove(self, name: str) -> None:
        """Remove an AppImage from the repository.

        Args:
            name: The name of the AppImage to remove
        """
        ...

    def get_by_name(self, name: str) -> Optional[AppImage]:
        """Get an AppImage by its name.

        Args:
            name: The name of the AppImage to retrieve

        Returns:
            The AppImage if found, None otherwise
        """
        ...

    def get_all(self) -> List[AppImage]:
        """Get all AppImages in the repository.

        Returns:
            A list of all AppImages
        """
        ...

    def find_by_display_name(self, display_name: str) -> List[AppImage]:
        """Find AppImages by display name (possibly multiple matches).

        Args:
            display_name: The display name to search for

        Returns:
            A list of matching AppImages
        """
        ...

    def find_by_version(self, version: str) -> List[AppImage]:
        """Find AppImages by version.

        Args:
            version: The version to search for

        Returns:
            A list of matching AppImages
        """
        ...

    def count(self) -> int:
        """Count the number of AppImages in the repository.

        Returns:
            The number of AppImages
        """
        ...

    def clear(self) -> None:
        """Remove all AppImages from the repository."""
        ...


# In-memory repository implementation
class InMemoryAppImageRepository:
    """In-memory implementation of AppImageRepository.

    This 'Concrete Repository' implements the AppImageRepository interface
    using a simple in-memory dictionary. This is useful for testing,
    prototyping, or small applications.

    In the Repository Pattern, concrete repositories implement storage-specific
    code while keeping the same interface, allowing the domain code to
    remain storage-agnostic.
    """

    def __init__(self):
        """Initialize an empty repository."""
        self._app_images: Dict[str, AppImage] = {}

    def add(self, app_image: AppImage) -> None:
        """Add an AppImage to the repository.

        Args:
            app_image: The AppImage to store
        """
        if app_image.name in self._app_images:
            raise KeyError(f"AppImage with name '{app_image.name}' already exists")

        # Make a copy to ensure immutability
        self._app_images[app_image.name] = app_image

    def update(self, app_image: AppImage) -> None:
        """Update an existing AppImage in the repository.

        Args:
            app_image: The AppImage with updated data
        """
        if app_image.name not in self._app_images:
            raise KeyError(f"AppImage with name '{app_image.name}' not found")

        # Update the last_updated timestamp
        app_image.last_updated = datetime.now()

        # Update the stored AppImage
        self._app_images[app_image.name] = app_image

    def remove(self, name: str) -> None:
        """Remove an AppImage from the repository.

        Args:
            name: The name of the AppImage to remove
        """
        if name not in self._app_images:
            raise KeyError(f"AppImage with name '{name}' not found")

        del self._app_images[name]

    def get_by_name(self, name: str) -> Optional[AppImage]:
        """Get an AppImage by its name.

        Args:
            name: The name of the AppImage to retrieve

        Returns:
            The AppImage if found, None otherwise
        """
        return self._app_images.get(name)

    def get_all(self) -> List[AppImage]:
        """Get all AppImages in the repository.

        Returns:
            A list of all AppImages
        """
        return list(self._app_images.values())

    def find_by_display_name(self, display_name: str) -> List[AppImage]:
        """Find AppImages by display name.

        Args:
            display_name: The display name to search for

        Returns:
            A list of matching AppImages
        """
        return [
            app for app in self._app_images.values() if app.display_name == display_name
        ]

    def find_by_version(self, version: str) -> List[AppImage]:
        """Find AppImages by version.

        Args:
            version: The version to search for

        Returns:
            A list of matching AppImages
        """
        return [app for app in self._app_images.values() if app.version == version]

    def count(self) -> int:
        """Count the number of AppImages in the repository.

        Returns:
            The number of AppImages
        """
        return len(self._app_images)

    def clear(self) -> None:
        """Remove all AppImages from the repository."""
        self._app_images.clear()


# File-based repository implementation
class FileAppImageRepository:
    """File-based implementation of AppImageRepository.

    This 'Concrete Repository' implements the AppImageRepository interface
    using JSON files for persistence. Each AppImage is stored in a separate
    file within a directory.

    This demonstrates how the Repository Pattern allows for different storage
    mechanisms while keeping the same interface, making the storage choice
    transparent to the domain code.
    """

    def __init__(self, storage_dir: str):
        """Initialize with the storage directory.

        Args:
            storage_dir: Directory where AppImage data will be stored
        """
        self.storage_dir = storage_dir

        # Ensure storage directory exists
        os.makedirs(self.storage_dir, exist_ok=True)

    def _get_file_path(self, name: str) -> str:
        """Get the file path for an AppImage.

        Args:
            name: The name of the AppImage

        Returns:
            The full file path
        """
        return os.path.join(self.storage_dir, f"{name}.json")

    def _save_to_file(self, app_image: AppImage) -> None:
        """Save an AppImage to a file.

        Args:
            app_image: The AppImage to save
        """
        file_path = self._get_file_path(app_image.name)

        # Convert to dict for serialization
        data_dict = {
            "data": asdict(app_image.data),
            "last_updated": app_image.last_updated.isoformat()
            if app_image.last_updated
            else None,
        }

        with open(file_path, "w") as f:
            json.dump(data_dict, f, indent=2)

    def _load_from_file(self, file_path: str) -> AppImage:
        """Load an AppImage from a file.

        Args:
            file_path: Path to the file to load

        Returns:
            The loaded AppImage
        """
        with open(file_path, "r") as f:
            data_dict = json.load(f)

        # Convert back to AppImage
        app_data = AppImageData(**data_dict["data"])
        last_updated = (
            datetime.fromisoformat(data_dict["last_updated"])
            if data_dict["last_updated"]
            else None
        )

        return AppImage(data=app_data, last_updated=last_updated)

    def add(self, app_image: AppImage) -> None:
        """Add an AppImage to the repository.

        Args:
            app_image: The AppImage to store
        """
        file_path = self._get_file_path(app_image.name)
        if os.path.exists(file_path):
            raise KeyError(f"AppImage with name '{app_image.name}' already exists")

        self._save_to_file(app_image)

    def update(self, app_image: AppImage) -> None:
        """Update an existing AppImage in the repository.

        Args:
            app_image: The AppImage with updated data
        """
        file_path = self._get_file_path(app_image.name)
        if not os.path.exists(file_path):
            raise KeyError(f"AppImage with name '{app_image.name}' not found")

        # Update last_updated timestamp
        app_image.last_updated = datetime.now()

        # Save updated AppImage
        self._save_to_file(app_image)

    def remove(self, name: str) -> None:
        """Remove an AppImage from the repository.

        Args:
            name: The name of the AppImage to remove
        """
        file_path = self._get_file_path(name)
        if not os.path.exists(file_path):
            raise KeyError(f"AppImage with name '{name}' not found")

        os.remove(file_path)

    def get_by_name(self, name: str) -> Optional[AppImage]:
        """Get an AppImage by its name.

        Args:
            name: The name of the AppImage to retrieve

        Returns:
            The AppImage if found, None otherwise
        """
        file_path = self._get_file_path(name)
        if not os.path.exists(file_path):
            return None

        return self._load_from_file(file_path)

    def get_all(self) -> List[AppImage]:
        """Get all AppImages in the repository.

        Returns:
            A list of all AppImages
        """
        app_images = []

        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                file_path = os.path.join(self.storage_dir, filename)
                app_images.append(self._load_from_file(file_path))

        return app_images

    def find_by_display_name(self, display_name: str) -> List[AppImage]:
        """Find AppImages by display name.

        Args:
            display_name: The display name to search for

        Returns:
            A list of matching AppImages
        """
        return [app for app in self.get_all() if app.display_name == display_name]

    def find_by_version(self, version: str) -> List[AppImage]:
        """Find AppImages by version.

        Args:
            version: The version to search for

        Returns:
            A list of matching AppImages
        """
        return [app for app in self.get_all() if app.version == version]

    def count(self) -> int:
        """Count the number of AppImages in the repository.

        Returns:
            The number of AppImages
        """
        return len([f for f in os.listdir(self.storage_dir) if f.endswith(".json")])

    def clear(self) -> None:
        """Remove all AppImages from the repository."""
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                os.remove(os.path.join(self.storage_dir, filename))


# SQLite repository implementation
class SQLiteAppImageRepository:
    """SQLite implementation of AppImageRepository.

    This 'Concrete Repository' implements the AppImageRepository interface
    using a SQLite database for storage. This demonstrates how the Repository
    Pattern can use relational databases while keeping the domain code
    database-agnostic.
    """

    def __init__(self, db_path: str):
        """Initialize with the database file path.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path

        # Initialize database and tables
        self._init_db()

    def _init_db(self):
        """Initialize the database schema."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create AppImages table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_images (
                name TEXT PRIMARY KEY,
                arch_keyword TEXT NOT NULL,
                download_url TEXT NOT NULL,
                sha_download_url TEXT NOT NULL,
                version TEXT NOT NULL,
                display_name TEXT NOT NULL,
                sha_file_name TEXT NOT NULL,
                owner TEXT,
                repo TEXT,
                last_updated TEXT
            )
        """)

        conn.commit()
        conn.close()

    def _app_image_from_row(self, row) -> AppImage:
        """Create an AppImage from a database row.

        Args:
            row: Database row tuple

        Returns:
            An AppImage object
        """
        (
            name,
            arch_keyword,
            download_url,
            sha_download_url,
            version,
            display_name,
            sha_file_name,
            owner,
            repo,
            last_updated_str,
        ) = row

        app_data = AppImageData(
            name=name,
            arch_keyword=arch_keyword,
            download_url=download_url,
            sha_download_url=sha_download_url,
            version=version,
            display_name=display_name,
            sha_file_name=sha_file_name,
            owner=owner or "",
            repo=repo or "",
        )

        last_updated = (
            datetime.fromisoformat(last_updated_str) if last_updated_str else None
        )

        return AppImage(data=app_data, last_updated=last_updated)

    def add(self, app_image: AppImage) -> None:
        """Add an AppImage to the repository.

        Args:
            app_image: The AppImage to store
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Check if already exists
            cursor.execute(
                "SELECT name FROM app_images WHERE name = ?", (app_image.name,)
            )
            if cursor.fetchone():
                raise KeyError(f"AppImage with name '{app_image.name}' already exists")

            # Add new AppImage
            cursor.execute(
                """
                INSERT INTO app_images
                (name, arch_keyword, download_url, sha_download_url, version,
                 display_name, sha_file_name, owner, repo, last_updated)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    app_image.name,
                    app_image.data.arch_keyword,
                    app_image.data.download_url,
                    app_image.data.sha_download_url,
                    app_image.data.version,
                    app_image.data.display_name,
                    app_image.data.sha_file_name,
                    app_image.data.owner,
                    app_image.data.repo,
                    app_image.last_updated.isoformat()
                    if app_image.last_updated
                    else None,
                ),
            )

            conn.commit()
        finally:
            conn.close()

    def update(self, app_image: AppImage) -> None:
        """Update an existing AppImage in the repository.

        Args:
            app_image: The AppImage with updated data
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Check if exists
            cursor.execute(
                "SELECT name FROM app_images WHERE name = ?", (app_image.name,)
            )
            if not cursor.fetchone():
                raise KeyError(f"AppImage with name '{app_image.name}' not found")

            # Update last_updated timestamp
            last_updated = datetime.now()

            # Update AppImage
            cursor.execute(
                """
                UPDATE app_images
                SET arch_keyword = ?, download_url = ?, sha_download_url = ?,
                    version = ?, display_name = ?, sha_file_name = ?,
                    owner = ?, repo = ?, last_updated = ?
                WHERE name = ?
            """,
                (
                    app_image.data.arch_keyword,
                    app_image.data.download_url,
                    app_image.data.sha_download_url,
                    app_image.data.version,
                    app_image.data.display_name,
                    app_image.data.sha_file_name,
                    app_image.data.owner,
                    app_image.data.repo,
                    last_updated.isoformat(),
                    app_image.name,
                ),
            )

            conn.commit()
        finally:
            conn.close()

    def remove(self, name: str) -> None:
        """Remove an AppImage from the repository.

        Args:
            name: The name of the AppImage to remove
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Check if exists
            cursor.execute("SELECT name FROM app_images WHERE name = ?", (name,))
            if not cursor.fetchone():
                raise KeyError(f"AppImage with name '{name}' not found")

            # Remove AppImage
            cursor.execute("DELETE FROM app_images WHERE name = ?", (name,))

            conn.commit()
        finally:
            conn.close()

    def get_by_name(self, name: str) -> Optional[AppImage]:
        """Get an AppImage by its name.

        Args:
            name: The name of the AppImage to retrieve

        Returns:
            The AppImage if found, None otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM app_images WHERE name = ?", (name,))
            row = cursor.fetchone()

            if not row:
                return None

            return self._app_image_from_row(row)
        finally:
            conn.close()

    def get_all(self) -> List[AppImage]:
        """Get all AppImages in the repository.

        Returns:
            A list of all AppImages
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM app_images")
            rows = cursor.fetchall()

            return [self._app_image_from_row(row) for row in rows]
        finally:
            conn.close()

    def find_by_display_name(self, display_name: str) -> List[AppImage]:
        """Find AppImages by display name.

        Args:
            display_name: The display name to search for

        Returns:
            A list of matching AppImages
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM app_images WHERE display_name = ?", (display_name,)
            )
            rows = cursor.fetchall()

            return [self._app_image_from_row(row) for row in rows]
        finally:
            conn.close()

    def find_by_version(self, version: str) -> List[AppImage]:
        """Find AppImages by version.

        Args:
            version: The version to search for

        Returns:
            A list of matching AppImages
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM app_images WHERE version = ?", (version,))
            rows = cursor.fetchall()

            return [self._app_image_from_row(row) for row in rows]
        finally:
            conn.close()

    def count(self) -> int:
        """Count the number of AppImages in the repository.

        Returns:
            The number of AppImages
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT COUNT(*) FROM app_images")
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def clear(self) -> None:
        """Remove all AppImages from the repository."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM app_images")
            conn.commit()
        finally:
            conn.close()


# Application service that uses repositories
class AppImageService:
    """Service that uses repositories to manage AppImages - Client of the Repository Pattern.

    This class demonstrates how the domain code uses repositories without knowing
    the specific storage implementation. It shows the benefits of the Repository
    Pattern in creating a clean separation between domain logic and data access.

    In an actual application, this service would contain business logic that
    operates on AppImages, using the repository for persistence.
    """

    def __init__(self, repository: Any):  # Using Any for typing simplicity
        """Initialize with a repository.

        Args:
            repository: Any class implementing AppImageRepository protocol
        """
        self.repository = repository

    def add_app_image(self, data: AppImageData) -> AppImage:
        """Add a new AppImage.

        Args:
            data: The AppImage data

        Returns:
            The created AppImage
        """
        # Create the domain entity
        app_image = AppImage(data=data)

        # Store it using the repository
        self.repository.add(app_image)

        return app_image

    def update_app_image(
        self, name: str, new_version: str, new_download_url: str
    ) -> Optional[AppImage]:
        """Update an existing AppImage.

        Args:
            name: Name of the AppImage to update
            new_version: New version
            new_download_url: New download URL

        Returns:
            The updated AppImage or None if not found
        """
        # Get the existing AppImage
        app_image = self.repository.get_by_name(name)
        if not app_image:
            return None

        # Update the domain entity
        app_image.data.version = new_version
        app_image.data.download_url = new_download_url

        # Update in the repository
        self.repository.update(app_image)

        return app_image

    def find_outdated_app_images(self, current_version: str) -> List[AppImage]:
        """Find AppImages with versions older than the given version.

        This demonstrates a domain service method that uses the repository
        to implement business logic.

        Args:
            current_version: Version to compare against

        Returns:
            List of outdated AppImages
        """
        # Fetch all AppImages using the repository
        all_app_images = self.repository.get_all()

        # Apply domain logic to filter outdated ones
        # In a real implementation, this might use semantic versioning comparison
        outdated = [app for app in all_app_images if app.version < current_version]

        return outdated

    def get_app_image_statistics(self) -> Dict[str, Any]:
        """Get statistics about stored AppImages.

        This demonstrates complex domain operations using repository methods.

        Returns:
            Dictionary of statistics
        """
        all_app_images = self.repository.get_all()

        # Assuming a real implementation would have more complex logic
        versions = {}
        for app in all_app_images:
            if app.version in versions:
                versions[app.version] += 1
            else:
                versions[app.version] = 1

        return {
            "total_count": len(all_app_images),
            "version_distribution": versions,
            "average_name_length": sum(len(app.name) for app in all_app_images)
            / max(1, len(all_app_images)),
        }

    def change_repository(self, repository: Any) -> None:
        """Change the underlying repository implementation.

        This demonstrates how the Repository Pattern allows switching
        storage mechanisms at runtime.

        Args:
            repository: The new repository to use
        """
        self.repository = repository
        print(f"Repository changed to: {repository.__class__.__name__}")


def main():
    """Example of the Repository Design Pattern in action.

    This demonstrates:
    1. Creating different repository implementations
    2. Using domain objects with repositories
    3. Switching between storage mechanisms
    4. Keeping domain code unaware of storage details

    The Repository pattern provides a clean abstraction over data access.
    """
    print("\n=== REPOSITORY PATTERN DEMONSTRATION ===\n")

    # Create sample AppImageData
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

    gitlab_data = AppImageData(
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

    # 1. Create repositories
    print("1. Creating different repository implementations...")
    in_memory_repo = InMemoryAppImageRepository()
    file_repo = FileAppImageRepository("./tmp/appimages")
    sqlite_repo = SQLiteAppImageRepository("./tmp/appimages.db")

    # 2. Create service with in-memory repository
    print("\n2. Creating service with in-memory repository...")
    service = AppImageService(in_memory_repo)

    # 3. Add AppImages using the service
    print("\n3. Adding AppImages using the service...")
    github_app = service.add_app_image(github_data)
    gitlab_app = service.add_app_image(gitlab_data)

    print(f"Added {github_app.name} and {gitlab_app.name} to repository")
    print(f"Repository now contains {service.repository.count()} AppImages")

    # 4. Update an AppImage
    print("\n4. Updating an AppImage...")
    updated_app = service.update_app_image(
        name="github-app",
        new_version="1.1",
        new_download_url="https://github.com/owner/repo/releases/download/v1.1/app.AppImage",
    )

    if updated_app:
        print(f"Updated {updated_app.name} to version {updated_app.version}")

    # 5. Find outdated AppImages
    print("\n5. Finding outdated AppImages...")
    outdated = service.find_outdated_app_images("2.0")
    print(f"Found {len(outdated)} outdated AppImages:")
    for app in outdated:
        print(f"  - {app.name} (version {app.version})")

    # 6. Switch to file repository
    print("\n6. Switching to file repository...")
    service.change_repository(file_repo)

    # Add the same AppImages to the file repository
    print("Adding AppImages to file repository...")
    service.add_app_image(github_data)
    service.add_app_image(gitlab_data)

    apps = service.repository.get_all()
    print(f"File repository contains {len(apps)} AppImages:")
    for app in apps:
        print(f"  - {app.name} (version {app.data.version})")

    # 7. Switch to SQLite repository
    print("\n7. Switching to SQLite repository...")
    service.change_repository(sqlite_repo)

    # Add the same AppImages to the SQLite repository
    print("Adding AppImages to SQLite repository...")
    service.add_app_image(github_data)
    service.add_app_image(gitlab_data)

    # 8. Get statistics
    print("\n8. Getting AppImage statistics...")
    stats = service.get_app_image_statistics()
    print(f"Statistics from SQLite repository: {stats}")

    print("\n=== REPOSITORY PATTERN BENEFITS ===")
    print("* Separation of domain logic from data access mechanism")
    print("* Ability to switch storage implementations transparently")
    print("* Improved testability through repository abstraction")
    print("* Centralized data access logic in repository classes")

    print("\n=== END OF REPOSITORY PATTERN DEMONSTRATION ===\n")


if __name__ == "__main__":
    main()
