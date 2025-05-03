"""
Command Design Pattern Implementation - AppImage Manager Example

This module demonstrates the Command design pattern, which:
1. Encapsulates a request as an object
2. Allows parameterizing clients with different requests
3. Enables operations like queueing, logging, and undoing requests
4. Decouples the sender of a request from its receiver

Why use the Command Pattern?
---------------------------
- ABSTRACTION: Separates the request from its execution
- EXTENSIBILITY: Add new commands without changing existing code
- COMPOSABILITY: Commands can be combined into composite commands
- UNDO/REDO: Commands can support undoing operations
- QUEUING & LOGGING: Requests can be stored, logged, and processed later

Key Components in Command Pattern:
--------------------------------
1. Command: Interface declaring Execute() method
2. Concrete Command: Implements Execute() and links receivers with actions
3. Invoker: Asks commands to execute requests
4. Receiver: Knows how to perform the actual operations
5. Client: Creates commands and assigns them to invokers

Additional Design Principles Demonstrated:
----------------------------------------
- Single Responsibility: Each command encapsulates one action
- Open/Closed: New commands can be added without changing client code
- Dependency Inversion: High-level modules depend on command abstractions
- Interface Segregation: Clients only depend on what they use

This example shows how to implement the Command pattern for AppImage management,
enabling operations like downloading, installing, updating, and removing AppImages
with support for history, undo functionality, and command composition.
"""

import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List


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
    """AppImage class - The 'Receiver' in the Command Pattern.

    In the Command Pattern, receivers know how to perform operations.
    Commands will delegate the actual work to these objects.
    """

    data: AppImageData

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # For convenience, expose common fields directly
        self.name = self.data.name
        self.download_url = self.data.download_url
        self.version = self.data.version
        self.display_name = self.data.display_name

    def download(self, destination_dir: str) -> str:
        """Download the AppImage to the specified directory.

        Args:
            destination_dir: Directory to download the AppImage to

        Returns:
            str: The path to the downloaded file
        """
        print(f"Downloading {self.name} from {self.download_url}...")
        file_path = os.path.join(
            destination_dir, f"{self.name}-{self.version}.AppImage"
        )

        # Simulate download
        time.sleep(0.2)

        print(f"Downloaded to {file_path}")
        return file_path

    def install(self, file_path: str) -> bool:
        """Install the AppImage.

        Args:
            file_path: Path to the downloaded AppImage file

        Returns:
            bool: True if installation succeeded
        """
        print(f"Installing {self.name} from {file_path}...")

        # Simulate installation
        time.sleep(0.2)

        print(f"Installation of {self.name} completed")
        return True

    def update(self, destination_dir: str, new_version: str, new_url: str) -> str:
        """Update the AppImage to a new version.

        Args:
            destination_dir: Directory to download the update to
            new_version: The new version
            new_url: URL for the new version

        Returns:
            str: The path to the updated file
        """
        old_version = self.version
        old_url = self.download_url

        print(f"Updating {self.name} from version {old_version} to {new_version}...")

        # Update AppImage data
        self.data.version = new_version
        self.data.download_url = new_url
        self.version = new_version
        self.download_url = new_url

        # Download the updated version
        file_path = self.download(destination_dir)

        # Return old values for potential undo
        return file_path, old_version, old_url

    def remove(self, file_path: str) -> bool:
        """Remove the AppImage.

        Args:
            file_path: Path to the AppImage file to remove

        Returns:
            bool: True if removal succeeded
        """
        print(f"Removing {self.name} from {file_path}...")

        # Simulate removal
        time.sleep(0.2)

        print(f"Removal of {self.name} completed")
        return True


# The Command interface
class Command(ABC):
    """Command interface - This is the 'Command' in the Command Pattern.

    In the Command Pattern, this defines the interface that all commands
    must implement. The core methods are execute() and undo(), allowing
    commands to be executed and reversed.

    Commands encapsulate all the information needed to perform an action,
    including the receiver, method to call, and parameters.
    """

    @abstractmethod
    def execute(self) -> Any:
        """Execute the command.

        Returns:
            Any: Command-specific result
        """
        pass

    @abstractmethod
    def undo(self) -> bool:
        """Undo the command.

        Returns:
            bool: True if undo was successful
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Get a human-readable description of the command.

        Returns:
            str: Command description
        """
        pass


