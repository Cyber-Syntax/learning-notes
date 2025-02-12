"""insert front, delete node example"""

# A linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Given a reference 
# to the head of a list and an int, 
# insert a new node on the front of the list

def insert_front(head_ref, new_data):
    # 1. allocate node    
    new_node = Node(new_data)

    # 2. put in the data
    #new_node.data = new_data

    # 3. make next of new node as head
    new_node.next = head_ref
    # 4. move the head to point to the new node
    head_ref = new_node
    return head_ref

# Function to insert element in LL
def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.next = head_ref
    head_ref = new_node
    
    return head_ref

# This function prints contents of
# linked list starting from head
def printList(node):
    while (node != None):
        print(node.data, end = " ")
        node = node.next
    print("\n")

# Delete a first node any position
def deleteNode(head_ref, position):
    temp = head_ref
    prev = head_ref
    for i in range(0, position):
        if i == 0 and position == 1:
            head_ref = head_ref.next        
        else:
            if i == position - 1 and temp is not None:
                prev.next = temp.next
            else:
                prev = temp

                # Posiiton is greater than number of nodes
                if prev is None:
                    break
                temp = temp.next
    return head_ref

# Driver code
if __name__ == '__main__':
    # Start with the empty list
    head = None
    head = push(head, 7)
    head = push(head, 1)
    head = push(head, 3)
    head = push(head, 2)

    print("Created Linked List: ", end = "")
    printList(head)

    # insert 8. So linked list becomes 8->2->3->1->7->None
    head = insert_front(head, 8)

    print("Created Linked List: ", end = "")
    printList(head)

    # delete node at position 4
    head = deleteNode(head, 4)

    print("Delete position 4 in linked list: ", end = "")
    printList(head)