# we declare dictionary using {} curly braces
d1 = {"Vaibhav":"Paneer", "Ritika":"Pani Puri", "Suresh":"Chocolate", "Vaishali":"Manchurian"}
# remember that dictionary is case-sensitive

print(d1["Vaibhav"])  #this will print Paneer as Vaibhav eats paneer

d2 = {"Virat": {"Breakfast":"Tea", "Lunch":"Roti", "Dinner":"Rice"}}
print(d2["Virat"])
print(d2["Virat"]["Breakfast"])

# adding elements to the dictionary
d2["Ankit"] = "Vada Pav"   #this will be added to the end of the dictionary
print(d2)   #verifying whether Ankit added or not

#deleting element of the dictionary

del d2["Ankit"]    #this will delete Ankit from the dictionary
print(d2)