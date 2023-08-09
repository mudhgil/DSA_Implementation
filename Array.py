ARRAY 

from array import *

#Create an array and traverse

my_array = array('i', [1,2,3,4,5] )

# for i in my_array:
#     print(i)

#Access elements through indexes
# print(my_array[4])

#Append value to array
# my_array.append(7)
# print(my_array)

#Insert value in array
# my_array.insert(0,9)
# print(my_array)

#Extend python array using extend()
# my_array1 = array('i', [30,40,50])
# my_array.extend(my_array1)
# print(my_array)

#Add items from list into array using fromlist() method
# tempList = [100,120,140]
# my_array.fromlist(tempList)
# print(my_array)

#Remove element using remove()
# my_array.remove(5)
# print(my_array)

#Remove last element using pop()
# my_array.pop()
# print(my_array)

#Fetch element using index()
# print(my_array.index(4))

#Reverse using reverse()
# my_array.reverse()
# print(my_array)

#Get array buffer info
# print(my_array.buffer_info())
# print(my_array)

#Check occurences of element using count()
# print(my_array.count(1))

#Convert array to string using tostring() 

#Convert array to list using tolist()
# print(my_array.tolist())

#Slice elements from array
# print(my_array[::-1])

#Access element
from array import *

arr1 = array('i', [1,2,3,4,5,6])

def accessElement(array,index):
    if index >= len(array):
        print("There is no element")
    else:
        print(array[index])
accessElement(arr1, 4)

#Searching an element
arr1 = array('i', [58, 39, 54, 4, 100, 46]
)
def search(array,value):
    for i in array:
        if i == value:
            return array.index(value)
        
    return "Element not found"
search(arr1, 8)


#delete element

arr1.remove(54)
print(arr1)

#2D ARRAY
import numpy as np
twoDArray = np.array([[12,34,32,12],[23,44,22,11],[21,22,33,45],[24,32,11,23]])
print(twoDArray)

#Adding row in 2D array
twoDArray = np.array([[12,34,32,12],[23,44,22,11],[21,22,33,45],[24,32,11,23]])
print(twoDArray)
print("New 2D array")
newTwoDarray = np.insert(twoDArray, 0,[[1,2,3,4]],axis=0)
print(newTwoDarray)
                                       
#Accessing element in 2D array

twoDArray = np.array([[12,34,32,12],[23,44,22,11],[21,22,33,45],[24,32,11,23]])
print(twoDArray)

def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array)and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])
accessElement(twoDArray, 1,3)


 #traversing 2D array
twoDArray = np.array([[12,34,32,12],[23,44,22,11],[21,22,33,45],[24,32,11,23]])
print(twoDArray)

def traverseTDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traverseTDarray(twoDArray)


 #Searching 2D array
twoDArray = np.array([[12,34,32,12],[23,44,22,11],[21,22,33,45],[24,32,11,23]])
print(twoDArray)

def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "Index" + " : " + str(i) + "" + str(j)
    return 'Not found'
print(searchTDArray(twoDArray, 32))

#Delete col/row in 2D ARRAY

import numpy as np

twoDArray = np.array([[12,34,32,12],[23,44,22,11],[21,22,33,45],[24,32,11,23]])
print(twoDArray)

newTDArray = np.delete(twoDArray, 1, axis = 0)
print(newTDArray)