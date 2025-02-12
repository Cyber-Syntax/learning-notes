
# Beginner Example
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.append(list2)

print(list1)  # [1, 2, 3, [4, 5, 6]]

# Real World Example
employee_list = []

employee = {
  "name": "John Smith",
  "age": 42,
  "position": "Software Engineer"
}

employee_list.append(employee)

print(employee_list)  # [{'name': 'John Smith', 'age': 42, 'position': 'Software Engineer'}]



# Beginner Example:
# Append is a method in Python that allows us to add an item to the end of an existing list. 

my_list = [1, 2, 3]

# To add 4 to the end of my_list, we can use the append() method:

my_list.append(4)

# After running the code, my_list will now be [1, 2, 3, 4]

# Real World Example:
# Suppose we are creating a program to store a list of customers. We want to add a new customer to the list. 

customer_list = ["John Smith", "Jane Doe", "Mike Brown"]

# To add a new customer to the end of our list, we can use the append() method:

customer_list.append("Sally Johnson")

# After running the code, customer_list will now be ["John Smith", "Jane Doe", "Mike Brown", "Sally Johnson"].



# append() function is used to add an element to the end of a list.

# Real world example:

# Let's say you are creating a grocery list. You can use the append() function to add items to the list.

# grocery_list = []
# grocery_list.append("Milk")
# grocery_list.append("Eggs")
# grocery_list.append("Bread")

# print(grocery_list)

# This will print out: ['Milk', 'Eggs', 'Bread']