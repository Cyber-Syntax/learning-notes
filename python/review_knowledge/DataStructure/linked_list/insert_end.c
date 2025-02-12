"""Insert a node at the end of a linked list"""

// Declare a node
struct node *newNode; 
// Allocate memory for a node
struct node *newNode = malloc(sizeof(struct node));
// Store data
newNode->data = 5;
// Change next of new node to point to head
newNode->next = head;
// Change head to point to recently created node
head = newNode;
