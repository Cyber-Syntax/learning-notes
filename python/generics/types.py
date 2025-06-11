# Python 3.12+ syntax with new generic class declaration


class Box[T]:
    def __init__(self, content: T) -> None:
        self.content = content

    def get_content(self) -> T:
        return self.content


# Usage with type annotations
int_box: Box[int] = Box(42)
str_box: Box[str] = Box("Hello")

# assigning the content to variables with type annotations
int_value: int = int_box.get_content()
str_value: str = str_box.get_content()

# assigning the content of str_box to an int variable
# WARN: Static type checkers like Mypy would flag this as an error,
# but the Python interpreter would not.
# NOTE: However, this practice is discouraged because it can lead to runtime errors
int_value_str_box: int = str_box.get_content()  # Type checker will complain

# printing the contents
print(int_box.get_content())  # Output: 42
print(str_box.get_content())  # Output: Hello
print(int_value)  # Output: 42
print(f"int_value_str_box: {int_value_str_box}")  # Output: Hello (unsafe)
print(f"str_value: {str_value}")  # Output: Hello


# Old version of the code that uses generics in Python
# from typing import TypeVar, Generic
#
# # Define a type variable
# T = TypeVar("T")
#
#
# # Create a generic class
# class Box(Generic[T]):
#     def __init__(self, content: T) -> None:
#         self.content = content
#
#     def get_content(self) -> T:
#         return self.content
#
#
# # Usage with type annotations
# int_box: Box[int] = Box(42)
# str_box: Box[str] = Box("Hello")
#
# # assigning the content to variables with type annotations
# int_value: int = int_box.get_content()
# str_value: str = str_box.get_content()
#
# # assigning the content of str_box to an int variable
# # WARN: Static type checkers like Mypy would flag this as an error,
# # but the Python interpreter would not.
# # NOTE: However, this practice is discouraged because it can lead to runtime errors
# int_value_str_box: int = str_box.get_content()
#
# # printing the contents
# print(int_box.get_content())  # Output: 42
# print(str_box.get_content())  # Output: Hello
# print(int_value)  # Output: 42
# print(f"int_value_str_box: {int_value_str_box}")  # Output: Hello
# print(f"str_value: {str_value}")  # Output: Hello
