class MyCircularQueue():
    
    def __init__(self, k):
        
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1
    
    # Insert an element into Queue
    def enqueue(self, data):
        
        if ((self.tail + 1)% self.k == self.head):
            print("Full")
        
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
        
    # deleting an element 
    def dequeue(self):
        if self.head == -1:
            print("Queue is empty")
        
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head +1) % self.k
            return temp
    
    def printQueue(self):
        if self.head == -1:
            print("Empty")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail+1):
                print(self.queue[i], end=" ")
            print()
            

ob = MyCircularQueue(5)
ob.enqueue(3)
ob.enqueue(5)
ob.enqueue(8)
ob.enqueue(5)
ob.enqueue(8)
ob.enqueue(5)
ob.printQueue()
            
        




