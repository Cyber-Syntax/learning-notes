# Define a lambda function that takes a single argument x and returns x^2
square = lambda x: x ** 2

# Use the lambda function
print(square(4))  # Output: 16

# Another example 

# List of items
items = [('apple', 5), ('banana', 2), ('orange', 3), ('mango', 1)]

# Use the lambda function as the key argument to the sorted() function
# This will sort the list of items in descending order by the second element of each tuple
# In this case, the second element of each tuple is the quantity of the item
sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

# Print the sorted list of items
print(sorted_items)  # Output: [('apple', 5), ('orange', 3), ('banana', 2), ('mango', 1)]



# Another example

# define a regular function using the def keyword
def sum(x, y):
    return x + y

# call the function and print the result
result = sum(3, 4)
print(result)  # prints 7

# define a lambda function that does the same thing
sum = lambda x, y: x + y

# call the function and print the result
result = sum(3, 4)
print(result)  # also prints 7

