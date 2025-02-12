file_path = "C:/Users/user/Documents/report.pdf"

# Find the index of the last period in the file path
try:
    index = file_path.rindex(".")
except ValueError:
    print("File extension not found")
else:
    # Extract the file extension
    file_ext = file_path[index:]
    print(file_ext)  # ".pdf"

# Another example 

# Find the last occurrence of a substring in a string
string = "The quick brown fox jumps over the lazy dog."

# Use the rindex() method to search for the last occurrence of the substring "the"
try:
    index = string.rindex("the")
except ValueError:
    # If the substring is not found, print an error message
    print("Substring not found")
else:
    # If the substring is found, print the index
    print(index)  # 35

# Another example:

# Parse a CSV string and extract the last column as a float
csv_string = "1.2,2.3,3.4,4.5\n5.6,6.7,7.8,8.9"

# Find the index of the last comma(virgül) in the string
try:
    # Use the rindex() method to search for the last comma
    index = csv_string.rindex(",")
except ValueError:
    # If the comma is not found, print an error message
    print("Comma not found")
else:
    # If the comma is found, extract the last column and convert it to a float
    # Use the index returned by rindex() to extract the last column from the string
    last_column = csv_string[index+1:]
    # Use the strip() method to remove any leading or trailing whitespace from the string
    last_column = last_column.strip()
    # Use the float() function to convert the string to a float
    last_column_float = float(last_column)
    print(last_column_float)  # 8.9

# rindex vs index

string = "Hello, World!"

# Find the index of the substring "World"
index = string.index("World")
print(index)  # Output: 7

# Find the index of the last occurrence(olay) of the substring "l"
rindex = string.rindex("l")
print(rindex)  # Output: 9



string = "Hello, World!"

# Find the index of the first occurrence of "l" after index 5
index = string.index("o", 5)
print(index)  # Output: 9

# Find the index of the last occurrence of "l" before index 9
rindex = string.rindex("o", 0, 9)
print(rindex)  # Output: 2

# Note that both index and rindex are case sensitive, so "l" and "L" are considered different substrings.