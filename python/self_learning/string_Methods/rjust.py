string = "Hello"
justified_string = string.rjust(10, "*")
print(justified_string)  # prints "****Hello"


# Print a table of information
name = "Alice"
age = 25
height = 5.5

print("Name".rjust(10), "Age".rjust(4), "Height".rjust(8))
print("-" * 26)
print(name.rjust(10), str(age).rjust(4), str(height).rjust(8))


justified_string = string.rjust(len(string) + 5, "*")
print(justified_string)  # prints "*****Hello"



string = "Hello"
justified_string = "{:>10}".format(string)
print(justified_string)  # prints "     Hello"


# Real world example:

# Print a table of information
names = ["Alice", "Bob sinclearedmaneable", "Charlie"]
ages = [25, 30, 35]
heights = [5.5, 6.0, 6.5]

# Find the maximum length of the strings in each column
name_width = max(len(name) for name in names)
age_width = max(len(str(age)) for age in ages)
height_width = max(len(str(height)) for height in heights)

# Print the header
print("Name".rjust(name_width), "Age".rjust(age_width), "Height".rjust(height_width))

# Print a line of dashes to separate the header from the rows
print("-" * (name_width + age_width + height_width))

# Print the rows
for name, age, height in zip(names, ages, heights):
    # Right-justify each string and print it
    print(name.rjust(name_width), str(age).rjust(age_width), str(height).rjust(height_width))


