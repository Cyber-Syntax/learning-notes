"""Circular linked list insertion and deletion """
class Node:
    def __init__(self, data):
        """
        Create a singular circular linked list node.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data # Assign data
        self.next = None # the pointer initially points to nothing

class CircularLinkedList:
    def __init__(self):
        """
        Initialize the Circular Linked List.
        """
        self.last = None # initialize the last node of the list

    def addToEmpty(self, data):
        """
        Add a node to an empty circular linked list.

        Args:
            data: The data to be stored in the new node.

        Returns:
            The last node of the circular linked list.
        """
        if self.last is not None:
            return self.last

        # Creating the new node 'temp'
        temp = Node(data) # allocate memory, assign data
        self.last = temp # assigning data, last points to the new node
        # Creating the link
        self.last.next = self.last # the only node points to itself , i.e. forming a loop
        return self.last # return the last node , i.e. temp
    
    def addBegin(self, data):
        """
        Add a node at the beginning of the circular linked list.

        Args:
            data: The data to be stored in the new node.

        Returns:
            The last node of the circular linked list.
        """
        if self.last is None:
            return self.addToEmpty(data)
        temp = Node(data) # allocate memory, assign data
        temp.next = self.last.next # new node points to head, i.e. first node
        self.last.next = temp # last node points to new node, i.e. new node becomes the last node
        return self.last # return the last node

    def addEnd(self, data):
        """
        Add a node at the end of the circular linked list.

        Args:
            data: The data to be stored in the new node.

        Returns:
            The last node of the circular linked list.
        """
        if self.last is None:
            return self.addToEmpty(data)
        temp = Node(data) # allocate memory, assign data
        temp.next = self.last.next # new node points to head, i.e. first node
        self.last.next = temp # last node points to new node
        self.last = temp # new node becomes the last node
        return self.last # return the last node

    def addAfter(self, data, item):
        """
        Add a node after a specific node in the circular linked list.

        Args:
            data: The data to be stored in the new node.
            item: The data value of the node after which the new node should be added.

        Returns:
            The last node of the circular linked list.
        """
        if self.last is None:
            return None

        temp = Node(data) # allocate memory, assign data
        # p is the node with data = item
        p = self.last.next # initialize p with the first node
        while p:
            if p.data == item: 
                temp.next = p.next # new node points to the next node of p
                p.next = temp # p points to the new node
                if p == self.last: 
                    self.last = temp # new node becomes the last node
                    return self.last 
                else:
                    return self.last
            p = p.next # move to the next node
            if p == self.last.next: 
                print(item, "not present in the list")
                break
    
    def traverse(self):
        """
        Traverse and print the elements of the circular linked list.
        """
        if self.last is None:
            print("List is empty")
            return
        temp = self.last.next # initialize temp with the first node
        while temp: # traverse the list
            print(temp.data, end=" ") # print the data
            temp = temp.next # move to next node, stop if reached the last node
            if temp == self.last.next: 
                break
    
    def deleteNode(self, key):
        """
        Delete a node with the given key from the circular linked list.

        Args:
            key: The data value of the node to be deleted.

        Returns:
            The last node of the circular linked list.
        """
        if self.last is None:
            return None
        
        if self.last.data == key and self.last.next == self.last:
            self.last = None
            return None

        if self.last.data == key: # check if the last node is the node to be deleted
            temp = self.last.next # initialize temp with the first node
            while temp.next != self.last: # traverse the list
                temp = temp.next # move to the next node
            temp.next = self.last.next # last node points to the first node
            self.last = temp.next # new last node is the first node
            return self.last 

        temp = self.last.next
        while temp.next != self.last:
            if temp.next.data == key:
                break
            temp = temp.next

        if temp.next == self.last:
            print("Element not found in the list")
            return self.last

        temp.next = temp.next.next
        return self.last

    def deleteLastNode(self):
        """
        Delete the last node from the circular linked list.

        Returns:
            The last node of the circular linked list.
        """
        if self.last is None:
            return None
        
        if self.last.next == self.last:
            self.last = None
            return None

        temp = self.last.next
        while temp.next != self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp
        return self.last


# Driver Code
if __name__ == '__main__':
    llist = CircularLinkedList()
    last = llist.addToEmpty(6)
    last = llist.addBegin(4)
    last = llist.addBegin(2)
    last = llist.addEnd(8)
    last = llist.addEnd(12)
    last = llist.addAfter(10, 8)
    llist.traverse()

    last = llist.deleteNode(8)
    print("\nAfter deletion of node 8: ")
    llist.traverse()
    
    last = llist.deleteLastNode()
    print("\nAfter deletion of last node: ")
    llist.traverse()
