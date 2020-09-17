class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.asalary = asalary
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
rohan = Employee("Rohan", 100, "Student")
karan = Employee.from_dash("Karan-200-Student")

good = karan.printgood("thing")    #this will execute the code written in printgood() and assign the return value to the variable good
print(good)     #this will print the return value of the printgood()