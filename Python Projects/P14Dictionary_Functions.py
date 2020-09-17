d1 = {"Vaibhav":"Paneer", "Ritika":"Pani Puri", "Suresh":"Chocolate", "Vaishali":"Manchurian"}
d2 = d1     #this is not the copy of d1

del d2["Vaibhav"]   # Vaibhav will also be deleted from d1
print(d1)

d3 = d1.copy()       # d3 is the copy of d3
del d3["Ritika"]   # Ritika will not be deleted from d1
print(d1)

#Accessing elements from dictionary
print(d1.get("Ritika"))

#Adding elements using update()
d1.update({"Akshay":"Nutritious Food"})   #Akshay will be added to the dictionary d1 at the end 
print(d1)

#keys() function
print(d1.keys())

#items() function
print(d1)