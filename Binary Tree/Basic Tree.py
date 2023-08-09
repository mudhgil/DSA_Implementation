import Queue_using_LinkedList as queue

class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
fanta = TreeNode('Fanta', [])
cola = TreeNode('Cola', [])
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
tree.addChild(cold)
tree.addChild(hot)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)
print(tree)



# the __str__ method recursively 
# traverses the tree rooted at the current node and returns 
# a formatted string representation of the entire tree. The 
# level parameter is used to keep track of the depth of the 
# node in the tree, and it is used to indent the node's data 
# appropriately for visualization.

# Line 1 constructs the string representation ret by adding 
# spaces (indentation) based on the current level, followed 
# by the string representation of the current node's data, 
# and a newline character.

# Line 2 then iterates over each child node in the children 
# list of the current node. For each child, it recursively calls 
# the __str__ method with an incremented level. This recursive 
# call helps to build the string representation of the entire 
# subtree rooted at each child.

# Finally, Line 3 returns the complete string representation ret, 
# which represents the entire tree rooted at the current node in 
# a formatted and indented manner.

print('----------------Preorder----------------------')
#PRE-ORDER TRAVERSAL

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)
print('---------Inorder---------')
def inOrderTraversel(rootNode):
    if not rootNode:
        return
    inOrderTraversel(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversel(rootNode.rightChild)

inOrderTraversel(newBT)
print('------postorder---------')
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBT)

print("-----------Level order --------------")

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

levelOrderTraversal(newBT)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 'Binary tree does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return 'Success'
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return 'Not found'
print(searchBT(newBT, 'Cola'))

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.lefChild = newNode
                return 'Successfully inserted'
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.lefChild = newNode
                return 'Successfully inserted'
            
# newNode = TreeNode('Cola')
# print(insertNodeBT(newBT, newNode))
# levelOrderTraversal(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        getDeepestNode = root.value
        return getDeepestNode
deepestNode = getDeepestNode(newBT)
print(deepestNode.data)


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.righChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

newNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT)
print('-----new ')
def deleteNodeBT(rootNode,node):
    if not rootNode:
        return 'The BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return 'Node Deleted!!'
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return 'Failed to delete'

deleteNodeBT(newBT,'Hot')
levelOrderTraversal(newBT)

#delete entire tree

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BT is deleted!'

deleteBT(newBT)
levelOrderTraversal(newBT)