# Concrete Command implementations
class DownloadCommand(Command):
    """Downloads an AppImage - This is a 'Concrete Command'.

    In the Command Pattern, concrete commands implement the Command interface
    and encapsulate a specific operation on a specific receiver.

    This command encapsulates all the information needed to download an AppImage:
    - The receiver (AppImage) to operate on
    - The parameters needed (destination directory)
    - Logic for undoing the operation (deleting the downloaded file)
    """

    def __init__(self, app_image: AppImage, destination_dir: str):
        """Initialize with AppImage and destination directory.

        Args:
            app_image: The AppImage to download
            destination_dir: Directory to download to
        """
        self.app_image = app_image
        self.destination_dir = destination_dir
        self.downloaded_path = None  # Filled after execution

    def execute(self) -> str:
        """Execute the download.

        Returns:
            str: Path to the downloaded file
        """
        self.downloaded_path = self.app_image.download(self.destination_dir)
        return self.downloaded_path

    def undo(self) -> bool:
        """Undo the download by deleting the file.

        Returns:
            bool: True if undo was successful
        """
        if not self.downloaded_path:
            print(f"Cannot undo download of {self.app_image.name}: No download path")
            return False

        print(f"Undoing download of {self.app_image.name}...")
        # In a real implementation, this would delete the file
        print(f"Deleted {self.downloaded_path}")
        return True

    @property
    def description(self) -> str:
        """Get a description of the command.

        Returns:
            str: Command description
        """
        return f"Download {self.app_image.name} version {self.app_image.version}"


class InstallCommand(Command):
    """Installs an AppImage - Another 'Concrete Command'.

    This command encapsulates all the information needed to install an AppImage:
    - The receiver (AppImage) to operate on
    - The parameters needed (file path)
    - Logic for undoing the operation (uninstalling)
    """

    def __init__(self, app_image: AppImage, file_path: str):
        """Initialize with AppImage and file path.

        Args:
            app_image: The AppImage to install
            file_path: Path to the AppImage file
        """
        self.app_image = app_image
        self.file_path = file_path
        self.installed = False

    def execute(self) -> bool:
        """Execute the installation.

        Returns:
            bool: True if installation succeeded
        """
        result = self.app_image.install(self.file_path)
        self.installed = result
        return result

    def undo(self) -> bool:
        """Undo the installation by uninstalling.

        Returns:
            bool: True if undo was successful
        """
        if not self.installed:
            print(f"Cannot undo installation of {self.app_image.name}: Not installed")
            return False

        print(f"Undoing installation of {self.app_image.name}...")
        # In a real implementation, this would perform uninstallation
        print(f"Uninstalled {self.app_image.name}")
        self.installed = False
        return True

    @property
    def description(self) -> str:
        """Get a description of the command.

        Returns:
            str: Command description
        """
        return f"Install {self.app_image.name} version {self.app_image.version}"


class UpdateCommand(Command):
    """Updates an AppImage - Another 'Concrete Command'.

    This command encapsulates all the information needed to update an AppImage:
    - The receiver (AppImage) to operate on
    - The parameters needed (destination directory, new version, new URL)
    - Logic for undoing the operation (reverting to previous version)

    This demonstrates how commands can store state for undo operations.
    """

    def __init__(
        self, app_image: AppImage, destination_dir: str, new_version: str, new_url: str
    ):
        """Initialize with AppImage and update information.

        Args:
            app_image: The AppImage to update
            destination_dir: Directory to download the update to
            new_version: The new version
            new_url: URL for the new version
        """
        self.app_image = app_image
        self.destination_dir = destination_dir
        self.new_version = new_version
        self.new_url = new_url

        # These will be filled during execution
        self.old_version = None
        self.old_url = None
        self.updated_path = None

    def execute(self) -> str:
        """Execute the update.

        Returns:
            str: Path to the updated file
        """
        self.updated_path, self.old_version, self.old_url = self.app_image.update(
            self.destination_dir, self.new_version, self.new_url
        )
        return self.updated_path

    def undo(self) -> bool:
        """Undo the update by reverting to the previous version.

        Returns:
            bool: True if undo was successful
        """
        if not self.old_version or not self.old_url:
            print(
                f"Cannot undo update of {self.app_image.name}: No previous version info"
            )
            return False

        print(f"Undoing update of {self.app_image.name}...")
        print(f"Reverting to version {self.old_version}")

        # Revert AppImage data
        self.app_image.data.version = self.old_version
        self.app_image.data.download_url = self.old_url
        self.app_image.version = self.old_version
        self.app_image.download_url = self.old_url

        return True

    @property
    def description(self) -> str:
        """Get a description of the command.

        Returns:
            str: Command description
        """
        return f"Update {self.app_image.name} from version {self.old_version or '?'} to {self.new_version}"


