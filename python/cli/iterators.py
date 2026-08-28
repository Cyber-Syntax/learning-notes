"""Iterator examples."""

print("range() example")

# NOTE:
# `range()` is NOT a generator.
# It is a special iterable sequence type.
#
# It is memory-efficient because it does not store every number in the
# sequence. It stores the information needed to represent the range.
#
# Unlike a generator, a range:
# - supports indexing
# - supports len()
# - can be iterated over multiple times
# - can calculate values without storing the whole sequence
#
# So `range` and generators can both avoid creating a huge list,
# but they achieve this in different ways.

my_range = range(4)

print("1. Iterating the first time:")
for i in my_range:
    print(i)
# OUTPUT
# 0
# 1
# 2
# 3

print(
    "\n2. Iterating a second time (Generators would be 'exhausted' here, but range allows this):"
)
for i in my_range:
    print(i)
# OUTPUT
# 0
# 1
# 2
# 3

print("\n3. Showcasing len():")
print(len(my_range))
# OUTPUT
# 4

print("\n4. Showcasing indexing:")
print(my_range[2])  # Gets the item at index 2
# OUTPUT
# 2

print(my_range[-1])  # Gets the last item
# OUTPUT
# 3

print("\n")
print("enumerate() example")

# NOTE:
# `enumerate()` returns an iterator, not a generator.
#
# It produces one `(index, value)` pair at a time.
# It does not need to create a complete list of pairs first.

names = ["Alice", "Bob", "Charlie"]

result = enumerate(names)

print(result)
# <enumerate object at ...>

print(type(result))
# <class 'enumerate'>

# The iterator remembers where it is:
print(next(result))  # (0, 'Alice')
print(next(result))  # (1, 'Bob')
print(next(result))  # (2, 'Charlie')


for index, name in enumerate(names):
    print(index, name)

# 0 Alice
# 1 Bob
# 2 Charlie

print("\n")
print("zip() example")

# NOTE:
# `zip()` returns an iterator.
# It combines values from multiple iterables one pair at a time.
#
# It does not first create something like:
#
# [
#     ("Alice", 20),
#     ("Bob", 25),
#     ("Charlie", 30),
# ]
#
# Instead, it produces each tuple when requested.

ages = [20, 25, 30]

pairs = zip(names, ages)

print(next(pairs))  # ('Alice', 20)
print(next(pairs))  # ('Bob', 25)

print("\n")
print("map() example")

# NOTE:
# `map()` returns an iterator.
# It applies a function to each value and produces the result one at a time.
#
# It does NOT immediately create:
#
# [2, 4, 6, 8]
#
# Instead, the values are calculated as we request them.

numbers = [1, 2, 3, 4]

doubled = map(lambda x: x * 2, numbers)

print(next(doubled))  # 2
print(next(doubled))  # 4

print("\n")
print("filter() example")

# NOTE:
# `filter()` returns an iterator.
# It checks values one at a time and produces only the values
# that satisfy the condition.
#
# It does not immediately create:
#
# [2, 4, 6]
#
# Instead, it finds and produces matching values as we request them.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(next(even_numbers))  # 2
print(next(even_numbers))  # 4

print("\n")
print("reversed() example")


# NOTE:
# `reversed()` returns an iterator for objects that support the
# required sequence protocol.
#
# It can produce values in reverse order without first creating
# another complete reversed list.

numbers = [1, 2, 3, 4]

reverse_numbers = reversed(numbers)

print(next(reverse_numbers))  # 4
print(next(reverse_numbers))  # 3


print("\n")
print("iter() example")


# NOTE:
# `iter()` gets an iterator from an iterable.
#
# A list is iterable, but it is not itself an iterator.
# `iter(numbers)` creates a list iterator that can produce the
# list's values one at a time.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30


print("\n")
print("dict example")

# NOTE:
# Dictionaries also produce iterators when you iterate over them.
# You can also explicitly get iterators for the keys, values, or items
person = {
    "name": "Alice",
    "age": 25,
}


keys = iter(person.keys())
values = iter(person.values())
items = iter(person.items())

print(next(keys))  # name
print(next(values))  # Alice
print(next(items))  # ('name', 'Alice')


# # NOTE:
# # A file object is an iterable and also provides iterator behavior.
# #
# # When we iterate over a file, Python gives us one line at a time
# # instead of requiring us to load the entire file into memory.
# #
# # This is one reason generators and iterators are useful for
# # processing large files.
# with open("large_file.txt") as file:
#     for line in file:
#         print(line)
#
#
# # You can also explicitly use next():
# with open("large_file.txt") as file:
#     print(next(file))
#     print(next(file))


# itertools — a huge collection of iterators
# The standard library's itertools module contains many tools specifically designed for iterator-based processing.

print("\n")
print("itertools library example")


# NOTE:
# `itertools.count()` returns an iterator that produces an infinite
# sequence of numbers.
#
# It behaves similarly to:
#
# def count_up():
#     i = 1
#     while True:
#         yield i
#         i += 1
#
# The important idea is that the values are produced one at a time.

from itertools import count, cycle, islice, repeat

numbers = count(1)

print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3

print("\n")


# repeats 3 time
values = repeat("hello", 3)

print(next(values))  # hello
print(next(values))  # hello
print(next(values))  # hello


# it can also repeat forever
values = repeat("hello")

print(next(values))  # hello
print(next(values))  # hello
print(next(values))  # hello


# Repeats an iterable forever:
colors = cycle(["red", "green", "blue"])

print(next(colors))  # red
print(next(colors))  # green
print(next(colors))  # blue
print(next(colors))  # red
print(next(colors))  # green


# # NOTE:
# # `cycle()` returns an iterator that repeats the input sequence forever.
# #
# # Be careful with infinite iterators like this.
# # A normal `for` loop will never finish unless you stop it yourself.
#
#
# values = cycle([1, 2, 3])
#
# for value in values:
#     print(value)
#     # This would continue forever.


# This is useful for taking only part of an iterator.
first_five = islice(numbers, 5)

print(list(first_five))
# [4, 5, 6, 7, 8]


print(next(numbers))  # 9
print(next(numbers))  # 10

# The iterator maintains its state.
remaining = islice(numbers, 3)

print(list(remaining))
# [11, 12, 13]
