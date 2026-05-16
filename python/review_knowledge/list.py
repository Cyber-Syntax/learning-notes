"""Learning lists.

Lists are mutable sequences, typically used to store collections
of homogeneous items (where the precise degree of similarity
will vary by application).

Resource:
https://docs.python.org/3/library/stdtypes.html#lists
"""

from functools import cmp_to_key

SEPARATOR = "--" * 30


def section(title: str):
    """Print a reusable separator section."""
    print(f"\n{SEPARATOR}")
    print(title)
    print(SEPARATOR)


# ======================================================================
# class list(iterable=(), /)
#
# Lists may be constructed in several ways:
#
#   * Using a pair of square brackets to denote the empty list: []
#   * Using square brackets, separating items with commas: [a], [a, b, c]
#   * Using a list comprehension: [x for x in iterable]
#   * Using the type constructor: list() or list(iterable)
#
# The constructor builds a list whose items are the same and in
# the same order as iterable’s items.
#
# iterable may be either:
#   * a sequence
#   * a container that supports iteration
#   * an iterator object
#
# If iterable is already a list, a copy is made and returned,
# similar to iterable[:].
#
# Examples:
#   * list("abc") -> ['a', 'b', 'c']
#   * list((1, 2, 3)) -> [1, 2, 3]
#   * list() -> []
# ======================================================================


def list_creation_examples():
    # Empty list using square brackets
    empty = []
    empty.append(5)

    print("Empty list using []:", empty)
    # Empty list using []: [5]

    # Lists with items
    numbers = [1, 2, 3]
    fruits = ["apple", "banana", "orange"]

    print("\nUsing square brackets with items:")
    print("numbers:", numbers)
    print("fruits:", fruits)
    # Using square brackets with items:
    # numbers: [1, 2, 3]
    # fruits: ['apple', 'banana', 'orange']

    # List comprehension
    # new_list = [expression for item in iterable]
    #
    # x * x == x ** 2 in Python
    # "*" multiples, while "**" means exponentiation
    squares = [x * x for x in range(5)]
    squares_2 = [x**2 for x in range(5)]

    print("\nList comprehension [x for x in iterable]:")
    print("squares:", squares)
    print("x**2:", squares_2)
    # List comprehension [x for x in iterable]:
    # squares: [0, 1, 4, 9, 16]
    # x**2: [0, 1, 4, 9, 16]

    # Without list comprehension:
    squares_list = []
    for x in range(5):
        squares_list.append(x * x)

    print("squares_list via for loop:", squares_list)

    # Constructor example
    # list() -> constructor is a built-in python function
    empty_constructor = list()
    chars = list("abc")
    tuple_numbers = list((1, 2, 3))

    print("\nUsing list() constructor:")
    print("list() -> creates an empty list", empty_constructor)
    print('list("abc") - string is iterable character by character', chars)
    print(
        "list((1,2,3)) -> a tuple is iterable element by element",
        tuple_numbers,
    )

    # Using list() constructor:
    # list() -> creates an empty list []
    # list("abc") - string is iterable character by character ['a', 'b', 'c']
    # list((1,2,3)) -> a tuple is iterable element by element [1, 2, 3]

    # Constructor keeps same order
    data = ("A", "B", "C")
    copied_from_tuple = list(data)
    # Different iterable types
    sequence = list("hello")

    print("\nConstructor preserves iterable order:")
    print("Original tuple:", data)
    print("Copied list:", copied_from_tuple)
    # Constructor preserves iterable order:
    # Original tuple: ('A', 'B', 'C')
    # Copied list: ['A', 'B', 'C']

    # Sets are unordered collections, so order may differ
    container = list({"apple", "banana", "orange"})

    iterator = list(iter([10, 20, 30]))

    print("\nDifferent iterable types:")
    print('Sequence list("hello") ->', sequence)
    print("Container list(set) ->", container)
    print("Iterator list(iter(...)) ->", iterator)
    # Different iterable types:
    # Sequence list("hello") -> ['h', 'e', 'l', 'l', 'o']
    # Container list(set) -> ['apple', 'orange', 'banana']
    # Iterator list(iter(...)) -> [10, 20, 30]

    # Copying a list
    original = [1, 2, 3]
    copied_list = list(original)
    copied_list.append(4)

    print("\nCopying an existing list:")
    print("Original:", original)
    print("Copied + modified:", copied_list)
    # Copying an existing list:
    # Original: [1, 2, 3]
    # Copied + modified: [1, 2, 3, 4]


