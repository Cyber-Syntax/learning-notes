"""middle, beginning, end insert and delete"""

# Define a Node class to represent nodes in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None # initialize head pointer as None

    def delete_beginning(self):
        if self.head is None:
            print("The list empty")
        else:
            # Move the head pointer to the next node
            self.head = self.head.next

    def delete_middle(self, target):
        if self.head is None:
            print("The list empty")
        else:
            temp = self.head # initialize current or temporary node
            prev = self.head # initialize previous node
            while temp is not None: # Iterate through the list
                if temp.data == target: # If the target is found
                    prev.next = temp.next # update previous node's next pointer to skip the current node
                    break
                else:
                    prev = temp # move previous pointer to the current node
                    temp = temp.next # move current pointer to the next node
                
    def delete_end(self):
        if self.head is None:
            print("The list empty")
        else:
            temp = self.head # initialize current or temporary node
            prev = self.head # initialize previous node
            while temp.next is not None:
                prev = temp # move previous pointer to the current node
                temp = temp.next # move current pointer to the next node
            prev.next = None # update previous node's next pointer to None, to remove the last node

    def insert_beginning(self, data):
        new_node = Node(data) # create new node
        new_node.next = self.head # Set the new node's next pointer to the current head
        self.head = new_node # Set the new node as the new head

    def insert_middle(self, target, data):
        new_node = Node(data) # create new node
        temp = self.head # initialize current or temporary node
        prev = self.head # initialize previous node
        while temp is not None:
            if temp.data == target: # If the target is found
                prev.next = new_node # update previous node's next pointer to the new node
                new_node.next = temp # Set the new node's next pointer to the current node
                break
            else:
                prev = temp # move previous pointer to the current node
                temp = temp.next # move current pointer to the next node
            
    def insert_end(self, data):
        new_node = Node(data) # create new node
        temp = self.head # initialize current/temporary node

        while temp.next is not None: # Iterate through the list
            temp = temp.next # move current pointer to the next node
        
        temp.next = new_node # Set the current node's next pointer to the new node
    
    def searchNode(self, target):
        temp = self.head # initialize current/temporary node

        while temp != None: # Iterate through the list
            if temp.data == target: # Check if current node's data is equal to the target
                return True # Node with target value found

            temp = temp.next # move current pointer to the next node
        
        return False # Node with target value not found

    def sortLinkedList(self):
        temp = self.head  # Initialize current/temporary node
        index = Node(None)  # Initialize index node

        if self.head is None:  # Check if the list is empty
            return
        else:
            while temp is not None:  # Iterate through the list
                index = temp.next  # Index points to the node next to the current node

                while index is not None:  # Iterate through the remaining nodes
                    if temp.data > index.data:  # Compare the data of the current node with the index node
                        temp.data, index.data = index.data, temp.data  # Swap the data if necessary

                    index = index.next  # Move the index pointer to the next node

                temp = temp.next  # Move the current pointer to the next node
        
    def printList(self):
        temp = self.head # initialize current/temporary node
        
        while (temp): # Iterate through the list
            print(temp.data, end = " ") # print current node's data
            temp = temp.next # move current pointer to the next node
        print("\n")

if __name__ == "__main__":
    # Start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    llist.head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth
    fifth.next = sixth

    print("Given Linked List: ", end = "")
    llist.printList() # 1 2 3 4 5 6

    llist.insert_beginning(0)
    print("Insert 0 at beginning: ", end = "")
    llist.printList() # 0 1 2 3 4 5 6

    llist.insert_middle(3, 2.5)
    print("Insert 2.5 after 2: ", end = "")
    llist.printList() # 1 2 2.5 3 4 5 6

    print("Delete beginning: ", end = "")
    llist.delete_beginning()
    llist.printList() # 1 2.5 3 4 5 6

    print("Delete middle: ", end = "")
    llist.delete_middle(3)
    llist.printList() # 1 2.5 4 5 6

    print("Delete end: ", end = "")
    llist.delete_end()
    llist.printList() # 1 2.5 4 5

    llist.insert_end(3)
    print("Insert 3 at end: ", end = "")
    llist.printList() # 1 2.5 4 5 3

    print("Search 2: ", end = "")
    if llist.searchNode(2):
        print("Found")
    else:
        print("Not Found")

    print("Sort Linked List: ", end = "")
    llist.sortLinkedList()
    llist.printList() # 1 2.5 4 5 6


