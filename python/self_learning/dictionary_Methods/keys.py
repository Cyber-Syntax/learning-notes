# Write me keys() python example with explaining code with comments and give me beginner and real world scenerio


# Beginner Scenario

# The keys() method returns a list of keys from a dictionary.
# Let's create a dictionary and use keys() to return the list of keys.

my_dict = {
    "name": "John",
    "age": 20,
    "city": "New York"
    }

# To get the list of keys from the dictionary, we use the keys() method
keys_list = my_dict.keys()

# Print the list of keys
print(keys_list)

# Output: 
# dict_keys(['name', 'age', 'city'])

print('\n')
# Real World Scenario

# Let's say we have a dictionary of car models and their corresponding years. 
# We can use the keys() method to get a list of car models.

car_models = {
    "BMW 3 Series": 2018,
    "Audi A4": 2019,
    "Mercedes Benz C Class": 2020
    }

# To get the list of car models, we use the keys() method
car_models_list_keys = car_models.keys()
car_models_list_items = car_models.items()


# Print the list of car models
print("Keys: ",car_models_list_keys)
print("items: ",car_models_list_items)

# Output: 
# dict_keys(['BMW 3 Series', 'Audi A4', 'Mercedes Benz C Class'])