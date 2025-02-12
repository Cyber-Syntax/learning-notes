# Initialize a string
string = "ThIs Is A sTrInG"

# Use the swapcase() method to convert the string to "tHiS iS a StRiNg"
swapped_string = string.swapcase()

print(swapped_string)  # Output: "tHiS iS a StRiNg"


# ANother example 


import unicodedata

# Initialize a string with non-ASCII characters
string = "ThIs Is A sTrInG with non-ASCII characters áéíóú"

# Normalize the string to its ASCII equivalent
# Normalize the string to its NFD form
normalized_string = unicodedata.normalize('NFD', string).encode('ascii', 'ignore').decode()

# Use the swapcase() method to convert the string to "tHiS iS a StRiNg with non-ASCII characters ÁÉÍÓÚ"
swapped_string = normalized_string.swapcase()

print(swapped_string)  # Output: "tHiS iS a StRiNg with non-ASCII characters ÁÉÍÓÚ"