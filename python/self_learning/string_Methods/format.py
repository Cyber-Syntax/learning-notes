# Initialize a string with placeholders
string = "Hello, {name}! You are {age} years old."

# Substitute the placeholders with values
formatted_string = string.format(name="Alice", age=23)

# Print the formatted string
print(formatted_string)  # Output: "Hello, Alice! You are 23 years old."


# real world example 

# Initialize a string with placeholders
string = "Hello, {first_name} {last_name}! You have {num_emails} unread emails."

# Substitute the placeholders with values
formatted_string = string.format(first_name="Alice", last_name="Smith", num_emails=3)

# Print the formatted string
print(formatted_string)  # Output: "Hello, Alice Smith! You have 3 unread emails."


# Another example


# Initialize a string with placeholders
string = "The result of 3 + 4 is {result}."

# Substitute the placeholder with the result of the calculation
formatted_string = string.format(result=3+4)

# Print the formatted string
print(formatted_string)  # Output: "The result of 3 + 4 is 7."
