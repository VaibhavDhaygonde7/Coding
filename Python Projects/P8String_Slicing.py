mystr = "Vaibhav is a good boy"

# there is len() function in python which will write the number of elements or string in the string 
print(len(mystr))   

# we can also take a part of string using string slicing
print(mystr[0:7])   # 0 is included in slicing while 7 is exclueded while slicing

# This will cut the string from 0th element till 6th element
# NOTE: 'V' is 0th element not 1st element
# print(mystr[47])  this will display error because there are not 47 elements 


print(mystr[0:47])  # this will not display error but instead write the whole string
print(mystr[0:47])  # this will also print whole string

print(mystr[0:7])   # 0 is included in slicing while 7 is excluded while slicing
# slicing 1 character everytime
print(mystr[0:7:2])   # this will print alternate letters of 'Vaibhav'

# the following slicing will write the whole string
# print(mystr[0:21])          
# print(mystr[0:])            
# print(mystr[0::])           
# print(mystr[:21:])          
# print(mystr[::1])           
# print(mystr[0:21:1])        
# print(mystr[0:21:])         
# print(mystr[:21:1])         
# print(mystr[0::1])          
# print(mystr[:])             
# print(mystr[::]             
# the first value is 0, second value is the lenght of the string and the third value is 1

# Advanced slicing
print(mystr[-3:])   #this will count the letters in a reverse way
print(mystr[18:])


# reversing the string
print(mystr[::-1])

# reversing the string and then printing its alternate characters
print(mystr[::-2])
