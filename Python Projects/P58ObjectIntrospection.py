class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This is {self.fname} {self.lname}"
    
    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting now")
        name = string.split("@")[0]
        self.fname = string.split(".")[0] 
        self.lname = string.split(".")[1] 

    @email.deleter   #making a deleter for deleting email attribute
    def email(self):
        self.fname = None 
        self.lname = None 

skillf = Employee("Skill", "F")

print(type(skillf))   #this will print class Employee and this is called object introspection

print(id("This is a string"))    #every object is having a unique id and we can print it using id()

print(dir(skillf))   #this will print all the functions in the skillf

import inspect
print(inspect.getmembers(skillf))  #this will print all the attributes of skillf