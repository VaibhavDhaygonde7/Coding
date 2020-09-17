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
        cls.no_of_leaves = leaves 

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good", string)
        return "something"

#we will make a class which will inherit all the attributes of the class Employee
class Programmer(Employee):
    #now class Programmer is inherited from the Employee
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"Programmer's mame is {self.name}.The salary of the programmer is {self.salary} The role is {self.role}. The languages are {self.languages}"
          
harry = Employee("Harry", 500, "Instructor") 
rohan = Employee("Rohan", 100, "Student")

shubham = Programmer("Shubham", 300, "Programmer", ["python"])
karan = Programmer("Karan", 200, "Programmer", ["python", "C++"])
#note: We can also execute Employee's function using Programmer objects
print(karan.printprog())