# Initialize our list
ToDoList = []

# Function to add items to our list
def addItem(item):
    ToDoList.append(item)
    print("Item Added.")

# Function to remove items from our list
def removeItem(item):
    ToDoList.remove(item)
    print("Item Removed.")

# Function to show our list
def showList():
    print("Here is your To-Do List:")
    for item in ToDoList:
        print("[ ]", item)

# Function to mark items as done
# !, find the updating item like this
def markDone(item):
    ToDoList.append("[X]", item)
    print("Marked done.")

# Main function to run program
def main():
    while True:
        print("What would you like to do?")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Mark as Done")
        print("4. Show List")
        print("5. Quit")
        userInput = int(input("Enter your choice: "))
        if userInput == 1:
            item = input("Enter item to add: ")
            addItem(item)
        elif userInput == 2:
            item = input("Enter item to remove: ")
            removeItem(item)
        elif userInput == 3:
            item = input("Enter item to mark as done: ")
            markDone(item)
        elif userInput == 4:
            showList()
        elif userInput == 5:
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()