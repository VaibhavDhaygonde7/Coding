# lambda function are also called as anonymous functions
add = lambda x, y: x + y
minus = lambda x,y: x - y
#this lambda function will take two arguments x and y and will return x + y which is written after the colon ':'

# def add(x, y):
#     return x + y

print(add(5, 2))
print(minus(5, 2))

#sort() 
a = [[2,5], [1, 10], [3,0]]
a.sort(key=lambda a: a[1])    #this will sort the 1st element of the list in list

print(a)