mystr = "Vaibhav is a good boy"
mystr2 = "vaibhavisagoodboy"

print(mystr.isalnum())      #this will return true if there are no spaces in the string and it will return false if there are spaces
print(mystr2.isalnum())

print(mystr.isalpha())   #this will return true if there is no alpha and numbers in the string and false if there is no alpha and number
print(mystr2.isalpha())

print(mystr.endswith("boy"))   #this will return true if "boy" ends with mystr
print(mystr2.endswith("boy"))

print(mystr.count("v"))   #this will return the number of times the character in mystr

print(mystr2.capitalize())   #this will capitalize the first letter of the string

print(mystr.find("is"))    #this will find 'is' and it will return the index of 'i'

print(mystr.lower())      #this will convert all the letters of string to the lower case
print(mystr.upper())      #this will convert all the letters of string to the upper case

print(mystr.replace("is", "are"))