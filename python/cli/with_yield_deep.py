"""
Example showing how `yield` works in pytest fixtures and context managers.

We simulate a `config.py` module that stores a global list of XDG directories.
The application calls `create_app_directories()` to make sure those directories
exist. In tests, we don't want to touch the real user directories, so we
temporarily replace them with temporary directories.
"""

import os
from contextlib import contextmanager
from pathlib import Path

import pytest

# ----------------------------------------------------------------------
# Simulated part of config.py
# ----------------------------------------------------------------------

# Real XDG directories that the application would normally use.
ORIGINAL_XDG_DIRS = [
    "/home/user/.config/myapp",
    "/home/user/.local/share/myapp",
]

# Global variable that the rest of the code uses.
# We keep a separate ORIGINAL_XDG_DIRS so we can restore later.
XDG_DIRS = ORIGINAL_XDG_DIRS.copy()


def create_app_directories():
    """
    Create the application's XDG directories if they don't exist.

    This is the function that, in real life, would be called at startup.
    It reads the global XDG_DIRS and creates each directory.
    """
    for directory in XDG_DIRS:
        os.makedirs(directory, exist_ok=True)


# ----------------------------------------------------------------------
# Context manager to temporarily patch the global directory list
# ----------------------------------------------------------------------


@contextmanager
def patch_xdg_dirs(temp_dirs):
    """
    Temporarily replace the global XDG_DIRS with `temp_dirs`.

    Args:
        temp_dirs (list of str): The directories to use instead of the real ones.

    Yields:
        list of str: The temporary directories (same as `temp_dirs`).
    """
    global XDG_DIRS

    # Save the current value so we can put it back later.
    original_dirs = XDG_DIRS

    # Replace the global with our mock directories.
    XDG_DIRS = temp_dirs
    print("[patch] Swapped XDG_DIRS ->", XDG_DIRS)

    try:
        # `yield` pauses the context manager here and gives control
        # to the code inside the `with` block.
        yield temp_dirs
    finally:
        # This code runs after the `with` block finishes, no matter what
        # (even if an exception occurred inside the `with` block).
        XDG_DIRS = original_dirs
        print("[patch] Restored XDG_DIRS ->", XDG_DIRS)


# ----------------------------------------------------------------------
# Pytest fixture that uses the context manager
# ----------------------------------------------------------------------


@pytest.fixture
def mock_xdg_dirs(tmp_path):
    """
    Provide temporary XDG directories during a test.

    This fixture:
      1. Creates two temporary directory paths inside pytest's `tmp_path`.
      2. Patches the global XDG_DIRS to point to those temporary directories.
      3. Yields the patched list to the test.
      4. After the test finishes, restores the original XDG_DIRS.

    Args:
        tmp_path: Built‑in pytest fixture (pathlib.Path) for temporary files.

    Yields:
        list of str: The temporary directories used during the test.
    """
    # Create mock directory paths. They don't exist yet – the test will
    # call `create_app_directories()` and actually create them.
    mock_dirs = [
        str(tmp_path / "config"),
        str(tmp_path / "local" / "share"),
    ]

    print("\nFixture: about to enter 'with' block")

    # The `with` block will set XDG_DIRS to mock_dirs and yield control.
    with patch_xdg_dirs(mock_dirs) as patched_dirs:
        print("Fixture: inside 'with', before yield (paused here)")

        # `yield` pauses the fixture and hands `patched_dirs` to the test.
        # The test runs now.
        yield patched_dirs

        # After the test finishes, execution resumes here.
        print("Fixture: inside 'with', after yield (test done, resuming)")

    # This line runs after the `with` block exits.
    # The context manager has already restored XDG_DIRS to the original.
    print("Fixture: after 'with' block (XDG_DIRS restored)")


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------


def test_create_dirs_uses_mock_locations(mock_xdg_dirs):
    """
    Test that the application creates directories in the mock locations.

    Args:
        mock_xdg_dirs: The fixture (list of str) with temporary dirs.
    """
    print("Test 1: started, XDG_DIRS =", XDG_DIRS)

    # The fixture yielded the patched dirs; we can also check the global.
    assert mock_xdg_dirs == XDG_DIRS

    # Simulate what the application does: create the directories.
    create_app_directories()

    # Verify that the directories were actually created in the mock locations.
    for directory in mock_xdg_dirs:
        assert Path(directory).exists(), f"Expected {directory} to be created"

    print("Test 1: passed - directories created in mock location")


def test_xdg_dirs_restored_after_fixture():
    """
    Test that after the fixture, the global XDG_DIRS is back to normal.
    """
    print("\nTest 2: started, XDG_DIRS =", XDG_DIRS)

    # The context manager's `finally` block restored the original list.
    assert XDG_DIRS == ORIGINAL_XDG_DIRS

    print("Test 2: passed - original XDG_DIRS restored")
