# I inspered from chatGPT AI.
# Class printing and object deleting.

class Person:
    # ? what is the init function?
    def __init__(self, name, age, country): # Don't forget to colon    
        self.name = name
        self.age = age
        self.country = country

    # To print the class object in the example you provided, you could define a toString 
    # method in the Person class that returns a string representation of the object. 
    # Here's an example:
 
    def toString(self):
        # hasattr eğer age varsa true döndürüyor.
        if hasattr(self, 'age'):
            return f"{self.name} is {self.age} years old and lives in {self.country}"
        else:
            return f"{self.name} lives in {self.country}"


    # You could then create an instance of the Person class and print it using the toString method:

# Create an instance of the Person class
p = Person('John', 36, 'Norway')

# Print the instance using the toString method
print(p.toString())
########## John is 36 years old and lives in Norway

# Set the name attribute of the instance using the setattr function
setattr(p, 'name', "Jessica")

print(p.toString())
########## Jessica is 36 years old and lives in Norway

# You can also delete the age attribute from the instance 
# Yaş özniteliğini örnekten silebilirsiniz.
delattr(p, 'age')

# Print the instance(örnek) again using the toString method
print(p.toString())
########## Jessica lives in Norway

# Note that in the toString method, you can use the hasattr function to check if the instance has the age attribute. 
# If the age attribute is present, the toString method will return a string that includes the person's name, age, and country. 
# If the age attribute is not present, the toString method will return a string that includes only the person's name and country.

# Display the content of an object:
print(dir(Person))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'toString']