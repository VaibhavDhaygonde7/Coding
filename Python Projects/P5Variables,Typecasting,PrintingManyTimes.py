var1 = "Hello World"    # this is a string 
var2 = 7                # this is a type of integer
var3 = 7.923            # this is a type of float
var4 = "7"              # this is also a string 

print(var1)     # this will print Hello World because var1 has the value of Hello World

print(type(var1))      # this will print str
print(type(var2))      # this will print int
print(type(var3))      # this will print float

# type function writes the type of the variable written in the bracket

# we can also add a int and a float but not a int or float with string
print(var2 + var3)
print(var1 + var4)

var5 = "70"
var6 = "30"

print(var5 + var6)   # this will write the output 7030

# typecasting the var5 and var6 to int

print(int(var5) + int(var6))    # this will write the output 100
# var5 and var6 are converted to integers and this is known as typecasting
"""
typecast functions
int()
float()
str()
"""




# printing statements multiple times
print(10 * "Hello World")   # this will print the statement 10 times

# print(10 * int(var5) + int(var6))  this will print the number by 10
# for desired results typecast it into string
print(10 * str(int(var5) + int(var6)))