class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    # property() işlevini kullanarak salary özelliğini tanımlayın
    @property
    def salary(self):
        # _salary niteliğinin değerini döndürün
        return self._salary

    # salary özelliğinin setter metodunu tanımlayın
    @salary.setter
    def salary(self, new_salary):
        # Yeni maaş değerini doğrula
        if new_salary < 0:
            raise ValueError('Salary must be a positive number.')
        self._salary = new_salary

# Bir Employee nesnesi oluşturun
e = Employee('John Doe', 50000)

# Çalışanın maaşını alın
print(e.salary)

# Çalışanın maaşını ayarlayın
e.salary = 60000
print(e.salary)



# Another example


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    # Define the age property using the property() function
    @property
    def age(self):
        # Return the value of the _age attribute
        return self._age

    # Define the setter method for the age property
    @age.setter
    def age(self, new_age):
        # Validate the new age value
        if new_age < 0:
            raise ValueError('Age must be a positive number.')
        self._age = new_age

# Create a Person object
p = Person('John Doe', 30)

# Get the person's age
print(p.age)

# Set the person's age
p.age = 40
print(p.age)

# Another example

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Define the diameter property using the property() function
    @property
    def diameter(self):
        # Return the diameter of the circle (2 * radius)
        return self.radius * 2

    # Define the setter method for the diameter property
    @diameter.setter
    def diameter(self, new_diameter):
        # Set the radius of the circle (diameter / 2)
        self.radius = new_diameter / 2

# Create a Circle object
c = Circle(5)

# Get the circle's diameter
print(c.diameter)

# Set the circle's diameter
c.diameter = 10
print(c.radius)
