class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.asalary = asalary
        self.role = arole
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and the role is {self.role}"

    @classmethod    #this decorator is used to access the class
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves 
        #cls is the class of the object we are talking about

    #using class methods instead of constructor
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        # one-liner code for above
        return cls(*string.split("-"))

harry = Employee("Harry", 500, "Instructor") 
rohan = Employee("Rohan", 100, "Student")
karan = Employee.from_dash("Karan-200-Student")
harry.change_leaves(10)

print(harry.no_of_leaves)

print(karan.name)