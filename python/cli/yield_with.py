"""Understanding `with` + `yield` in context managers (no pytest).

Key Concepts:
1. `@contextmanager` turns a generator function into a context manager.
2. `yield` splits the function into:
   - **Setup** (code BEFORE yield) → runs when entering `with`.
   - **Teardown** (code AFTER yield) → runs when exiting `with`.
3. The value after `as` in `with` gets the yielded value.
4. `try/finally` ensures teardown runs **even if an exception occurs**.
"""

from contextlib import contextmanager

# Global variable we'll temporarily modify (like your REAL_DIRS).
CURRENT_DIR = "/home/user"


# ---------------------------------------------------------------------------
# THE CONTEXT MANAGER (with yield)
# ---------------------------------------------------------------------------
@contextmanager
def temporary_dir(new_dir):
    """Temporarily replace CURRENT_DIR with new_dir for a `with` block.

    Execution Flow:
    1. [SETUP]  Code before `yield` runs (entering `with`).
    2. [BODY]   The `with` block runs (we `yield` control here).
    3. [TEARDOWN] Code after `yield` runs (exiting `with`).
    """
    global CURRENT_DIR

    # --- [SETUP] Runs ONCE when entering `with` ---
    original_dir = CURRENT_DIR  # Save original.
    CURRENT_DIR = new_dir  # Replace global.
    print(f"[SETUP] CURRENT_DIR = {CURRENT_DIR}")

    try:
        # --- [YIELD] Pause here and give control to `with` block ---
        # The value after `as` in `with` gets this:
        #   with temporary_dir("/mock") as dir:  # dir = "/mock"
        yield new_dir

    finally:
        # --- [TEARDOWN] Runs ONCE when exiting `with` (even on exception) ---
        CURRENT_DIR = original_dir
        print(f"[TEARDOWN] CURRENT_DIR restored to {CURRENT_DIR}")


# ---------------------------------------------------------------------------
# DEMONSTRATION
# ---------------------------------------------------------------------------
print("=" * 60)
print("EXAMPLE 1: Normal usage (no exception)")
print("=" * 60)
print(f"Before: CURRENT_DIR = {CURRENT_DIR}")

with temporary_dir("/mock/dir") as dir:
    # This is the BODY of the `with` block.
    print(f"Inside with: CURRENT_DIR = {CURRENT_DIR}")
    print(f"Yielded value (dir) = {dir}")

print(f"After: CURRENT_DIR = {CURRENT_DIR}")

# ============================================================
# EXAMPLE 1: Normal usage (no exception)
# ============================================================
# Before: CURRENT_DIR = /home/user
# [SETUP] CURRENT_DIR = /mock/dir
# Inside with: CURRENT_DIR = /mock/dir
# Yielded value (dir) = /mock/dir
# [TEARDOWN] CURRENT_DIR restored to /home/user
# After: CURRENT_DIR = /home/user

# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXAMPLE 2: With exception (teardown STILL runs)")
print("=" * 60)
try:
    with temporary_dir("/error/dir") as dir:
        print(f"Inside with: CURRENT_DIR = {CURRENT_DIR}")
        raise ValueError("Simulated error!")
except ValueError:
    print("Exception caught in main code.")

print(f"After exception: CURRENT_DIR = {CURRENT_DIR}  # Restored!")

# ============================================================
# EXAMPLE 2: With exception (teardown STILL runs)
# ============================================================
# [SETUP] CURRENT_DIR = /error/dir
# Inside with: CURRENT_DIR = /error/dir
# [TEARDOWN] CURRENT_DIR restored to /home/user
# Exception caught in main code.
# After exception: CURRENT_DIR = /home/user  # Restored!


class ManualTemporaryDir:
    """Same logic, but using __enter__/__exit__ instead of @contextmanager."""

    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.original_dir = None

    def __enter__(self):
        """Runs when entering `with` (like code before yield)."""
        global CURRENT_DIR
        self.original_dir = CURRENT_DIR
        CURRENT_DIR = self.new_dir
        print(f"[MANUAL SETUP] CURRENT_DIR = {CURRENT_DIR}")
        return self.new_dir  # Value for `as` variable.

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Runs when exiting `with` (like code after yield)."""
        global CURRENT_DIR
        CURRENT_DIR = self.original_dir
        print(f"[MANUAL TEARDOWN] CURRENT_DIR restored to {CURRENT_DIR}")
        # Return False to propagate exceptions, True to suppress them.
        return False


# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EXAMPLE 3: Manual context manager (same behavior)")
print("=" * 60)

print(f"Before: CURRENT_DIR = {CURRENT_DIR}")
with ManualTemporaryDir("/manual/dir") as dir:
    print(f"Inside with: CURRENT_DIR = {CURRENT_DIR}")
print(f"After: CURRENT_DIR = {CURRENT_DIR}")


# ============================================================
# EXAMPLE 3: Manual context manager (same behavior)
# ============================================================
# Before: CURRENT_DIR = /home/user
# [MANUAL SETUP] CURRENT_DIR = /manual/dir
# Inside with: CURRENT_DIR = /manual/dir
# [MANUAL TEARDOWN] CURRENT_DIR restored to /home/user
# After: CURRENT_DIR = /home/user
