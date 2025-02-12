# Define a class with a 'name' attribute
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of the Person class
person = Person("John")

# Print the initial value of the 'name' attribute
print(person.name) # Prints 'John'

# Set the value of the 'name' attribute using the setattr() function
setattr(person, "name", "Jane")

# Print the updated value of the 'name' attribute
print(person.name) # Prints 'Jane'



# Another example:

# Define a class with a 'name' and 'age' attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Person class
person = Person("John", 30)

# Print the initial values of the 'name' and 'age' attributes
print(f"Name: {person.name}, Age: {person.age}") # Prints 'Name: John, Age: 30'

# Set the value of the 'name' attribute using the setattr() function
setattr(person, "name", "Jane")

# Set the value of the 'age' attribute using the setattr() function
setattr(person, "age", 35)

# Print the updated values of the 'name' and 'age' attributes
print(f"Name: {person.name}, Age: {person.age}") # Prints 'Name: Jane, Age: 35'


# Another example:


# Define a class with a 'name' and 'age' attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Person class
person = Person("John", 30)

# Print the initial values of the 'name' and 'age' attributes
print(f"Name: {person.name}, Age: {person.age}") # Prints 'Name: John, Age: 30'

# Define a dictionary with the new values for the 'name' and 'age' attributes
new_values = {"name": "Jane", "age": 35}

# Set the values of the 'name' and 'age' attributes using the setattr() function
for key, value in new_values.items():
    setattr(person, key, value)

# Print the updated values of the 'name' and 'age' attributes
print(f"Name: {person.name}, Age: {person.age}") # Prints 'Name: Jane, Age: 35'

# Another example 

# Define a class to represent a user account
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Create a new user account
user = User("John Doe", "john.doe@example.com")

# Print the initial values of the user's name and email
print(f"Name: {user.name}, Email: {user.email}") # Prints 'Name: John Doe, Email: john.doe@example.com'

# Prompt the user to update their name and email
name = input("Enter your name:")
email = input("Enter your email:")

# Set the values of the user's name and email using the setattr() function
setattr(user, "name", name)
setattr(user, "email", email)

# Print the updated values of the user's name and email
print(f"Name: {user.name}, Email: {user.email}")


