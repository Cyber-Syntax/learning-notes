# Write me popitem() python example. Explain code with comments for beginner. Write me beginner and real world scenerio.

# popitem() yöntemi, Python'da bir sözlükten rastgele (anahtar, değer) bir öğe çiftini kaldıran ve döndüren yerleşik bir işlevdir.

# Beginner Scenario
# Let's say that you are studying for a test and you have gathered all of the information you need into a dictionary. 
# You want to use the popitem() method to get information from the dictionary one item at a time.

# Create a dictionary
studying_info = {
    'Math': 'Algebra',
    'English': 'Grammar',
    'History': 'World War II'
}

# Use the popitem() method to get one item from the dictionary
item = studying_info.popitem()

# Remove and return an item from the dictionary
print(item)
print(studying_info)

# Output
# ('History', 'World War II')

# Real-World Scenario
# Let's say you are creating an online shopping cart. 
# You are using a dictionary to store the items in the shopping cart. 
# You want to use the popitem() method to remove items from the shopping cart one item at a time.

# Create a dictionary
shopping_cart = {
    'Sunglasses': 25,
    'Shoes': 75,
    'Jacket': 100
}

# Use the popitem() method to get one item from the dictionary
item = shopping_cart.popitem()

# Print the item
print(item)

# Output
# ('Jacket', 100)