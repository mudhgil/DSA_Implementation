#Create Stack

class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push

    def push(self, value):
        self.list.append(value)
        return "Inserted succesfully!"
    
    #pop

    def pop(self):
        if self.isEmpty():
            return "There is not any element in stack"
        else:
            return self.list.pop()
        
    #peek

    def peek(self):
        if self.isEmpty():
            return "There is no element in stack"
        else:
            return self.list[len(self.list)-1]
        
    #delete

    def delete(self):
        self.list = None


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(5)
customStack.push(7)
print(customStack)
# customStack.pop()
# print(customStack.pop())
# print(customStack.peek())


#Create stack with limited size

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #isEmpty

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    #Push
    def push(self, value):
        if self.isFull():
            return 'The stack is full'
        else:
            self.list.append(value)
            return 'Element inserted'
        
    #pop
    def pop(self):
        if self.isEmpty():
            return 'There is not element in stack'
        else:
            return self.list[len(self.list)-1]
        
    #delete
    def delete(self):
        self.list = None


customStack = Stack(4 )
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(5)
customStack.push(7)
customStack.push(11)
customStack.push(9)
customStack.push(91)
customStack.push(12)
print(customStack)


# #Create stack using Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():  
            return 'No element!'
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():  
            return 'No element!'
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
            
    def delete(self):
        self.LinkedList.head = None
            
customStack = Stack()
print(customStack.isEmpty())

customStack = Stack()
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(5)
customStack.push(7)
customStack.push(11)
customStack.push(9)
customStack.push(91)
customStack.push(12)
print(customStack)