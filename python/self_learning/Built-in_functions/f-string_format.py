name = 'John'
age = 30

# Using an f-string
print(f'{name} is {age} years old.')

# Using the format() method
print('{} is {} years old.'.format(name, age))


# format() avantage more control:

# Using the format() method with format specifiers
print('{:>10} is {:<8} years old.'.format(name, age))


# f-string avantage is more readable:

# Using f-strings with format specifiers
print(f'{name:>10} is {age:<8} years old.')


