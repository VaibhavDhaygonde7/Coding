class Employee:
    no_of_leaves = 8     #this is same for all the objects and this is called class variable 
    pass 

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 500
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 100
rohan.role = "Student"

print(harry.no_of_leaves)   #this will print 8 because it is same for all objects
print(rohan.__dict__)    #this will print all the variables of the object

#we can change the class variables with the help of the class
Employee.no_of_leaves = 9
print(harry.no_of_leaves)

rohan.no_of_leaves = 10   #note: this will not change the class variables but instead create a new instance variable
print(rohan.__dict__) 