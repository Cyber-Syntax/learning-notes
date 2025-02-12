# Write me pop() python example for beginner
# with explaining code with comments and give me beginner and advanced real world scenerio


# Beginner Example

# Let's say you have a list of fruits and you want to remove the last item from the list. 

fruits = ["apple", "orange", "banana"]

# To do this, you can use the pop() method. This method will remove the last item from the list and return it.

last_fruit = fruits.pop()  # removes and returns the last item in the list, "banana"

# Now the fruits list contains only two items and the last_fruit variable contains the removed item, "banana"

print(fruits)   # ["apple", "orange"]
print(last_fruit)  # "banana"


# Advanced
# Example of using the pop() method to delete an element from a dictionary

# Create a dictionary
customers = {
    'John': 25,
    'Tom': 32,
    'Anna': 28
}

# Print the dictionary
print(customers)

# Use the pop() method to delete the 'Tom' element from the dictionary
age = customers.pop('Tom')

# Print the dictionary again
print(customers)

# Print the removed element from the dictionary
print(age)