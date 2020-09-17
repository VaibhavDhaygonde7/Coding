import numpy as np

arr1 = np.array([[1,2,3], 
                [4,5,6]])

print(arr1.sum(axis=1))     #this will calculate the elements row by row 
print(arr1.sum(axis=0))     #this will calculate the elements column by column

arr2 = np.array([[6,7,0], [5364,123,8]])

# function to find a cross product
print(np.cross(arr1, arr2))


# SORT() 
print(np.sort(arr2))   #this will arrange all the elements in the ascending order and it is sorting at 
                       #axis=1
# we can also pass one more argument which is kind in the sort() such as kind="mergesort",
#  kind = "quick sort" 