string = "hello world"
print(string.index("world")) # Output: 6
print(string.index("world", 0, 5)) # Output: ValueError: substring not found

string = "hello123"
print(string.isalnum()) # Output: True
string = "hello 123"
print(string.isalnum()) # Output: False

string = "hello"
print(string.isalpha()) # Output: True
string = "hello123"
print(string.isalpha()) # Output: False

string = "123"
print(string.isdecimal()) # Output: True
string = "123.45"
print(string.isdecimal()) # Output: False

string = "123"
print(string.isdigit()) # Output: True
string = "123.45"
print(string.isdigit()) # Output: False

string = "hello"
print(string.isidentifier()) # Output: True
string = "123hello"
print(string.isidentifier()) # Output: False

string = "hello"
print(string.islower()) # Output: True
string = "Hello"
print(string.islower()) # Output: False

string = "123"
print(string.isnumeric()) # Output: True
string = "123.45"
print(string.isnumeric()) # Output: False

string = "hello world"
print(string.isprintable()) # Output: True
string = "hello\nworld"
print(string.isprintable()) # Output: False

string = "   "
print(string.isspace()) # Output: True
string = "hello world"
print(string.isspace()) # Output: False

# Define a string
string = "abc123"

# Check if all the characters in the string are alphanumeric
result = string.isalnum()
print(f"isalnum(): {result} (True if all characters are alphanumeric, False otherwise)")
print(f"Example of False: {'abc123!'.isalnum()}")

# Check if all the characters in the string are alphabetic
result = string.isalpha()
print(f"isalpha(): {result} (True if all characters are alphabetic, False otherwise)")
print(f"Example of False: {'abc123'.isalpha()}")

# Check if all the characters in the string are ASCII characters
result = string.isascii()
print(f"isascii(): {result} (True if all characters are ASCII, False otherwise)")
print(f"Example of False: {'abc123€'.isascii()}")

# Check if all the characters in the string are decimal digits
result = string.isdecimal()
print(f"isdecimal(): {result} (True if all characters are decimal digits, False otherwise)")
print(f"Example of False: {'123.45'.isdecimal()}")

# Check if all the characters in the string are digits
result = string.isdigit()
print(f"isdigit(): {result} (True if all characters are digits, False otherwise)")
print(f"Example of False: {'123.45'.isdigit()}")

# Check if all the characters in the string are lowercase
result = string.islower()
print(f"islower(): {result} (True if all characters are lowercase, False otherwise)")
print(f"Example of False: {'ABC123'.islower()}")

# Check if all the characters in the string are numeric
result = string.isnumeric()
print(f"isnumeric(): {result} (True if all characters are numeric, False otherwise)")
print(f"Example of False: {'123.45'.isnumeric()}")

# Check if all the characters in the string are printable
result = string.isprintable()
print(f"isprintable(): {result} (True if all characters are printable, False otherwise)")
print(f"Example of False: {'123.45'.isprintable()}")

# Check if all the characters in the string are uppercase
result = string.isupper()
print(f"isupper(): {result} (True if all characters are uppercase, False otherwise)")
print(f"Example of False: {'abc123'.isupper()}")


