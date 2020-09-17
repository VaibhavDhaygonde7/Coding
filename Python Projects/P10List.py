""" Declaring the list """
# NOTE: Write the list in square brackets '[]'
# here we are making a list named grocery
grocery = ["Vim Bar", "Masala", "Wheat", "Rice", "Paneer", 7]   #list can also store numbers
#the above list is a mixed list because there are strings and numbers both in the list

print(grocery)   #this will print the whole list stored in grocery

#we can also print any one item from the list
print(grocery[0])    #this will print Vim Bar

""" list of numbers """
numbers = [2, 7, 9, 11, 3]
print(numbers)
#we can also print the any one element stored in list 
print(numbers[2])

""" FUNCTIONS OF LIST """

# numbers.sort()
# print(numbers)      #this will write the list in ascending order
# numbers.reverse()    #this will reverse the list 
# print(numbers)  
print(len(numbers))    # this will print the length of the string
print(max(numbers))    # this will print the maximum value of the string
print(min(numbers))    # this will print the minimum value of the string
numbers.append(7)      # this will add number '7' to the end of the list and we can append anything many times according to our wish
print(numbers)
# some functions are commented because they might give unexpected output in the next lines of code

#NOTE: these functions will change the original list

""" SLICING IN LIST """

print(numbers[1:4])  #this will slice the first and the last element of the list
#NOTE: this will return a list but it will not change the original list
print(numbers)   #the above is proved by printing the numbers again


#extended slicing 
print(numbers[::2])    # the first value is 0 and the second value is the length of the string but the third value is 2 so it will skip 1 number                   everytime while printing


#don't take the third value lesser than -1. -1 will reverse the list but smaller numbers than -1 will give unexpected outputs

#insert function

num1 = [1,2,3,4,5]
num1.insert(1, 7)   # this will insert 7 at the index 1
print(num1)

#remove() function
num1.remove(3)
print(num1)

#pop() function
num1.pop()   #this will remove the last element
print(num1)

#changing the value of the numbers stored in num1
num1[1] = 100
print(num1)

#MUTABLE = can change
#IMMUTABLE = can not change