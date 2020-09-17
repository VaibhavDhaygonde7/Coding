class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.asalary = asalary
        self.role = arole
        #this method is called a constructor and it will do the work automaically
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and the role is {self.role}"

harry = Employee("Harry", 500, "Instructor")  #the arguments passed to the class will be passed to the __init__()

print(harry.name)