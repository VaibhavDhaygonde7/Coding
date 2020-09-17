import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]], dtype='int32')   #we can also pass here the datatype of the array

# array functions
print(arr.shape)   #this will tell us the shape of the array i.e. the number of rows and columns
print(arr.dtype)   #this will tell us the data type of the array

# function to make an array of zeros
print(np.zeros((4, 6)))   #note that the argument should be tuple 
# this will make 4 rows and 6 columns

# function to make an array of ones
print(np.ones((5)))
# note: these functions make an array of float type 

# function to make an empty array
print(np.empty((2,2)))    #this will allocate an array of 2 rows and columns 
# note: this will print 0. most of the times


# operations on array
arr2 = np.array([[1,2,3,4,5]])

print(arr2*arr2)   #this will print all the elements of the array one by one
print(arr2+arr2)   #this will print all the elements of the array one by one
print(arr2-arr2)   #this will print all the elements of the array one by one
print(arr2**arr2)  

print(1/arr2)   #this will divide 1 by each of the element in the arr2

# SLICING OF THE ARRAY
arr3 = np.array([1,2,3,4,5])
print(arr3[2:3])    #this is the same slicing as done in python

arr4 = arr3[2:5]    
#note: a copy is not passed in the arr4 and if we change the elements of the arr4 it will
#also be changed in the arr3 because they both point to the same memory location

arr4[0] = 7
print(arr3)
#to avoid this we have to use the copy()

arr5 = arr3[2:5].copy()
arr5[1] = 7     #this will not change the value in arr3
print(arr3)     

#slicing of 3 dimensional array
print(arr[0, 2])        #this will print the 3rd element of the 0th row