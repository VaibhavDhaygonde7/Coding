import re

mystr = "Vaibhav is good boy and he likes to code in c++ and python. 12345-1234"

# patt = re.compile(r"good")
# patt = re.compile(r".good")
# patt = re.compile(r'^Vaibhav')    #this will return an object if the string starts will Vaibhav
# patt = re.compile(r'python$')      #this will return an object if the string ends with python
# patt = re.compile(r'is*')      
# patt = re.compile(r'\AVaibhav')     #this will return an object if the string starts with Vaibhav  
# patt = re.compile(r'\b good')       #this will return an object if the word is present in the list
patt = re.compile(r'\d{5}-\d{4}')    #this will find 5 digits with a dash and there are 4 digits next
matches = patt.finditer(mystr)

for match in matches:
    print(match)
    # print(mystr[11:15])
