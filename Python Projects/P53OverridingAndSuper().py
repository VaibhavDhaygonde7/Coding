class A:
    classvar1 = "I am a variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "I am a instance variable in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"
    
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "I am a instance variable in class B"
        super().__init__()     
        print(super().classvar1)

a = A()
b = B()

print(b.classvar1)   #this will first check the instance variable and then class B and A
# Remember that python will search for instance variables in both the classes
print(b.special, b.var1, b.classvar1)   #this will print var1 and classvar1 of class A because the super() is called at the end of B's constructor and so the value of var1 and classvar1 will be from class A