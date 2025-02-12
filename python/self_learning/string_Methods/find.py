string = "Hello, World!"

# Search for the substring "World"
index = string.find("World")

# Print the index where the substring was found
print(index)  # Output: 7

# Another example
word = 'geeks for geeks'
# Substring is searched in 'eks for geeks'
print(word.find('ge', 2)) # Output: 10


# Another example 


# Initialize a string
text = "Hello, World!"

# Search for the keyword "Python"
index = text.find("Python")

# If the keyword was found, highlight it in the text
# In this example, the find() method is used to search for the substrings 
# "World" and "Python" in the string variable. The first find() call returns 7,
#  because the substring "World" is found at index 7 in the string variable.
#  The second find() call returns -1, because the substring "Python" is not found 
# in the string variable.
if index != -1:
    text = text[:index] + "\033[1mPython\033[0m" + text[index+len("Python"):]

print(text)
# We can write more readable way:

# Initialize a string
text = "Hello, World!"

# Search for the substring "World"
index = text.find("World")

# Replace the substring "World" with the substring "Python" (in bold text)
text = text.replace("World", "\033[1mPython\033[0m", 1)

# Print the modified text
print(text)  # Output: "Hello, \033[1mPython\033[0m!"


# this is != -1 example:

string = "Hello, World!"

# Search for the substring "World"
index = string.find("World")

# If the substring was found, print a message
if index != -1:
    print("The substring was found at index {}".format(index))
else:
    print("The substring was not found in the string")

