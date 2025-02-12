import string

# Create a translation table using maketrans
trans_table = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
# This is for understand to what are they doing
print(string.ascii_lowercase)  # "abcdefghijklmnopqrstuvwxyz"
print(string.ascii_uppercase)  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Use the translate method to translate the string
s = "hello world"
s_upper = s.translate(trans_table)
print(s_upper)  # "HELLO WORLD"


# Another example 


import string

# Create a translation table that removes punctuation(noktalama)
trans_table = str.maketrans('', '', string.punctuation)

# Use the translate method to remove punctuation from the string
s = "Hello, world!"
s_no_punct = s.translate(trans_table)
print(s_no_punct)  # "Hello world"
