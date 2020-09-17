class Student:
    pass  

harry = Student()    #creating an object named harry
larry = Student()    #creating an object named larry
#note: harry and larry are different
print(harry, larry)

#we can give attributes to the object which is as follows:
#the variables declared below are called instance
harry.name = "Harry"
harry.std = 12
harry.section = 1

larry.name = "Larry"

#we can also print the attributes
print(harry.name, larry.name)