section("List creation examples")
list_creation_examples()


# ============================================================================
# Many other operations also produce lists, including the sorted() built-in.
# ============================================================================


def sorted_builting_examples():
    numbers = [5, 2, 9, 1]

    # sorted() returns a NEW list
    sorted_numbers = sorted(numbers)

    print("Original numbers:", numbers)
    print("sorted(numbers):", sorted_numbers)
    # Original numbers: [5, 2, 9, 1]
    # sorted(numbers): [1, 2, 5, 9]

    # original list remains unchanged
    print("original list after sorted():", numbers)
    # original list after sorted(): [5, 2, 9, 1]


section("sorted() built-in examples")
sorted_builting_examples()


# ============================================================================
# Lists implement all common mutable sequence operations.
# ============================================================================


section("mutable sequence operations")


# Default argument values(list, dict, set, custom class instances)
# are created once, when the function is defined —
# not each time the function is called.
def add_item(item, items=[]):
    items.append(item)
    return items


print("When you use a mutable default argument:")
print(add_item("a"))
print(add_item("b"))
print(add_item("c"))
# Output:
# ['a']
# ['a', 'b']
# ['a', 'b', 'c']


# With this approach, the default argument(list) is created each time the function is called.
def add_item_ones(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(
    "\nWhen you use a mutable default argument with a conditional check to be able to reset the list:"
)
print(add_item_ones("a"))
print(add_item_ones("b"))
# ['a']
# ['b']


def mutable_operations():
    numbers = [1, 2, 3]

    print("\noriginal list:", numbers)
    # original list: [1, 2, 3]

    # Add item
    numbers.append(4)

    # remove item by value
    numbers.remove(2)

    # modify item by index
    numbers[0] = 100

    print("mutrable operations result:", numbers)
    # mutable operations result: [100, 3, 4]


mutable_operations()


# ============================================================================
# Lists also provide the following additional method:
#
#   sort(*, key=None, reverse=False)
#
# This method sorts the list in place, using only < comparisons
# between items.
#
# Exceptions are not suppressed. If any comparison operations fail,
# the entire sort operation will fail.
#
# sort() accepts keyword-only arguments:
#
#   * key
#   * reverse
#
# key:
#   Specifies a function of one argument used to extract
#   a comparison key from each list element.
#
# reverse:
#   If True, elements are sorted as if comparisons were reversed.
#
# sort() modifies the list in place and returns None.
# ============================================================================


def sort_examples():
    numbers = [4, 1, 3, 2]
    words = ["pear", "apple", "banana"]

    numbers.sort()
    words.sort()

    print("sort() in place numbers:", numbers)
    print("sort() using < comparisons between strings:", words)
    # sort() in place numbers: [1, 2, 3, 4]
    # sort() using < comparisons between strings: ['apple', 'banana', 'pear']

    # sort() returns None because it modifies the list directly
    result = numbers.sort()
    print("numbers.sort() return value:", result)
    # numbers.sort() return value: None

    # reverse=True
    reverse_numbers = [1, 4, 2, 3]
    reverse_numbers.sort(reverse=True)

    print("\nreverse=True example:")
    print("Descending order:", reverse_numbers)
    # reverse=True example:
    # Descending order: [4, 3, 2, 1]

    # key=None
    key_none_numbers = [9, 1, 5, 3]
    key_none_numbers.sort(key=None)

    print("\nkey=None example:")
    print("Sorted directly without custom key:", key_none_numbers)
    # key=None example:
    # Sorted directly without custom key: [1, 3, 5, 9]

    # key=str.lower
    mixed_case_words = ["Banana", "apple", "Orange"]
    mixed_case_words.sort(key=str.lower)

    print("\nkey=str.lower example:")
    print("Case-insensitive sort:", mixed_case_words)
    # key=str.lower example:
    # Case-insensitive sort: ['apple', 'Banana', 'Orange']

    # key=len
    length_words = ["watermelon", "kiwi", "apple"]
    length_words.sort(key=len)

    print("\nkey=len example:")
    print("Sorted by word length:", length_words)
    # key=len example:
    # Sorted by word length: ['kiwi', 'apple', 'watermelon']


section("sort() method examples")
sort_examples()

# ============================================================================
# The functools.cmp_to_key() utility converts an old-style cmp
# function into a key function.
# ============================================================================


def compare_lenght(a, b):
    """Compare strings by lenght."""
    return len(a) - len(b)


def cmp_to_key_example():
    words = ["pear", "apple", "kiwi"]
    words.sort(key=cmp_to_key(compare_lenght))
    print("cmp_to_key(compare_lenght):", words)
    # cmp_to_key(compare_lenght): ['pear', 'kiwi', 'apple']


section("cmp_to_key() examples")
cmp_to_key_example()


# ============================================================================
# sort() errors
#
# If comparison operations fail, sort() raises an exception.
# ============================================================================


def sort_error_example():
    mixed = [1, "apple", 3]

    try:
        mixed.sort()
    # TypeError already raised by sort() but here, we catch
    # it to handle the exception gracefully:
    except TypeError as error:
        print(f"TypeError while sorting mixed types: {error}")
        # TypeError while sorting mixed types:
        # '<' not supported between instances of 'str' and 'int'


section("sort() error example")
sort_error_example()

# ============================================================================
# sort() stability
#
# sort() is guaranteed to be stable.
#
# Stable sorting means:
# elements that compare equal keep their original relative order.
#
# This is useful for multi-pass sorting.
# ============================================================================


def get_score(student):
    """Alternative to lambda student: student[1]."""
    return student[1]


def get_item_priority(item):
    """Alternative to lambda item: item[1]."""
    return item[1]


def get_department(employee):
    """Alternative to lambda employee: employee[0]."""
    return employee[0]


def get_salary_grade(employee):
    """Alternative to lambda employee: employee[1]."""
    return employee[1]


def stable_sort_examples():
    students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 88),
        ("David", 95),
    ]
    # using named function instead of lambda
    # get_score() is a named function that returns the score of a student
    students.sort(key=get_score, reverse=True)
    print(f"\nstudents.sort() return value: \n{students}")
    # students.sort() return value:
    # [('David', 95), ('Bob', 92), ('Charlie', 88), ('Alice', 85)]

    # sort() still returns None
    stable = students.sort(key=get_score)

    print(f"\nstudents.sort() return value: \n{stable}")
    # students.sort() return value:
    # None

    # Relative order example
    items = [
        ("first", 1),
        ("second", 1),
        ("third", 2),
        ("fourth", 2),
    ]

    items.sort(key=get_item_priority)
    print(f"\nStable relative order: \n{items}")
    # [('first', 1), ('second', 1), ('third', 2), ('fourth', 2)]

    # Multi-pass sorting example
    employees = [
        ("IT", 3000, "alice"),
        ("HR", 2000, "bob"),
        ("IT", 1000, "charlie"),
        ("HR", 300, "david"),
    ]

    # First sort by salary grade (secondary key)
    #
    # get_salary_grade() is a named function that returns
    # the salary grade of an employee
    #
    # higher salary grades come first
    # if you want lower salary grades to come first,
    # set reverse=False
    employees.sort(key=get_salary_grade, reverse=True)

    # Then sort by department (primary key)
    # because sorting is stable, salary order inside
    # each department is preserved
    #
    # get_department() is a named function that returns
    # the department of an employee
    employees.sort(key=get_department)

    print(f"\nMulti-pass sorting example: \n{employees}")
    # [('HR', 2, 'bob'), ('HR', 3, 'david'), ('IT', 1, 'charlie'), ('IT', 3, 'alice')]


