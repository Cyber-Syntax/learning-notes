# Create a list to store the items
todo_list = []

# Function to add items to the list
def add_item(item):
    todo_list.append(item)

# Function to mark an item as done
def mark_done(item):
    for i in range(len(todo_list)):
        if todo_list[i] == item:
            todo_list[i] = "DONE - " + item

# Function to remove an item
def remove_item(item):
    for i in range(len(todo_list)):
        if todo_list[i] == item or todo_list[i] == "DONE -" + item:
            del todo_list[i]

# Add some items to the list
add_item("Write code")
add_item("Test code")
add_item("Debug code")

# Mark an item as done
mark_done("Write code")

# Remove an item
remove_item("Debug code")

# Print the list
print(todo_list)

# Output: ["DONE - Write code", "Test code"]