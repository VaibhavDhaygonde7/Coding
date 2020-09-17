"""
iterable - objects with function __iter__() or  __getitem__()
iterator - object with function __next__()
iteration - the process of iterating something is called iteration 
"""

#user-defined generator
def gen(n):
    for i in range(n):
        yield i  # this will make the function a generator 
        # yield will generate the values on the fly
        # generator will help to save our RAM

g = gen(10)   #this gen is capable of storing the values between 0 to 9 including 9
print(g)
# print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)

# how to check if the object is iterable or not 
# let's take an example of string
name = "vaibhav"
for char in name:
    print(char)      # string is iterable 

#second method 
iterable = iter(name)
print(iterable.__next__())

#remember: int is not iterable 