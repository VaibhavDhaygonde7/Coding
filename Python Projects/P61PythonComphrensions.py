# we have to make a list which would store the numbers which are divisble by 3 from 0 to 100
# normal method
ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)

print(ls)

# by list comphrension method
ls2 = [i for i in range(100) if i%3==0]

# first one is the variable second one is the loop and the third one is the conditional statement which is optional 
print(ls2)

# now will make a dictionary which would store a number and the value will be 'item i' where i is the number 
# we will do it by dictionary comphrension
dict1 = {i:f"item{i}" for i in range(100) if i % 2 == 0}
# print(dict1)
# first one is the variable second one is the loop and the third one is the conditional statement which is optional 

dict2 = {i:f"Item {i}" for i in range(5)}
# reversing the key and value
dict3 = {value:key for key,value in dict2.items()}    # we are storing the reverse of dict2 in dict3
print(dict3)

# making a set comphrension
dresses = {dress for  dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(dresses)

# we will make a generator comphrension
evens = (i for i in range(100) if i % 2 == 0)
print(type(evens))   # this will print generator object 
print(evens.__next__())
print(evens.__next__())