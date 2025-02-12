# from hello.py import hello function
from hello import hello


def test_default():     
    assert hello() == "hello, world"

def test_argument():
    #assert hello("David") == "hello, David"
    for name in ["Hermione", "Harry" , "Ron"]:
        assert hello(name) == f"hello, {name}"

def test_argument2():
    assert hello("David") == "hello, David"

# Run the test