class RemoveCommand(Command):
    """Removes an AppImage - Another 'Concrete Command'.

    This command encapsulates the removal operation, with enough information
    stored to potentially undo it (though a real implementation would need
    more data to fully restore a removed AppImage).
    """

    def __init__(self, app_image: AppImage, file_path: str):
        """Initialize with AppImage and file path.

        Args:
            app_image: The AppImage to remove
            file_path: Path to the AppImage file
        """
        self.app_image = app_image
        self.file_path = file_path
        self.removed = False

    def execute(self) -> bool:
        """Execute the removal.

        Returns:
            bool: True if removal succeeded
        """
        result = self.app_image.remove(self.file_path)
        self.removed = result
        return result

    def undo(self) -> bool:
        """Undo the removal by restoring the file and data.

        Returns:
            bool: True if undo was successful
        """
        if not self.removed:
            print(f"Cannot undo removal of {self.app_image.name}: Not removed")
            return False

        print(f"Undoing removal of {self.app_image.name}...")
        # In a real implementation, this would restore the file from backup
        print(f"Restored {self.app_image.name} to {self.file_path}")
        self.removed = False
        return True

    @property
    def description(self) -> str:
        """Get a description of the command.

        Returns:
            str: Command description
        """
        return f"Remove {self.app_image.name} version {self.app_image.version}"


# Composite Command - combines multiple commands into one
class CompositeCommand(Command):
    """A command that executes multiple commands in sequence - A 'Macro Command'.

    In the Command Pattern, composite commands group multiple commands into one,
    following the Composite Pattern. This allows treating individual commands
    and sequences of commands uniformly.

    This demonstrates how commands can be combined into more complex operations,
    while maintaining the same interface.
    """

    def __init__(self, commands: List[Command], description: str):
        """Initialize with a list of commands.

        Args:
            commands: The commands to execute in sequence
            description: Human-readable description of the macro
        """
        self.commands = commands
        self._description = description
        self.executed_commands = []

    def execute(self) -> List[Any]:
        """Execute all commands in sequence.

        Returns:
            List[Any]: Results from all commands
        """
        results = []

        for command in self.commands:
            try:
                result = command.execute()
                results.append(result)
                self.executed_commands.append(command)
            except Exception as e:
                print(f"Error executing {command.description}: {e}")
                # Undo already executed commands
                self._undo_executed()
                raise

        return results

    def _undo_executed(self):
        """Undo all commands that were executed successfully."""
        for command in reversed(self.executed_commands):
            try:
                command.undo()
            except Exception as e:
                print(f"Error undoing {command.description}: {e}")

    def undo(self) -> bool:
        """Undo all commands in reverse order.

        Returns:
            bool: True if all undos were successful
        """
        if not self.executed_commands:
            print(f"Cannot undo {self._description}: No commands executed")
            return False

        success = True
        for command in reversed(self.executed_commands):
            try:
                if not command.undo():
                    success = False
            except Exception as e:
                print(f"Error undoing {command.description}: {e}")
                success = False

        self.executed_commands = []
        return success

    @property
    def description(self) -> str:
        """Get a description of the composite command.

        Returns:
            str: Command description
        """
        return self._description


# Command History - keeps track of executed commands
class CommandHistory:
    """Maintains a history of executed commands for undo operations.

    This class demonstrates how the Command Pattern enables features like
    command history, undo/redo functionality, and audit logs.

    By keeping a record of executed commands, the system can:
    - Track what operations have been performed
    - Undo operations in reverse order
    - Potentially persist operations for audit or recovery
    """

    def __init__(self):
        """Initialize an empty command history."""
        self.history: List[Command] = []
        self.undone: List[Command] = []  # For potential redo functionality

    def add(self, command: Command):
        """Add a command to the history after execution.

        Args:
            command: The command that was executed
        """
        self.history.append(command)
        self.undone = []  # Clear redo history

    def undo_last(self) -> bool:
        """Undo the last executed command.

        Returns:
            bool: True if undo was successful
        """
        if not self.history:
            print("Nothing to undo")
            return False

        command = self.history.pop()
        print(f"Undoing: {command.description}")

        success = command.undo()
        if success:
            self.undone.append(command)
        else:
            # If undo failed, put the command back in history
            self.history.append(command)

        return success

    def redo_last(self) -> Any:
        """Redo the last undone command.

        Returns:
            Any: Result of the redone command
        """
        if not self.undone:
            print("Nothing to redo")
            return None

        command = self.undone.pop()
        print(f"Redoing: {command.description}")

        result = command.execute()
        self.history.append(command)

        return result

    def clear(self):
        """Clear the command history."""
        self.history = []
        self.undone = []

    def print_history(self):
        """Print the command history."""
        print("\nCommand History:")
        if not self.history:
            print("  (empty)")
        else:
            for i, command in enumerate(self.history, 1):
                print(f"  {i}. {command.description}")


