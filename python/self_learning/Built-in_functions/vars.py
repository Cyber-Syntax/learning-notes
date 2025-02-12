class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person = Person("John", 30)
print(vars(person))  # Output: {'name': 'John', 'age': 30}

vars(person)['name'] = 'Jane'
print(vars(person))  # Output: {'name': 'Jane', 'age': 30}

# Keep in mind that the vars() function only works on objects that have a dict attribute. 