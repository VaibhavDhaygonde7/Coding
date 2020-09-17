l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]

#we have to write the odd number of element from the list l1

i = 1 
for items in l1:
    if i % 2 != 0:
        print(items)
    i += 1

#by using enumerate()
for index, items in enumerate(l1):
    #we are writing here == 0 because the index start from 0 and not 1 like the above
    if index % 2 == 0:
        print(items)