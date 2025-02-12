# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map() function to square each number in the list
squares = map(lambda x: x**2, numbers)

# Print the squared numbers
print(list(squares))


# Another example 

# Define a list of words
words = ["apple", "banana", "cherry", "date"]

# Use the map() function to get the length of each word
lengths = map(len, words)

# Print the lengths of each word
print(list(lengths))
