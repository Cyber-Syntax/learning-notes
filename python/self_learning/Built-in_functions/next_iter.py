# Create an iterator object from a list
numbers = [1, 2, 3, 4, 5]
it = iter(numbers)

# Get the next item from the iterator
# The first time we call next(), it will return the
# first item from the list (1)
print(next(it))

# Get the next item from the iterator
# This time it will return the second item from the list (2)
print(next(it))

# Get the next item from the iterator
# This time it will return the third item from the list (3)
print(next(it))

# Get the next item from the iterator
# This time it will return the fourth item from the list (4)
print(next(it))

# Get the next item from the iterator
# This time it will return the fifth item from the list (5)
print(next(it))

# Since we have reached the end of the list, the next
# time we call next() it will raise a StopIteration exception
next(it)
