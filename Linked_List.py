class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

#Insertion in a single linked List

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index <location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

#Traverse in Single Linked List

    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

#Search in Single Linked List

    def searchSLL(self, nodevalue):
        if self.head is None:
            return "This list doesn't exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return "The value doesn't exist in list"

    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
#Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL doesn't exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(2,2)
singlyLinkedList.traverseSLL()
print([node.value for node in singlyLinkedList])
print(singlyLinkedList.searchSLL(2))
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])