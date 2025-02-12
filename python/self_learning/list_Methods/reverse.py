# Write me reverse() python example for beginner
# with explaining code with comments and give me beginner and advanced real world scenerio


# Beginner Reverse() Example

# reverse() is a built-in python function that can be used to reverse the order of a list. 
# In this example, we will have a list of numbers and use reverse() to put them in reverse order. 

# Create list of numbers
numbers = [1,2,3,4,5]

# Use reverse() to reverse the order of numbers
numbers.reverse()

# Print the reversed list
print(numbers)

# Output: [5,4,3,2,1]

# Beginner Real World Scenario
# For example, if you were creating a game of hangman, you could use reverse() to reverse the order of a list 
# of letters so that they are in the correct order when the user guesses them. 

# Advanced Reverse() Example

# reverse() can also be used to reverse the order of a string. For example, we will take a string and use reverse() 
# to put the characters in reverse order.

# Create string 
string = "Hello World"

# Use reverse() to reverse order of characters
string = "".join(reversed(string))

# Print the reversed string
print(string)

# Output: dlroW olleH

# Advanced Real World Scenario
# For example, if you were creating a web app that encrypts strings, you can use reverse() to reverse the order 
# of characters in a string and create an encrypted version of the string.