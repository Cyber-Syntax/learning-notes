def get_field(record, field_name, default=None):
    # Use the getattr() function to get the value of the given field in the record
    # If the field is not present, return the default value
    return getattr(record, field_name, default)

# Define a data record
record = {
    "name": "John Smith",
    "age": 33,
    "address": "123 Main St",
    "email": "johnsmith@example.com",
}

# Use the get_field() function to get the value of different fields in the record
name = get_field(record, "name")
age = get_field(record, "age")
address = get_field(record, "address")
email = get_field(record, "email")

    # Print the values of the fields
print("Name:", name)
print("Age:", age)
print("Address:", address)
print("Email:", email)
# Bu çıktıları none olarak çalışıyor ama mantık olarak normal uygulamada
#  inputu başka yerden rahatlıkla çeker zaten.

# Another example

# Define a class representing a person
class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

# Create an instance of the Person class
person = Person("John Smith", 33, "New York, NY")

# Use the getattr() function to get the value of the location attribute
location = getattr(person, "location")
name_2 = getattr(person, "name")

# Print the location of the person
print("Location:", location)
print("Name:", name_2)
