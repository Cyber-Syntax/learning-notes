# Initializing tuple , Demet başlatılıyor
tuple1 = ("Geeks", "for", "Geeks") 
print("Initial Tuple: ") 
print(tuple1) 

# Updating tuple 
tuple1 = ("Geeks", "for", "Geeks", "Passion") 
print("\nUpdated Tuple: ") 
print(tuple1)

"""
 We can't add tuple like list or dict but 
 we can update old tuple to create new tuple
"""

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Concatenate two tuples to create a new tuple
new_tuple = my_tuple + (6, 7, 8)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Repeat a tuple to create a new tuple
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Note that the original tuple is unchanged
print(my_tuple)  # Output: (1, 2, 3, 4, 5)


# Remember list and dictionary:

# Create a list
my_list = [1, 2, 3, 4, 5]

# Add an element to the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Modify an element in the list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Create a dictionary
my_dict = {1: 'a', 2: 'b', 3: 'c'}

# Add a key-value pair to the dictionary
my_dict[4] = 'd'
print(my_dict)  # Output: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Modify a value in the dictionary
my_dict[2] = 'e'
print(my_dict)  # Output: {1: 'a', 2: 'e', 3: 'c', 4: 'd'}
