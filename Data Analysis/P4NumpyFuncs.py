import numpy as np

arr1 = np.arange(5)    #this will create an array of number from 0 to 4
print(arr1)


# RESHAPE() 
arr2 = np.array([12,452,63,5,13,41,46,53456,2,324])
# print(arr2.shape)
print(arr2.reshape(5,2))   #this will make an array using arr2 of 5 rows and 2 columns

# ARGSORT()
print(np.argsort(arr2))    
#this will print the index of the values which are sorted in the ascending order

# ARGSMAX() 
print(np.argmax(arr2))   #this will print the index of the largest value of the array

# ARGSMIN() 
print(np.argmin(arr2))   #this will print the index of the smallest value of the array