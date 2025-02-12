# Convert an integer to a string
my_int = 123
my_int_str = str(my_int)
print(my_int_str)

# Convert a string to an integer
my_str = "456"
my_str_int = int(my_str)
print(my_str_int)

# Determine the length of a string
my_string = "Hello, world!"
string_length = len(my_string)
print(string_length)

# Create a dictionary
my_dict = dict(key1=1, key2=2, key3=3)
print(my_dict)

# Print output to the console
print("Hello, world!")

# divmod can't be usable for floats
x = divmod(4, 2)
y = divmod(7.0, 2)
z = divmod(5.0, 2)

print(x)
print(y)
print(z)

# Define a list of fruits
fruits = ['apple', 'banana', 'mango', 'kiwi']

# Use the enumerate() function to iterate over the list
for index, fruit in enumerate(fruits):
    # Print the index and the element at that index
    print(index, fruit)


# Define a mathematical expression as a string
expression = "2 + 3 * 4"

# Evaluate the expression and print the result
result = eval(expression)
print(result)



