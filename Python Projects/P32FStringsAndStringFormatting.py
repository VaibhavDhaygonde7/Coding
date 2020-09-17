me = "Vaibhav"
n = 7

#this is the old way
a = "This is %s %s"%(me, n)

#by using format function
b = "this is {1} {0}"    #the number written in the curly braces is the order of the variables according to the format function
c = b.format(me, n)    #this will insert me and n to the curly braces

#by using f-strings
d = f"this is {me} {n} {5*2}"
#we can also perform mathematical operations in the curly braces of the f strings and even we can use functions

print(a)
print(c)
print(d)