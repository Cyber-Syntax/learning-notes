# Create a tuple
t = (1, 2, 3, 2, 4, 2, 5)

# Use the count method to count the number of occurrences of a value in the tuple
num_twos = t.count(2)
print(num_twos)  # Output: 3

# Use the index method to find the first index of a value in the tuple
# This means tuple start counting with 0 on the "1".
first_index_of_two = t.index(2)
print(first_index_of_two)  # Output: 1

# You can also specify a start and end index to search within a slice of the tuple
second_index_of_two = t.index(2, 2, 4)
print(second_index_of_two)  # Output: 3
