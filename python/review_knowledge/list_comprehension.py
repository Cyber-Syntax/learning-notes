"""List comprehension notes.

Structure:
    [expression for item in iterable]

expression:
  what you want to produce.

    x * 2
    x.upper()
    len(word)

Item:
  variable used in the loop

    for x in numbers


Iterable:
    anything you can loop over

        list
        tuple
        string
        range
        dict
        set


List comprehensions are usually:
- Faster than normal loops
- More readable
- More pythonic
"""

# keep only even numbers
evens = [x for x in range(10) if x % 2 == 0]

print(evens)
# [0, 2, 4, 6, 8]

words = ["cat", "elephant", "dog", "tiger"]

# keep words longer than 3 character
long_words = [word for word in words if len(word) > 3]

print(long_words)
# ["elephant", "tiger"]


# [expression_if_true if condition else expression_if_false for item in iterable]

result = ["even" if x % 2 == 0 else "odd" for x in range(5)]

print(result)
# ['even', 'odd', 'even', 'odd', 'even']

matrix = [[1, 2], [3, 4], [5, 6]]

# flatten a matrix
flat = [num for row in matrix for num in row]

print(flat)
# [1, 2, 3, 4, 5, 6]

for row in matrix:
    for num in row:
        print(num)
# Output
# 1
# 2
# 3
# 4
# 5
# 6

flat = []
for row in matrix:
    for num in row:
        flat.append(num)

print(flat)
# [1, 2, 3, 4, 5, 6]

# convert to upper case
names = ["alice", "bob", "charlie"]

upper_names = [name.upper() for name in names]

print(upper_names)
# ['ALICE', 'BOB', 'CHARLIE']

# get character from string
chars = [c for c in "python"]

print(chars)
# alternative more easy
print(list("python"))
# ['p', 'y', 't', 'h', 'o', 'n']

# read file lines
with open("test.txt") as file:
    lines = [line.strip() for line in file]

print("test.txt file lines: ", lines)
# test.txt file lines:  ['1', 'alice', '2', 'bob', '3', '4']

# find common
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = [x for x in a if x in b]

print(common)
# [3, 4]


# transpose matrix
matrix2 = [[1, 2, 3], [4, 5, 6]]

transpose = [[row[i] for row in matrix2] for i in range(3)]

print(transpose)
# [[1, 4], [2, 5], [3, 6]]
