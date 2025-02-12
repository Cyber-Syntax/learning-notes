# Check if a string starts with a specific substring

# Create a string
string = "This is a string"

# Check if the string starts with "This"
result = string.startswith("This")
print(f"startswith('This'): {result}")

# Check if the string starts with "that"
result = string.startswith("that")
print(f"startswith('that'): {result}")

# Output:
# startswith('This'): True
# startswith('that'): False


# ANother example 

# Check if a string starts with one of several substrings
string = "He is a string"

# Check if the string starts with "This", "That", or "The"
result = string.startswith(("This", "That", "The"))
print(f"startswith(('This', 'That', 'The')): {result}")

# Check if the string starts with "is" at index 2
result = string.startswith("is", 2)
print(f"startswith('is', 2): {result}")

# Check if the string from index 6 to the end starts with "string"
result = string.startswith("string", 6)
print(f"startswith('string', 6): {result}")

# Output:
# startswith(('This', 'That', 'The')): True
# startswith('is', 2): True
# startswith('string', 6): True

