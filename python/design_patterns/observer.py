"""
Observer Design Pattern Implementation - AppImage Manager Example

This module demonstrates the Observer design pattern, which:
1. Defines a one-to-many dependency between objects
2. When the subject changes state, all dependents are notified automatically
3. Enables loose coupling between the subject and its observers

Why use the Observer Pattern?
---------------------------
- DECOUPLING: Subjects don't need to know about specific observers
- EXTENSIBILITY: New observers can be added without changing the subject
- BROADCAST COMMUNICATION: One update can notify multiple observers
- SEPARATION OF CONCERNS: Subject focuses on state, observers on reactions

Key Components in Observer Pattern:
---------------------------------
1. Subject: Maintains a list of observers and notifies them of state changes
2. Observer: Defines an interface for objects that should be notified of changes
3. Concrete Observer: Implements the Observer interface to respond to updates
4. Concrete Subject: Implements the Subject interface to notify observers

Additional Design Principles Demonstrated:
----------------------------------------
- Single Responsibility: Subject manages state, observers handle reactions
- Open/Closed Principle: New observers can be added without modifying subject
- Composition over Inheritance: Observable behavior is composed into subjects
- Dependency Inversion: High-level subjects depend on observer abstractions

This example shows how to implement the Observer pattern for an AppImage management
system, where various components need to be notified of changes to AppImages.
"""

import enum
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Protocol, Set


# We'll reuse the AppImageData class concept from factory.py
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


# Base AppImage class (simplified from factory.py)
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


# Event types for our observer pattern
class EventType(enum.Enum):
    """Types of events that can occur in the AppImage system."""

    APPIMAGE_ADDED = "appimage_added"
    APPIMAGE_UPDATED = "appimage_updated"
    APPIMAGE_REMOVED = "appimage_removed"
    DOWNLOAD_STARTED = "download_started"
    DOWNLOAD_PROGRESS = "download_progress"
    DOWNLOAD_COMPLETED = "download_completed"
    DOWNLOAD_FAILED = "download_failed"


@dataclass
class Event:
    """Event class to encapsulate information about an event.

    This class represents an event in the Observer pattern. It contains:
    - The type of event that occurred
    - The appimage that the event relates to (if applicable)
    - Any additional data associated with the event

    Events are passed to observers when notifying them of changes.
    """

    event_type: EventType
    appimage: Optional[AppImage] = None
    data: Dict[str, Any] = field(default_factory=dict)


class Observer(Protocol):
    """Observer interface using Protocol for structural typing.

    In the Observer pattern, this defines the interface that all
    concrete observers must implement. The update method is called
    by the subject when an event occurs.

    The Protocol approach allows for duck typing while maintaining
    type hints for better IDE support and code readability.
    """

    def update(self, event: Event) -> None:
        """Method called when subject state changes.

        Args:
            event: The event object containing information about what changed
        """
        ...


class Subject:
    """Subject base class for the Observer pattern.

    In the Observer pattern, the Subject maintains a list of observers
    and provides methods to register, unregister, and notify observers.

    This implementation uses a set for observers to prevent duplicates
    and provides type hints for better code quality.
    """

    def __init__(self):
        """Initialize with an empty set of observers."""
        self._observers: Set[Observer] = set()

    def register_observer(self, observer: Observer) -> None:
        """Add an observer to be notified of events.

        Args:
            observer: The observer to register
        """
        self._observers.add(observer)

    def unregister_observer(self, observer: Observer) -> None:
        """Remove an observer so it no longer receives notifications.

        Args:
            observer: The observer to unregister
        """
        self._observers.discard(observer)

    def notify_observers(self, event: Event) -> None:
        """Notify all registered observers of an event.

        This method is called by the concrete subject when a state
        change occurs that observers should be notified about.

        Args:
            event: The event object with information about the change
        """
        for observer in self._observers:
            observer.update(event)