section("sort() stability examples")
stable_sort_examples()


# ============================================================================
# CPython implementation detail:
#
# While a list is being sorted, mutating or even inspecting
# the list is undefined behavior.
#
# CPython may raise ValueError if mutation is detected.
# ============================================================================


def mutating_during_sort():
    numbers = [3, 1, 2]

    try:

        def bad_key(x):
            # modifying the list while sorting is unsafe
            numbers.append(4)
            return x

        numbers.sort(key=bad_key)
    except ValueError as e:
        print(f"ValueError: list is being mutated during sort: {e}")
        # ValueError: list is being mutated during sort: list modified during sort


section("mutating_during_sort()")
mutating_during_sort()


# The sort() method is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).
def stable_sort():
    students = [("Alice", 50), ("Bob", 90), ("Charlie", 85)]
    students.sort(key=lambda s: s[1], reverse=True)
    # this gives None because sort() modifies the list in place
    # stable = students.sort(key=lambda s: s[1], reverse=True)
    stable = sorted(students, key=lambda s: s[1], reverse=True)
    print(students)
    print(stable)


stable_sort()


# TODO: write examples for thread-safety:
# https://docs.python.org/3/library/threadsafety.html#thread-safety-for-list-objects
# For detailed information on thread-safety guarantees for list objects, see Thread safety for list objects.

