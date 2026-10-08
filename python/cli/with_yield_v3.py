from contextlib import contextmanager

import pytest

# ==============================================================================
# 1. THE 'PRODUCTION' CODE
# Imagine this is your actual app code (e.g., a config.py module) managing
# Linux XDG paths for your CLI tool.
# ==============================================================================

XDG_DIRS = {
    "config": "/home/user/.config/myapp",
    "data": "/home/user/.local/share/myapp",
}


def create_xdg_dirs():
    """Creates the necessary XDG directories for the application.

    Returns:
        list: A list of the directory paths that were processed.
    """
    # In a real script, this would run: os.makedirs(path, exist_ok=True)
    return list(XDG_DIRS.values())


# ==============================================================================
# 2. THE TEST HELPERS (Context Managers & Fixtures)
# ==============================================================================


@contextmanager
def patch_xdg_dirs(mock_dirs):
    """Temporarily replaces the global XDG_DIRS with a mock dictionary.

    This context manager acts as a safe 'sandbox'. It changes the global state,
    yields control to whatever is inside the `with` block, and guarantees the
    original state is restored afterward, even if the code crashes.

    Args:
        mock_dirs (dict): The fake directories to use during testing.

    Yields:
        dict: The active (mocked) directory configuration.
    """
    global XDG_DIRS
    original_dirs = XDG_DIRS.copy()  # 1. Save the real-world state
    XDG_DIRS = mock_dirs  # 2. Set up the fake world

    try:
        # YIELD #1: Inside a context manager.
        # This hands execution control to the code block INSIDE the `with` statement.
        yield XDG_DIRS
    finally:
        # 3. Teardown: Restore the real world.
        # This ALWAYS runs when the `with` block ends, thanks to 'finally'.
        XDG_DIRS = original_dirs


@pytest.fixture
def isolated_xdg_environment():
    """Fixture to provide a safe, isolated filesystem for tests.

    This fixture opens our context manager and pauses execution so the test
    can run safely inside the mocked environment.

    Yields:
        dict: The mock directories safely injected into the app.
    """
    fake_xdg = {
        "config": "/tmp/mock_home/.config/myapp",
        "data": "/tmp/mock_home/.local/share/myapp",
    }

    # The `with` block opens our sandbox. Everything indented under here
    # is running with the fake XDG directories.
    with patch_xdg_dirs(fake_xdg) as active_mock_dirs:
        # YIELD #2: Inside a pytest fixture.
        # Think of this yield as a PAUSE BUTTON.
        # 1. Pytest stops running this fixture right here.
        # 2. It hands `active_mock_dirs` over to the test function.
        # 3. The test function runs completely.
        # 4. Once the test finishes, pytest unpauses this fixture.
        yield active_mock_dirs

        # The fixture resumes here after the test is completely done.
        # As soon as we exit this indentation level, the `with` block ends,
        # triggering the `finally` block in our context manager above.


# ==============================================================================
# 3. THE TESTS
# ==============================================================================


def test_create_xdg_dirs_uses_mock_paths(isolated_xdg_environment):
    """Tests that our directory creation logic uses the mocked paths.

    Args:
        isolated_xdg_environment (dict): Injected by pytest via the fixture's yield.
    """
    # When this test starts, the fixture is currently "paused" at its yield statement.
    # The global XDG_DIRS has been successfully swapped.

    created_paths = create_xdg_dirs()

    # Verify our app code saw the fake paths, not the real ones.
    assert "/tmp/mock_home/.config/myapp" in created_paths
    assert "/home/user/.config/myapp" not in created_paths

    # Verify the yielded value matches what we expect
    assert isolated_xdg_environment["config"] == "/tmp/mock_home/.config/myapp"

    # When this test finishes, pytest goes back to the fixture, unpauses it,
    # and the context manager cleans up the globals.


def test_global_state_is_restored_after_fixture():
    """Verifies that the previous test cleaned up after itself."""
    # This test DOES NOT request the fixture.
    # Therefore, XDG_DIRS should be entirely untouched.
    assert XDG_DIRS["config"] == "/home/user/.config/myapp"