# Concrete Observer implementations
class LoggingObserver:
    """Observer that logs all events.

    This concrete observer demonstrates how to implement the Observer
    interface to respond to events from the subject. It logs details
    about each event to the console.
    """

    def update(self, event: Event) -> None:
        """Log the event details.

        Args:
            event: The event object containing information about what changed
        """
        appimage_name = event.appimage.name if event.appimage else "N/A"
        print(f"LOG: {event.event_type.value} - AppImage: {appimage_name}")

        if event.data:
            print(f"     Additional data: {event.data}")


class NotificationObserver:
    """Observer that shows user notifications for important events.

    This concrete observer implements the Observer interface to show
    notifications to the user when certain events occur.
    """

    def update(self, event: Event) -> None:
        """Show a notification for important events.

        Args:
            event: The event object containing information about what changed
        """
        # In a real implementation, this would use the system's notification API
        if event.event_type in [
            EventType.APPIMAGE_UPDATED,
            EventType.DOWNLOAD_COMPLETED,
        ]:
            appimage_name = event.appimage.name if event.appimage else "Unknown"
            print(f"NOTIFICATION: {appimage_name} - {event.event_type.value}")


class SystemTrayObserver:
    """Observer that updates system tray icon status.

    This concrete observer implements the Observer interface to update
    the system tray icon based on the state of AppImages.
    """

    def __init__(self):
        """Initialize with empty counts."""
        self.download_count = 0
        self.update_available_count = 0

    def update(self, event: Event) -> None:
        """Update counters and refresh system tray icon.

        Args:
            event: The event object containing information about what changed
        """
        if event.event_type == EventType.DOWNLOAD_STARTED:
            self.download_count += 1
            self._refresh_icon()
        elif event.event_type == EventType.DOWNLOAD_COMPLETED:
            self.download_count = max(0, self.download_count - 1)
            self._refresh_icon()
        elif event.event_type == EventType.APPIMAGE_UPDATED:
            self.update_available_count -= 1
            self._refresh_icon()

    def _refresh_icon(self):
        """Refresh the system tray icon based on current state."""
        # In a real implementation, this would update an actual system tray icon
        status = []
        if self.download_count > 0:
            status.append(f"{self.download_count} downloads in progress")
        if self.update_available_count > 0:
            status.append(f"{self.update_available_count} updates available")

        if status:
            print(f"SYSTEM TRAY: {', '.join(status)}")
        else:
            print("SYSTEM TRAY: No active tasks")


# AppImageManager with Observer pattern
class AppImageManager(Subject):
    """AppImage manager that implements the Subject interface.

    This class demonstrates how the Observer pattern can be integrated
    with the existing AppImageManager from the factory pattern example.
    It extends the Subject class to inherit observer management functionality.

    This manager maintains a collection of AppImages and notifies observers
    when AppImages are added, updated, removed, or their download status changes.
    """

    def __init__(self):
        """Initialize with parent constructor and empty AppImage collection."""
        super().__init__()
        self.appimages: Dict[str, AppImage] = {}

    def add_appimage(self, appimage: AppImage) -> None:
        """Add an AppImage to the manager and notify observers.

        Args:
            appimage: The AppImage to add
        """
        is_update = appimage.name in self.appimages
        self.appimages[appimage.name] = appimage

        # Notify observers of the appropriate event
        if is_update:
            self.notify_observers(
                Event(event_type=EventType.APPIMAGE_UPDATED, appimage=appimage)
            )
        else:
            self.notify_observers(
                Event(event_type=EventType.APPIMAGE_ADDED, appimage=appimage)
            )

    def remove_appimage(self, name: str) -> None:
        """Remove an AppImage from the manager and notify observers.

        Args:
            name: The name of the AppImage to remove
        """
        if name in self.appimages:
            appimage = self.appimages[name]
            del self.appimages[name]

            # Notify observers
            self.notify_observers(
                Event(event_type=EventType.APPIMAGE_REMOVED, appimage=appimage)
            )

    def download_appimage(self, name: str) -> None:
        """Download an AppImage and notify observers of progress.

        This method simulates the download process for an AppImage,
        notifying observers at different stages of the process.

        Args:
            name: The name of the AppImage to download
        """
        if name not in self.appimages:
            print(f"Error: AppImage '{name}' not found")
            return

        appimage = self.appimages[name]

        # Notify download started
        self.notify_observers(
            Event(event_type=EventType.DOWNLOAD_STARTED, appimage=appimage)
        )

        # Simulate download progress
        for progress in [25, 50, 75, 100]:
            # In a real implementation, this would be async/threaded
            self.notify_observers(
                Event(
                    event_type=EventType.DOWNLOAD_PROGRESS,
                    appimage=appimage,
                    data={"progress": progress},
                )
            )

        # Notify download completed
        self.notify_observers(
            Event(event_type=EventType.DOWNLOAD_COMPLETED, appimage=appimage)
        )

        print(f"Download of {appimage.name} completed")


