class Employee:
    no_of_leaves = 8
    var = 8

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

class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game 

    def printdetails(self):
        return f"Name is {self.name} and game is {self.game}"


class CoolProgrammer(Employee, Player):
    #note: Employee is considered while using __init__ or any other function because it is written first in the () brackets
    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 500, "Instructor") 
rohan = Employee("Rohan", 100, "Student")

shubham = Player("Shubham", "Cricket")

karan = CoolProgrammer("Karan", 1000, "CoolProgrammer")     #this is taking the arguments of the employee __init__
det = karan.printdetails()

# print(det)
# karan.printlanguage()
print(karan.var)     #this will print the value of var from the employee class which is 8