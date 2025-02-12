# Get the data type of the "hello" string
hello_data_type = type("hello")

# Print the data type of the "hello" string
print(hello_data_type)


# I didn't SOLVE THIS IDIOT EXAMPLE
import re 

user_input = input("Write your name: ")
# Check the data type of the user_input variable
user_input_type = type(user_input)

# try:
    # If the user_input is not a string, raise a TypeError
    #if user_input_type != str:
if re.match("^[a-zA-Z0-9]+$", user_input):
        raise TypeError("Invalid input: expected string, got {}".format(user_input_type))

    # If the user_input is a string, process it further
elif isinstance(user_input, str):
        # Perform string processing here
        print(f"It is string name {user_input}")
#  except TypeError as e:
 #    If a TypeError is raised, print the error message
    # print(e)


# Another example

x = "Hello"
print(type(x))  # Output: <class 'str'>

y = 5
print(type(y))  # Output: <class 'int'>

z = [1, 2, 3]
print(type(z))  # Output: <class 'list'>

a = {'name': 'John', 'age': 30}
print(type(a))  # Output: <class 'dict'>
