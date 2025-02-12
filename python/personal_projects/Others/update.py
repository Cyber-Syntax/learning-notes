from collections import OrderedDict


# This is when we need to add specific index with update
# We can add specific index with insert but we can't use dict, we can use list with insert()
# Create an OrderedDict object
fruits = OrderedDict()

# Add some key-value pairs
fruits["apple"] = 1
fruits["banana"] = 2
fruits["cherry"] = 3

# Insert a new key-value pair at index 2
fruits.update({2: "mango"})

# Print the updated OrderedDict
print(fruits)  # Output: OrderedDict([('apple', 1), (2, 'mango'), ('banana', 2), ('cherry', 3)])
