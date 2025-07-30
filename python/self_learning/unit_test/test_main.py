from main import is_sister_older_than_brother


def test_is_sister_older_than_brother():
    assert is_sister_older_than_brother() == False, (
        "Sister should not be older than brother"
    )
