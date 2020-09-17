a = 1
b = 2

#traditional way
temp = a
a = b
b = temp
print(a, b)

#Pro way
a2 = 1 
b2 = 2
a2, b2 = b2, a2
print(a2, b2)