# Command Invoker - responsible for executing commands
class CommandInvoker:
    """Executes commands and manages history - This is the 'Invoker' in the Command Pattern.

    In the Command Pattern, the invoker is responsible for executing commands
    and can provide additional functionality like history tracking, scheduling,
    or queueing.

    This invoker demonstrates:
    - Command execution
    - History tracking
    - Undo/redo capabilities
    - Command logging

    By separating the invoker from both the commands and their receivers,
    the system achieves better decoupling and flexibility.
    """

    def __init__(self):
        """Initialize with an empty command history."""
        self.history = CommandHistory()
        self.commands_executed = 0

    def execute_command(self, command: Command) -> Any:
        """Execute a command and add it to the history.

        Args:
            command: The command to execute

        Returns:
            Any: The result of the command execution
        """
        print(f"Executing: {command.description}")
        result = command.execute()
        self.history.add(command)
        self.commands_executed += 1
        return result

    def undo_last(self) -> bool:
        """Undo the last executed command.

        Returns:
            bool: True if undo was successful
        """
        return self.history.undo_last()

    def redo_last(self) -> Any:
        """Redo the last undone command.

        Returns:
            Any: Result of the redone command
        """
        return self.history.redo_last()

    def print_history(self):
        """Print the command history."""
        self.history.print_history()

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about command execution.

        Returns:
            Dict[str, Any]: Execution statistics
        """
        return {
            "commands_executed": self.commands_executed,
            "history_size": len(self.history.history),
            "undone_size": len(self.history.undone),
        }


def main():
    """Example of the Command Design Pattern in action.

    This demonstrates:
    1. Creating and executing different commands
    2. Tracking command history
    3. Undoing and redoing commands
    4. Creating and using composite commands

    The Command pattern enables flexible operation handling with support
    for features like undo/redo, command history, and composite operations.
    """
    print("\n=== COMMAND PATTERN DEMONSTRATION ===\n")

    # Setup phase - create AppImages and invoker
    print("1. Creating AppImages and Command Invoker...")

    # Create AppImages (receivers)
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

    # Create Command Invoker
    invoker = CommandInvoker()
    download_dir = "/tmp/appimages"

    # 2. Create and execute individual commands
    print("\n2. Creating and executing individual commands...")

    # Create and execute DownloadCommand
    download_cmd = DownloadCommand(github_image, download_dir)
    file_path = invoker.execute_command(download_cmd)

    # Create and execute InstallCommand
    install_cmd = InstallCommand(github_image, file_path)
    invoker.execute_command(install_cmd)

    # Print command history
    invoker.print_history()

    # 3. Demonstrate undo capability
    print("\n3. Demonstrating undo capability...")
    invoker.undo_last()  # Undo the installation
    invoker.undo_last()  # Undo the download

    # 4. Demonstrate redo capability
    print("\n4. Demonstrating redo capability...")
    invoker.redo_last()  # Redo the download
    invoker.redo_last()  # Redo the installation

    # 5. Create and execute UpdateCommand
    print("\n5. Creating and executing UpdateCommand...")
    update_cmd = UpdateCommand(
        github_image,
        download_dir,
        "2.0",
        "https://github.com/owner/repo/releases/download/v2.0/app.AppImage",
    )
    invoker.execute_command(update_cmd)

    # 6. Create and execute CompositeCommand
    print("\n6. Creating and executing CompositeCommand...")

    # Create commands for the composite operation
    download_gitlab_cmd = DownloadCommand(gitlab_image, download_dir)
    install_gitlab_cmd = InstallCommand(
        gitlab_image,
        f"{download_dir}/{gitlab_image.name}-{gitlab_image.version}.AppImage",
    )

    # Create and execute composite command
    download_install_cmd = CompositeCommand(
        [download_gitlab_cmd, install_gitlab_cmd],
        f"Download and Install {gitlab_image.name}",
    )
    invoker.execute_command(download_install_cmd)

    # Print updated history
    invoker.print_history()

    # 7. Demonstrate undoing a composite command
    print("\n7. Demonstrating undoing a composite command...")
    invoker.undo_last()  # This will undo both commands in the composite

    # 8. Create and execute RemoveCommand
    print("\n8. Creating and executing RemoveCommand...")
    remove_cmd = RemoveCommand(github_image, file_path)
    invoker.execute_command(remove_cmd)

    # Final history and statistics
    print("\nFinal Command History and Statistics:")
    invoker.print_history()
    stats = invoker.get_stats()
    print(f"Command Statistics: {stats}")

    print("\n=== COMMAND PATTERN BENEFITS ===")
    print("* Encapsulate operations as objects for flexibility")
    print("* Support for undo/redo functionality")
    print("* Command history for auditing and recovery")
    print("* Parameterize objects with operations")
    print("* Support for composite commands and complex operations")

    print("\n=== END OF COMMAND PATTERN DEMONSTRATION ===\n")


if __name__ == "__main__":
    main()
