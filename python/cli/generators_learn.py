"""Yield example and generator vs. list comparison.

So every generator is an iterator, but not every iterator is a generator:
Iterable
│
├── list
├── tuple
├── string
├── dict
├── set
├── range
│
└── can give you an Iterator with iter()
                         │
                         ├── list_iterator
                         ├── range_iterator
                         ├── dict_keyiterator
                         ├── enumerate object
                         ├── zip object
                         ├── map object
                         ├── file object
                         └── generator

Note:
`range()` is NOT a generator.
It is a special iterable sequence type.

It is memory-efficient because it does not store every number in the
sequence. It stores the information needed to represent the range.

Unlike a generator, a range:
- supports indexing
- supports len()
- can be iterated over multiple times
- can calculate values without storing the whole sequence

So `range` and generators can both avoid creating a huge list,
but they achieve this in different ways.

More info check iterators.py

Generators vs List:
    - A generator produces values on demand, one at a time. It does not
        store all the values in memory at once like a list does. A generator
        keeps its execution state so it can resume where it paused.

    - A generator is fast to start because it does not need to compute and
        store all values before producing the first one. A list must create
        and store all its values before it is returned.

    - A generator object is single-use. Once it is exhausted, it cannot be
        restarted or iterated over again. Calling the generator function
        again creates a new generator object. A list is reusable and can be
        iterated over multiple times.

    - A generator does not provide indexing because generator objects do not
        implement the sequence/subscript protocol. With a list, we can use an
        index such as `numbers[2]` to get the third value.

    - A generator does not provide len() because generator objects do not
        implement the __len__() protocol. A list stores all its
        values, so `len(numbers)` works.

    - A generator can pause and resume execution at each `yield` statement.
        It maintains its state between yields, including local variables
        such as `i`. A list does not maintain execution state; it is simply
        a collection of already-created values.

    - A generator can represent an infinite sequence, such as `1, 2, 3, 4,
        ...`, because it produces values only when requested. A list must be
        finite because it needs to store all of its values in memory.

Generators are useful for streaming data, processing large files,
building pipelines, and working in memory-constrained environments.

Lists are useful for small datasets, random access, multiple iterations,
and caching values that we want to keep in memory.

The difference:
    List comprehension:

        [0, 1, 4, 9, 16]
        ↓
        all values already created and stored


    Generator expression:

        generator object
        ↓
        produce 0
        ↓
        produce 1
        ↓
        produce 4
        ↓
        produce 9
        ↓
        produce 16

Note:
    Python has several different kinds of objects that can produce values
    one at a time.

    Do not call all of them "generators".

    Generator:
    Created by a generator function (`yield`) or generator expression.

    Iterator:
    An object that produces values one at a time with `next()`.

    Iterable:
    An object that can provide an iterator through `iter()`.

    Some common examples:

    list          -> iterable, NOT an iterator
    tuple         -> iterable, NOT an iterator
    string        -> iterable, NOT an iterator
    dict          -> iterable, NOT an iterator
    set           -> iterable, NOT an iterator
    range         -> iterable, NOT a generator

    iter(list)    -> iterator
    enumerate()   -> iterator
    zip()         -> iterator
    map()         -> iterator
    filter()      -> iterator
    reversed()    -> iterator
    file object   -> iterator

    generator function
            │
            └── calling it ──> generator object
                                │
                                └── iterator
    generator expression -> generator

    itertools.count()   -> iterator
    itertools.repeat()  -> iterator
    itertools.cycle()   -> iterator
    itertools.islice()  -> iterator

"""


# Iterable:
# An object that we can get an iterator from.
#
# Examples:
# list, tuple, string, dict, set, range

numbers = [1, 2, 3]

# Iterator:
# An object that produces values one at a time with next().
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

print("\n")


