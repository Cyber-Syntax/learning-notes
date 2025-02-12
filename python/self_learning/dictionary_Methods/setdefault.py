# Write me setdefault() python example. Explain code with comments for beginner. Write me beginner and real world scenerio.

# Beginner Scenario
# A dictionary is a collection of key-value pairs. 
# Sözlük, anahtar/değer çiftlerinin bir koleksiyonudur.
# The setdefault() method in Python allows you to set a value for a key if the key is not already in the dictionary.

# Here is an example of the setdefault() method being used in a dictionary.

# Create a dictionary
my_dict = {
  'name': 'John',
  'age': 26
}

# Set a value for a key if it is not already in the dictionary
my_dict.setdefault('favorite_color', 'blue')

# Print the updated dictionary
print(my_dict)

# Output: {'name': 'John', 'age': 26, 'favorite_color': 'blue'}

# In this example, the key 'favorite_color' was not already in the dictionary. 
# The setdefault() method was used to add the key-value pair 'favorite_color': 'blue' to the dictionary.

# Real World Scenario
# Let's say you are creating a program to store the phone numbers of your contacts. 
# You want to use a dictionary to store each contact's name and phone number.

# Here is an example of the setdefault() method being used in this scenario.

# Create a dictionary
contacts = {
  'John': '555-123-4567',
  'Mary': '555-345-6789'
}

# Set a value for a key if it is not already in the dictionary
contacts.setdefault('Jack', '555-678-9012')

# Print the updated dictionary
print(contacts)

# Output: {'John': '555-123-4567', 'Mary': '555-345-6789', 'Jack': '555-678-9012'}

# In this example, the key 'Jack' was not already in the dictionary. 
# The setdefault() method was used to add the key-value pair 'Jack': '555-678-9012' to the dictionary.


# Another example 

# Initialize an empty dictionary to store login counts
login_counts = {}

def record_login(user_id):
    # Set the default value for the given user ID to 0 if it is not already present in the dictionary
    login_counts.setdefault(user_id, 0)
    # Increment the login count for the given user ID by 1
    login_counts[user_id] += 1

# Record login for user 1
record_login(1)
# Record login for user 2
record_login(2)
# Record another login for user 1
record_login(1)

# Print the login counts for all users
print(login_counts)  # {1: 2, 2: 1}

