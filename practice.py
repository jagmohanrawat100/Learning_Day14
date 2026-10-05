print("hello again Lambda Function")

#lambda arguments: expression

multi = lambda x,y:x*y
print(multi(5,4))

#also
print(multi(5,4)),print(multi(10,4))

#in case of lambda we can give only one expression, unlike in functions as below example

def addtwo(A,B):
    return A+B ,  A*B

x = addtwo(4,5)

print(x)
#(9, 20)

#return A+B and A*B here output will be 20 not 9 because and gives both positive but output will come as the latest output pyton gets from last expression

#Lambda in LIST
#Creat read update and delete CRUD Operations

students = [
    ("Ram", 85),
    ("Shyam", 92),
    ("Mohan", 78)
]
students.sort(key=lambda x:x[1])
print(students)

#now create data in list, list inside list

students = [
    ["Ram", 85],
    ["Shyam", 92],
    ["Mohan", 88]
]
students.sort(key=lambda x:x[1]) #here column 1 is sorted means numbers [['Ram', 85], ['Mohan', 88], ['Shyam', 92]]
#students.sort(key=lambda x:x[0]) #here column 0 means names are sorted [['Mohan', 88], ['Ram', 85], ['Shyam', 92]]
print(students)

#Error Handling Next Topic , exceptional handling

import numpy as np

arr = np.array([[2,3,4,5],[6,7,8,9]])
#print(arr[1]) #output [6 7 8 9]
print(arr[0]) # output [2 3 4 5]

#LIST COMPREHENSION

square = [x*x for x in range (1,6)]
print(square)
