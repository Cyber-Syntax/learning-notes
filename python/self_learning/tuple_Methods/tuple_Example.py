# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Get the length of the tuple
length = len(my_tuple)
print(length)  # Output: 5

# Count the number of occurrences of a value in the tuple
count = my_tuple.count(3)
print(count)  # Output: 1

# Find the index of the first occurrence of a value in the tuple
index = my_tuple.index(4)
print(index)  # Output: 3

# Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)

# Repeat a tuple
tuple4 = tuple1 * 3
print(tuple4)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Access elements of the tuple using indexing
first_element = my_tuple[0]
print(first_element)  # Output: 1