def main():
    """Example of the Observer Design Pattern in action.

    This demonstrates:
    1. Creating a subject (AppImageManager)
    2. Creating and registering various observers
    3. Performing actions that trigger events
    4. Showing how different observers respond to the same events

    The Observer pattern enables a clean separation between the subject's
    state and the various components that need to react to state changes.
    """
    print("\n=== OBSERVER PATTERN DEMONSTRATION ===\n")

    # Create the subject (AppImageManager)
    print("1. Creating AppImageManager (Subject)...")
    manager = AppImageManager()

    # Create and register observers
    print("\n2. Creating and registering observers...")
    logger = LoggingObserver()
    notifier = NotificationObserver()
    tray_icon = SystemTrayObserver()

    manager.register_observer(logger)
    manager.register_observer(notifier)
    manager.register_observer(tray_icon)

    print(
        "   * Registered LoggingObserver, NotificationObserver, and SystemTrayObserver"
    )

    # Create some AppImages
    print("\n3. Creating and adding AppImages...")

    # Create Github AppImage
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

    # Create GitLab AppImage
    gitlab_data = AppImageData(
        name="gitlab-app",
        arch_keyword="x86_64",
        download_url="https://gitlab.com/owner/repo/-/releases/v1.0/app.AppImage",
        sha_download_url="https://gitlab.com/owner/repo/-/releases/v1.0/app.AppImage.sha256",
        version="1.0",
        display_name="GitLab App",
        sha_file_name="app.AppImage.sha256",
        owner="owner",
        repo="repo",
    )
    gitlab_image = AppImage(data=gitlab_data)

    # Adding AppImages - this will trigger APPIMAGE_ADDED events
    print("\n4. Adding AppImages (triggers APPIMAGE_ADDED events)...")
    manager.add_appimage(github_image)
    manager.add_appimage(gitlab_image)

    # Download an AppImage - triggers download events
    print("\n5. Downloading an AppImage (triggers download events)...")
    manager.download_appimage("github-app")

    # Update an AppImage - triggers APPIMAGE_UPDATED event
    print("\n6. Updating an AppImage (triggers APPIMAGE_UPDATED event)...")
    # Create new version of GitHub AppImage
    updated_github_data = AppImageData(
        name="github-app",
        arch_keyword="x86_64",
        download_url="https://github.com/owner/repo/releases/download/v2.0/app.AppImage",
        sha_download_url="https://github.com/owner/repo/releases/download/v2.0/app.AppImage.sha256",
        version="2.0",  # Updated version
        display_name="GitHub App",
        sha_file_name="app.AppImage.sha256",
        owner="owner",
        repo="repo",
    )
    updated_github_image = AppImage(data=updated_github_data)
    manager.add_appimage(updated_github_image)

    # Remove an AppImage - triggers APPIMAGE_REMOVED event
    print("\n7. Removing an AppImage (triggers APPIMAGE_REMOVED event)...")
    manager.remove_appimage("gitlab-app")

    # Unregister an observer
    print("\n8. Unregistering NotificationObserver...")
    manager.unregister_observer(notifier)

    # Download again to show difference with fewer observers
    print("\n9. Downloading again with fewer observers...")
    manager.download_appimage("github-app")

    print("\n=== END OF OBSERVER PATTERN DEMONSTRATION ===\n")


if __name__ == "__main__":
    main()