def fibonacci():
    """Generate Fibonacci numbers using yield.

    Using a generator is better when we need to produce a very large
    number of values that would take too much memory to store in a list.
    For example, if storing all the values required 10 GB of RAM, a list
    could use that much memory, while the generator produces one value
    at a time and keeps its execution state.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # Infinite generator!


def count_up_to_list(n):
    """Create and return a list containing numbers from 1 to n."""
    result = []
    i = 1
    while i <= n:
        result.append(i)  # store all values in a list
        i += 1

    # return the full list at once
    return result


def count_up_to(n):
    """Yield numbers from 1 to n one at a time.

    Generator:
        A special type of iterator, usually created by:
        1. A function containing `yield`
        2. A generator expression `()`
    """
    i = 1
    while i <= n:
        yield i
        i += 1


# Call the function to create a generator object.
counter = count_up_to(5)
print(f"yield counter: {counter}")
# OUTPUT:
# yield counter: <generator object count_up_to at 0x7f95271459c0>

# NOTE:
# The for loop starts iterating over counter.
#
# On the first iteration:
# The generator starts executing count_up_to().
# i = 1 is set.
# The while condition (1 <= 5) is True.
# yield i produces 1, so num = 1 and print(num) outputs 1.
# The generator pauses at the yield statement.
#
# On the second iteration:
# The generator resumes exactly where it paused.
# i += 1 runs first, so i becomes 2.
# The while condition (2 <= 5) is True.
# yield i produces 2, so num = 2 and print(num) outputs 2.
# The generator pauses again at the yield statement.
#
# This continues until i becomes 6.
# The while condition (6 <= 5) is False, so the loop ends.
# The generator is exhausted, and the for loop stops automatically.
#
# Iterate over the generator.
for num in counter:
    print(f"yield: {num}")
# OUTPUT:
# yield: 1
# yield: 2
# yield: 3
# yield: 4
# yield: 5

numbers = count_up_to_list(5)
print(f"list numbers: {numbers}")
# OUTPUT:
# list numbers: [1, 2, 3, 4, 5]

# Iterate over the list.
for num in numbers:
    print(num)
# OUTPUT:
# 1
# 2
# 3
# 4
# 5

print("\n")
print("yield from example")


# NOTE:
# `yield from` lets a generator yield values from another iterable.
#
# It is useful when one generator needs to delegate producing values
# to another iterable or generator.


# yield from basically convenient way of this:
# def numbers():
#     for number in [1, 2, 3]:
#         yield number
#
def numbers():
    yield from [1, 2, 3]


for number in numbers():
    print(number)

# 1
# 2
# 3


print("\n")

# NOTE: You can also create a generator without defining a function with
# `yield`. A generator expression is a simple way to create a generator.
#
# List comprehension (eager)
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]
print(squares_list[0])  # 0
print("\n")

# Generator expression (lazy)
squares_gen = (x**2 for x in range(5))
print(squares_gen)  # <generator object <genexpr> at 0x7ff6fddea8e0>

# NOTE: `squares_gen` does not currently store [0, 1, 4, 9, 16].
# Instead, it represents a computation that can produce those values
# one at a time when we request them.
#
# Each `next()` asks the generator to produce the next value.
# After producing a value, the generator pauses and remembers its state.
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
print("\n")

# NOTE:
# The generator has now produced 0, 1, 4, and 9.
# The next value it can produce is 16.
#
# If we call `next()` again, the generator produces 16.
# After that, the generator is exhausted because there are no more values.
#
# print(next(squares_gen))  # 16

# NOTE:
# Generators do not support indexing or `len()` directly.
#
# print(len(squares_gen))  # TypeError: object of type 'generator' has no len()
# print(squares_gen[0])  # TypeError: 'generator' object is not subscriptable

# NOTE:
# If we need indexing, `len()`, or multiple iterations, we can convert
# the remaining values from the generator into a list.
#
# IMPORTANT: We have already consumed 0, 1, 4, and 9 above.
# Therefore, only 16 remains in the generator.
print("Converting generator to list as a workaround")
squares_gen_list = list(squares_gen)

print(squares_gen_list[0])  # 16
print(len(squares_gen_list))  # 1
print(squares_gen_list)  # [16]
