class Employee:
    no_of_leaves = 8     #this is same for all the objects and this is called class variable 
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and the role is {self.role}"
        #self is the object about which we are talking about

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 500
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 100
rohan.role = "Student"

print(rohan.printdetails())    #rohan will be automatically passed in the printdetails()