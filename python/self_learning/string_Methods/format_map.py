# define a dictionary with placeholders as keys and values as values
data = {
  'name': 'John',
  'age': 30,
  'city': 'New York'
}

# define a string with placeholders enclosed in curly braces
template = 'My name is {name}, I am {age} years old, and I live in {city}.'

# use the format_map() method to fill in the placeholders with the values from the data dictionary
formatted_string = template.format_map(data)

print(formatted_string)  # prints 'My name is John, I am 30 years old, and I live in New York.'


# Another example


# define a dictionary with placeholders as keys and values as values
data = {
  'product': 'Apple',
  'price': 1.99,
  'quantity': 10
}

# define a string with placeholders enclosed in curly braces
template = 'You have ordered {quantity} {product}(s) at a total price of ${price:.2f}.'

# use the format_map() method to fill in the placeholders with the values from the data dictionary
formatted_string = template.format_map(data)

print(formatted_string)  # prints 'You have ordered 10 Apple(s) at a total price of $1.99.'


# Another example 

# define a class with attributes that match the placeholders in the template string
class Customer:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city

# create an instance of the Customer class
customer = Customer('John', 30, 'New York')

# define a string with placeholders enclosed in curly braces
template = 'My name is {name}, I am {age} years old, and I live in {city}.'

# use the format_map() method to fill in the placeholders with the values from the customer object
# vars() returns a dictionary of the object's attributes and their values
# vars just taking the values in class Customer.
formatted_string = template.format_map(vars(customer))

print(formatted_string)  # prints 'My name is John, I am 30 years old, and I live in New York.'
