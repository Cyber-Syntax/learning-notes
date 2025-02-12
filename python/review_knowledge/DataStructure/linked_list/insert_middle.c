"""Insert at the middle of a linked list"""
// Declare a node
struct node *newNode;
// Allocate memory for a node
struct node *newNode = malloc(sizeof(struct node));
// Store data
newNode->data = 5;

// Traverse to node just before the required position of new node
struct node *temp = head;

for (int i = 2; i < postion; i++) {
    if(temp -> next != NULL) {
        temp = temp -> next;
    } else {
        printf("Position not found\n");
        return;        
    }
}
// Change next pointers to include new node in between
newNode -> next = temp -> next;
temp -> next = newNode;