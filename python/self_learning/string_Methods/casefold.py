# Convert a string to lowercase using casefold()

string = "Hello World!"
print(string.casefold())  # outputs "hello world!"

# real world usage

# Delete words that are not in lowercase and add the lowercase version of the word to check

# List of words
words = ["banana", "Orange", "Pineapple", "ApPle"]

# Word to check
word = "aPpLE" 

# Convert the word to check to lowercase
word = word.casefold()

# Delete words that are not in lowercase
words = [w for w in words if w.casefold() == w]

# Add the lowercase version of the word to check to the list
words.append(word)

# Print the updated list of words
print(words)


# This is the update lowercase words

# Convert all words in a list to lowercase

# List of words
words = ["banana", "OraNge", "Pineapple", "ApPle"]

# Word to check
word = "aPpLE"

# Convert the word to check to lowercase
word = word.casefold()

# Convert all words in the list to lowercase
words = [w.casefold() for w in words]

# Add the lowercase version of the word to check to the list
words.append(word)

# We are using set to delete 2 "apple" here because 
# we didn't want to add 2 "apple" variable in list.
words = set(words)
# Print the updated list of words
print(words)


# More words to check:

# Check if multiple words are already in a list and remove any duplicates

# List of words
words = ["banana", "Orange", "Pineapple", "ApPle"]

# Words to check
check_words = ["aPpLE", "orange", "pineApple", "BANANA"]

# Convert the words to check to lowercase
check_words = [w.casefold() for w in check_words]

# Delete words that are not in lowercase
words = [w for w in words if w.casefold() == w]

# Add the lowercase versions of the words to check to the list
words.extend(check_words)

# Convert the list to a set to remove duplicates
words = set(words)

# Print the updated list of words
print(list(words))
