#Queue implemetntaion in python 

class Queue:
    
    def __init__(self):
        self.queue = []
        
    #adding an element 
    def enqueue(self, item):
        self.queue.append(item)
        return "item added {}".format(item)
    
    #remove an element from queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0) #removes first elements
    
    #display the queue
    def display(self):
        return (self.queue)
    
    def size(self):
        return len(self.queue)
q = Queue()
p = Queue()
print(q.enqueue(12))
print(q.enqueue(1))
print(p.enqueue(11))
print(p.enqueue(77))
print(p.display())
print(q.display())

    
    
        