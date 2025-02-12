# The slice() function takes three arguments: the start index, the stop index,
#  and the step size. In this case, the slice() function is called with the start
#  index 0 (which is the first character of the string) and the stop index 5 
# (which is the fifth character of the string), and the default step size of 1.

# Define a string to slice
string = "Hello, world!"

# Create a slice object that extracts the first five characters of the string
slice_obj = slice(0, 5)

# Use the slice object to extract the desired characters from the string
substring = string[slice_obj]

# Print the resulting substring
print(substring) # Prints 'Hello'


# Another example:


# Define a list of numbers to slice
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a slice object that extracts every other number from the list
slice_obj = slice(0, len(numbers), 1) 
# slice(0, len(numbers), 3)  = [0, 3, 6, 9]
# slice(0, len(numbers), 2)  = [0, 2, 4, 6, 8]

# Use the slice object to extract the desired numbers from the list
sublist = numbers[slice_obj]

# Print the resulting sublist
print(sublist) # Prints [0, 2, 4, 6, 8]
print(len(numbers))
