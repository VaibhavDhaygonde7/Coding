#-----------------------------------MAP()----------------------------------------------#

number = ["0", "1", "2"]
#by for loop
for i in range(len(number)):
    number[i] = int(number[i])
    #this will convert all the string to the integers

number[2] = number[2] + 1
print(number[2])

#by map function
number2 = ["0", "1", "2"]
number2 = list(map(int, number2))    #we have to typecaste the map to list because map is a object
#the first argument of the map() is the function to be applied and the second argument is the list on which the function is to be applied

number2[2] = number2[2] + 1
print(number2[2])

num3 = [1,2,3,4,5]     #we will make a list which would store all the squares of these numbers
squares = list(map(lambda x: x*x, num3))
print(squares)


#applying two functions at a time on numbers
def square(x):
    return x * x

def cube(x):
    return x * x * x

func = [square, cube]

for i in range(5):
    val = list(map(lambda x:x(i), func))
    #lambda is a function which apply all the functions in func to the i passed to it
    print(val)

#----------------------------------------FILTER()-------------------------------------------#

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    #this function will return true if num is greater than 5
    return num>5

greater_5 = list(filter(is_greater_5, list_1))
#filter is a object so we have typecasted it to list
#the first argument is the function to be applied and the second argument is the list on which the function is to be applied
#function will return something if the function returns true
print(greater_5)


#---------------------------------REDUCE()---------------------------------------------------#
from functools import reduce

numerals = [1,2,3,4,5]
#we have to make a function which will add all the elements of the list numerals
#by using for loop
num1 = 0
for i in numerals:
    num1 = num1 + i

print(num1)

#by using reduce()
num2 = reduce(lambda x,y:x+y, numerals)  #this will apply add function to all the elements of the list numerals
print(num2)