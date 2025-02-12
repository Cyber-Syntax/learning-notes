# Write me items() python example for beginner
# with explaining comments and give me beginner and real world scenerio


# Example 1 - Beginner:
# This example creates a dictionary called 'my_dict' with three key-value pairs, and then calls the items() method to print out each key-value pair.

my_dict = {
    "name": "John Doe",
    "age": 25,
    "city": "New York"
}

# Print each key-value pair in the dictionary
for key, value in my_dict.items():
    print(key + ": " + str(value))

# Output:
# name: John Doe
# age: 25
# city: New York


# Example 2 - Real World:
# This example creates a dictionary called 'employee_data' with four key-value pairs, and then uses the items()
#  method to iterate over each key-value pair to print out the employee data.

employee_data = {
    "name": "John Doe",
    "age": 25,
    "city": "New York",
    "job": "Software Engineer"
}

# Print each employee's data
# add this line to aling text same line like table

print("Name\t\tAge\tCity\t\tJob")

for key, value in employee_data.items():
    # add '\t' for tab space
    print(str(value) + '\t', end='')

# Output:
# Name		Age	City		Job
# John Doe	25	New York	Software Engineer
print('\n')

# Create a dictionary
fruits = {'apple': 4, 'banana': 2, 'cherry': 3}

# Get a view of the key-value pairs in the dictionary
items = fruits.items()

# Print the view object
print(items)  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])

# Iterate through the key-value pairs in the view object
for key, value in items:
    print(f'{key}: {value}')
