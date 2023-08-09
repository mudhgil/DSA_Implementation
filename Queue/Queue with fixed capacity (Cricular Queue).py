class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return 'The queue is Full'
        else:
            if self.top+1 == self.maxSize:  #Situation assuming only item being added/present at last position in list self.top =0 
                self.top = 0
            else:
                self.top +=1                #else top value incremented
                if self.start ==-1:         #Situation assuming completely empty queue
                    self.start = 0          #start pointer changes to 0 after enqueueing 
            self.items[self.top] = value    #value added to the top
            return 'The element is inserted at the end of queue'
        
    def dequeue(self):
        if self.isEmpty():
            return 'No element in Queue'
        else:
            firstElement = self.items[self.start] #In dequeueing first/start element changes , in queueing last/top element changes
            start = self.start
            if self.start == self.top:            #Situation if only element present in queue, we'll set start and top = -1 (empty)
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:    
                self.start = 0
            else:
                self.start +=1
            self.items[start] = None
            return firstElement
             
    def peek(self):
        if self.isEmpty():
            return 'No element in queue!'
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
print(customQueue.peek())
customQueue.delete()
print(customQueue)
