class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls, leaves):
        cls.change_leaves = leaves 

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and the role is {self.role}"

# The method which start with '__' and end with '__' (double underscore) are called as Dunder Method 
# __init__ is an example of dunder method
emp1 = Employee("Harry", 500, "Programmer")
emp2 = Employee("Rohan", 50, "Cleaner")

print(emp1 + emp2)     #for adding two objects it will go to the __add__()
print(emp1 / emp2)     #for dividing it will go to the __truediv__()

print(str(emp1))
print(repr(emp1))   #remember that if we print the object it will execute the code in __str__() 