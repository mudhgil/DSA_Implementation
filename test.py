class Queue:


    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str[x] for x in self.items]
        return values
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self,values):
        self.items.append(values)
        return 'Value Inserted!'
    
    def dequeue(self):
        if self.isEmpty():
            return 'No item!'
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return 'No item!'
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
        return self.items