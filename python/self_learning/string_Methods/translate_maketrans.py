import string

# Create a translation table to remove all punctuation(noktalama)
translator = str.maketrans('', '', string.punctuation)

# Use the translation table to remove all punctuation from the string
no_punct = "Hello, World!".translate(translator)
print(no_punct)  # Output: "Hello World"




