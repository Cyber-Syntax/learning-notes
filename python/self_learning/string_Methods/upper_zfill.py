txt = "Hello my friends"

x = txt.upper()

print(x) 


# Import the string module
import string

# Define a function that takes a string as an argument and returns the uppercase version of the string
# with leading zeros added to reach a specified length
def add_leading_zeros(s, length):
  return s.upper().zfill(length)

# Test the function with some sample inputs
print(add_leading_zeros('abc', 5))  # Output: 00ABC
print(add_leading_zeros('123', 5))  # Output: 00123
print(add_leading_zeros('12345', 5))  # Output: 12345
