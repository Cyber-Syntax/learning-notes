class Person:
    def __init__(self, name, age):
        self.name = name
        self. age = age

    def __str__(self):
        # Print a dictionary of all local variables
        print(locals())

        return f"{self.name} is {self.age} years old."                    

# Print the welcome message
person = Person("Ali", 33)

print(person)




    
