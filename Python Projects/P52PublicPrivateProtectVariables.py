class Employee:
    no_of_leaves = 8
    var = 8
    _protect = 10    #this is a protected variable 
    __private = 12   #this is a private variable 
    #we can print protect variable and it can be used by the derived classed
    #we can print private variable but cannot be use the derived class

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves 

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good", string)
        return "something"

harry = Employee("Harry", 500, "Instructor")
# printing protected variable 
print(harry._protect)

# printing private variable
print(harry._Employee__private)    #remember to write _ClassName before private variable to access it