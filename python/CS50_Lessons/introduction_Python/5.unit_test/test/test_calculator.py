# import our function
from calculator import square
# import unit_test framework
import pytest

def main():
    test_positive()
    test_negative()
    test_zero()


# assert(ileri sürmek)
# Bu try assert ile unit test yapmak yerine pytest gibi frameworkler ile kodun çok aşırı uzun olmamasını sağlıyor.
def test_positive():
    try:
        assert square(2) == 4
    except AssertionError():
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError():
        print("3 squared was not 9")

def test_negative():
    assert square(-2) == 4

def test_zero():
    assert(0) == 0

# ? I think this is giving type error for user.
def test_str():
    with pytest.raises(TypeError):
        square("cat")

    # if square(2) != 4:
    #     print("There is a bug in your code. 2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")

if __name__ == "__main__":
    main()