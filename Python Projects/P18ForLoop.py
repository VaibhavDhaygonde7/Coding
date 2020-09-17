list1 = [ ["Vaibhav", 7], ["Ritika", 20], ["Suresh", 25], ["Vaishali", 15] ]

for items, number in list1:
    print(items,"is", number)
    #items will become the name and number will become the number assigned to each name

#converting list to dictionary
dict1 = dict(list1)

#this will print only the keyword
for items in dict1:
    print(items)

for items, number in dict1.items():
    print(items,"is", number)
    #remember to use the .items() to completely iterate a dictionary 