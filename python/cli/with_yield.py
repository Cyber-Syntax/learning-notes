import pytest


class MyContext:
    def __enter__(self):
        print("ENTER context: setup")
        return "resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT context: cleanup")


@pytest.fixture
def my_fixture():
    print("Fixture start")
    with MyContext() as resource:
        print("Fixture: inside with, before yield")
        yield resource
        print("Fixture: inside with, after yield (runs after test)")

    print("Fixture: after with (runs after with block exits)")


def test_using_fixture(my_fixture):
    print("Test: got", my_fixture)
    print("Test: doing work")


# -s: Shortcut for --capture=no
# OUTPUT via `uv run pytest -s with_yield.py`
# with_yield.py Fixture start
# ENTER context: setup
# Fixture: inside with, before yield
# Test: got resource
# Test: doing work
# .Fixture: inside with, after yield (runs after test)
# EXIT context: cleanup
# Fixture: after with (runs after with block exits)
