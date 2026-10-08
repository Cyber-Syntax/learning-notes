"""Demonstrates how `yield` works in context managers and pytest fixtures for mocking XDG directories.

This module teaches:
1. How `@contextmanager` uses `yield` to split **setup** (before) and **teardown** (after) code.
2. How pytest fixtures use `yield` to split **setup** (before) and **teardown** (after) code.
3. The difference between `yield` in a context manager vs. a pytest fixture.
4. How global state (like `REAL_DIRS`) can be temporarily replaced for testing.

Run with: `uv run pytest -s this_file.py`
"""

from contextlib import contextmanager

import pytest

# Global variable representing real XDG config directories.
# In real code, this might come from `os.environ` or a config module.
REAL_DIRS = ["/home/user/.config", "/home/user/.local/share"]


# ---------------------------------------------------------------------------
# PART 1: Context Manager (patch_dirs)
# ---------------------------------------------------------------------------
@contextmanager
def patch_dirs(mock_dirs):
    """Temporarily replaces `REAL_DIRS` with `mock_dirs` for the duration of a `with` block.

    This is a **context manager** created with `@contextmanager`.
    The `yield` statement splits the function into two parts:
      - **Before yield**: Setup code (runs when entering the `with` block).
      - **After yield**: Teardown code (runs when exiting the `with` block).

    Args:
        mock_dirs (list[str]): The mock directory paths to use during the test.

    Yields:
        list[str]: The `mock_dirs` value, assigned to the variable after `as` in the
            `with` statement (e.g., `with patch_dirs(...) as dirs:`).

    Example:
        >>> with patch_dirs(["/mock/config"]) as dirs:
        ...     assert REAL_DIRS == ["/mock/config"]  # Mock is active here
        >>> assert REAL_DIRS == ["/home/user/.config", ...]  # Original restored
    """
    global REAL_DIRS

    # --- SETUP PHASE (runs ONCE when entering the `with` block) ---
    original_dirs = REAL_DIRS  # Save the original value to restore later.
    REAL_DIRS = mock_dirs  # Replace global with mock.
    print("[CONTEXT] SETUP: REAL_DIRS =", REAL_DIRS)

    try:
        # --- YIELD PHASE ---
        # The `yield` statement:
        #   1. **Pauses** this function here.
        #   2. **Returns** `mock_dirs` to the `with` block (as the `as` variable).
        #   3. The code **inside the `with` block** runs.
        #   4. When the `with` block finishes, execution **resumes HERE** (after yield).
        yield mock_dirs

    finally:
        # --- TEARDOWN PHASE (runs ONCE when exiting the `with` block) ---
        # This runs even if the `with` block raises an exception.
        REAL_DIRS = original_dirs
        print("[CONTEXT] TEARDOWN: REAL_DIRS restored to", REAL_DIRS)


# ---------------------------------------------------------------------------
# PART 2: Pytest Fixture (mocked_dirs_fixture)
# ---------------------------------------------------------------------------
@pytest.fixture
def mocked_dirs_fixture():
    """Pytest fixture that provides mock directories and uses `patch_dirs` internally.

    Pytest fixtures can use `yield` to split **setup** (before yield) and
    **teardown** (after yield) code. This is **similar but separate** from the
    `@contextmanager` `yield` above.

    Key differences:
      - Fixture `yield`: Pauses to **run the test function**, then resumes for teardown.
      - Context manager `yield`: Pauses to **run the `with` block**, then resumes for teardown.

    Yields:
        list[str]: The mock directories (passed to the test as its argument).

    Note:
        The fixture **wraps** the context manager (`patch_dirs`), so:
          1. Fixture setup runs.
          2. Context manager setup runs.
          3. Fixture yields to the test.
          4. Test runs.
          5. Fixture resumes (after its `yield`).
          6. Context manager teardown runs.
          7. Fixture teardown runs.
    """
    mock_dirs = ["/mock/config", "/mock/local/share"]

    print("\n[FIXTURE] Starting fixture setup...")

    # Use the context manager to handle the mocking of `REAL_DIRS`.
    with patch_dirs(mock_dirs) as dirs:
        print("[FIXTURE] Inside context manager, about to yield to test...")

        # --- FIXTURE YIELD ---
        # The `yield` here:
        #   1. **Pauses** the fixture function.
        #   2. **Passes** `dirs` to the test function as its `mocked_dirs_fixture` argument.
        #   3. The **test function** runs.
        #   4. When the test finishes, execution **resumes HERE** (after yield).
        yield dirs

        # This runs AFTER the test finishes, but BEFORE the context manager exits.
        print("[FIXTURE] Test finished, still inside context manager.")

    # This runs AFTER the context manager's teardown.
    print("[FIXTURE] Context manager exited, fixture teardown complete.")


# ---------------------------------------------------------------------------
# PART 3: Tests
# ---------------------------------------------------------------------------
def test_uses_mock_directories(mocked_dirs_fixture):
    """Test that `REAL_DIRS` is mocked during the test.

    Args:
        mocked_dirs_fixture (list[str]): Injected by pytest from the fixture's `yield`.
    """
    print("[TEST 1] Test started. REAL_DIRS =", REAL_DIRS)

    # Assert that the global was replaced by the mock.
    assert REAL_DIRS == ["/mock/config", "/mock/local/share"]

    # The fixture's `yield` value is also passed to the test.
    assert mocked_dirs_fixture == ["/mock/config", "/mock/local/share"]

    print("[TEST 1] Assertions passed!")


def test_sees_original_dirs_after_fixture():
    """Test that `REAL_DIRS` is restored to its original value after the fixture exits.

    This test runs **after** `test_uses_mock_directories`, so the fixture and
    context manager have already cleaned up.
    """
    print("\n[TEST 2] Test started. REAL_DIRS =", REAL_DIRS)

    # Assert that the original directories are back.
    assert REAL_DIRS == ["/home/user/.config", "/home/user/.local/share"]

    print("[TEST 2] Original directories confirmed!")


# OUTPUT: `uv run pytest -s with_yield_v2.py`
# with_yield_v2.py
# [FIXTURE] Starting fixture setup...
# [CONTEXT] SETUP: REAL_DIRS = ['/mock/config', '/mock/local/share']
# [FIXTURE] Inside context manager, about to yield to test...
# [TEST 1] Test started. REAL_DIRS = ['/mock/config', '/mock/local/share']
# [TEST 1] Assertions passed!
# .[FIXTURE] Test finished, still inside context manager.
# [CONTEXT] TEARDOWN: REAL_DIRS restored to ['/home/user/.config', '/home/user/.local/share'
# ]
# [FIXTURE] Context manager exited, fixture teardown complete.
#
# [TEST 2] Test started. REAL_DIRS = ['/home/user/.config', '/home/user/.local/share']
# [TEST 2] Original directories confirmed!
