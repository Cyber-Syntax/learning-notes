# Write me remove() python example for beginner
# with explaining code with comments and give me beginner and advanced real world scenerio


# Beginner example:
# The following code creates a list, and then removes the number 3 from it:

my_list = [1, 2, 3, 4, 5]  # Create list
print(my_list)  # Print list

my_list.remove(3)  # Remove 3 from list
print(my_list)  # Print list

# Advanced example: 
# The following code creates a list of dictionaries, and then removes the dictionary with the key "name" equal to "John":

my_list = [{'name': 'John', 'age': 30}, {'name': 'Mary', 'age': 23}, {'name': 'Alex', 'age': 27}]  # Create list
print(my_list)  # Print list

for item in my_list:  # Iterate through list # Listeyi yinele
    if item['name'] == 'John':  # Check if dictionary has key 'name' equal to 'John'
        my_list.remove(item)  # Remove the dictionary from list
        break  # Exit loop

print("remove example: ",my_list)  # Print list""""""""""""""""""""""""""""""""""

# pop() example

for i, item in enumerate(my_list):  # Iterate through list with index
    if item['name'] == 'John':  # Check if dictionary has key 'name' equal to 'John'
        my_list.pop(i)  # Remove the dictionary at index i from the list
        break  # Exit loop

print("pop example: ", my_list)
