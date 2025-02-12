# Create a string with multiple lines of text
text = """
This is line 1.
This is line 2.
This is line 3.
"""

# Split the string into a list of lines using the splitlines() function
lines = text.splitlines()
print(f"splitlines(): {lines}")

# Split the string into a list of words using the split() function
words = text.split()
print(f"split(): {words}")

# Split the string into a list of words using the rsplit() function
right_words = text.rsplit()
print(f"rsplit(): {right_words}")

# Output:
# splitlines(): ['', 'This is line 1.', 'This is line 2.', 'This is line 3.', '']
# split(): ['This', 'is', 'line', '1.', 'This', 'is', 'line', '2.', 'This', 'is', 'line', '3.']
# rsplit(): ['This', 'is', 'line', '3.', 'This', 'is', 'line', '2.', 'This', 'is', 'line', '1.']


# Another example



# Split a string into a list of substrings using the specified delimiter

# Create a string with multiple words separated by a space
string = "This is a string with multiple words"

# Use the split() function to split the string into a list of substrings
# using a space as the delimiter
words = string.split(' ')
print(f"split(): {words}")

# Use the rsplit() function to split the string into a list of substrings
# starting from the right side of the string and using a space as the delimiter
right_words = string.rsplit(' ')
print(f"rsplit(): {right_words}")

# Use the splitlines() function to split the string into a list of lines
# using the newline character as the delimiter
lines = string.splitlines()
print(f"splitlines(): {lines}")

# Output:
# split(): ['This', 'is', 'a', 'string', 'with', 'multiple', 'words']
# rsplit(): ['This', 'is', 'a', 'string', 'with', 'multiple', 'words']
# splitlines(): ['This is a string with multiple words']


# Anotherexample


# Split a string with comma-separated values
csv = "value1,value2,value3"
values = csv.split(',', maxsplit=1)
print(f"split(): {values}")

# Use the rsplit() function to split the string into a list of substrings
# starting from the right side of the string and using a comma as the delimiter
right_values = csv.rsplit(',', maxsplit=1)
print(f"rsplit(): {right_values}")

# Split a string with tab-separated values
tsv = "value1\tvalue2\tvalue3"
values = tsv.split('\t')
print(f"split(): {values}")

# Output:
# split(): ['value1', 'value2,value3']
# rsplit(): ['value1,value2', 'value3']
# split(): ['value1', 'value2', 'value3']