section("other old examples:")


def get_squares() -> list[int]:
    """
    Return squares of even numbers from 0-20,
    excluding numbers divisible by 3.
    """
    return [x**2 for x in range(21) if x % 2 == 0 and x % 3 != 0]


print(get_squares())
# [4, 16, 64, 100, 196, 256, 400]


# Reversing list
def reverse_list_1():
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for i in range(len(l2) - 1, -1, -1):  # range(start, stop, step)
        result.append(l2[i])
    return result


print(reverse_list_1())
# [9, 8, 7, 6, 5, 4, 3, 2, 1]


# more easy way with built-in
def reverse_list(items):
    """Return a reversed copy of the given iterable."""
    return list(reversed(items))


print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [9, 8, 7, 6, 5, 4, 3, 2, 1]


# Look list is sorted or not
def is_sorted_manual():
    l3 = [1, 2, 5, 4]
    print(l3)
    for i in range(len(l3) - 1):  # range(3) = [0, 1, 2]
        num = l3[i]
        next_num = l3[i + 1]
        if num > next_num:  # 1 > 2
            return False
    return True


print("Is it sorted?", is_sorted_manual())  # False


# another manual example with zip
def is_sorted_manual_2(numbers):
    """Check if a list is sorted in ascending order
    using manual comparison.
    """
    print(numbers)

    for current, next_value in zip(numbers, numbers[1:]):
        if current > next_value:
            return False

    return True


def is_sorted_manual_3():
    l5 = [1, 2, 3, 4]
    print(l5)
    return all(l5[i] <= l5[i + 1] for i in range(len(l5) - 1))


def is_sorted_pythonic(numbers):
    print(numbers)
    return all(
        current <= next_value
        for current, next_value in zip(numbers, numbers[1:])
    )


def is_sorted_builtin(numbers):
    print(numbers)
    return numbers == sorted(numbers)


print("Is it sorted?", is_sorted_manual_3())  # True

# Unsorted example
test1 = [1, 2, 5, 4]

print("Manual:", is_sorted_manual_2(test1))
print("Built-in:", is_sorted_builtin(test1))
print("Pythonic:", is_sorted_pythonic(test1))

# Sorted example
test2 = [1, 2, 3, 4]

print("Manual:", is_sorted_manual_2(test2))
print("Built-in:", is_sorted_builtin(test2))
print("Pythonic:", is_sorted_pythonic(test2))
