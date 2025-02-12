class MyClass(object):
    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)

my_obj = MyClass(5)
my_obj.print_x()  # Output: 5


# Another example 

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

john = Person('John', 32)
print(john.get_name())  # Output: John
print(john.get_age())  # Output: 32

john.set_age(33)
print(john.get_age())  # Output: 33

# Another example with input:

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

# Create a new instance of the Person class
john = Person('John', 32)

# Get the person's current age
print(f'{john.get_name()} is currently {john.get_age()} years old.')

# Ask the user for the person's new age
new_age = input('Enter the person\'s new age: ')

# Set the person's age to the new age
john.set_age(new_age)

# Print the person's updated age
print(f'{john.get_name()} is now {john.get_age()} years old.')
