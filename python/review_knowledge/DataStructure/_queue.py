class Queue:
    
    def __init__(self):
        self.queue = list()
    
    def __str__(self):
        return str(self.queue)
    
    # Adding elements to queue
    def enqueue(self, data):
        # Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        
        # return False if duplicate entry exists
        return False
    
    # Removing the last element from the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue Empty!")

    # Getting the size of the queue
    def size(self):
        return len(self.queue)

    # is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    # is full
    def isFull(self):
        return len(self.queue) == 10
    
    def peek(self):
        return self.queue[-1]
    
    def clear(self):
        self.queue = list()
        return self.queue

# Test
Q = Queue()
print("Check empty: ", Q.isEmpty()) # True
print("Check full: ", Q.isFull()) # False
print("Enqueue: ", Q.enqueue(1))
# more than one enqueue
print("Enqueue: ", Q.enqueue(2))
print("Enqueue: ", Q.enqueue(3))
print("Enqueue: ", Q.enqueue(4))
print("Queue: ", Q) # [4, 3, 2, 1]
print("Dequeue: ", Q.dequeue()) # 1
print("Queue: ", Q) # [4, 3, 2]
print("Size: ", Q.size()) # 3
print("Peek: ", Q.peek()) # 2 is the last element
print("Clear: ", Q.clear()) # None
print("Queue: ", Q) # []
print("Check empty: ", Q.isEmpty()) # True


