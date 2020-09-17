from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod   #this will give the order that every class derived to Shape should have a function named printarea
    def printarea(self):
        return 0 
    #if printarea() is not created in derived classes then it will throw error
    #NOTE: you cannot create a object of abstract class

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.height = 7

    def printarea(self):
        return self.length * self.height

rect1 = Rectangle()
# s = Shape()   #it will display error because we cannot create objects of abstract class
print(rect1.printarea())