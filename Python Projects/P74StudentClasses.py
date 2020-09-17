class Student():
    names = []
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getName(self):
        return f"The name of the student is {self.name}"
    
    def getMarks(self):
        return f"The marks of the student is {self.marks}"

    def listofstudents(self, lst):
        self.names = lst
        
    def students(self):
        for i in self.names:
            print(i)

    def listofmarks(self, lstm):
        self.marks = lstm

    def marks_update(self):
        for i in self.marks:
            print(i)
    
s1 = Student("Ratan", 96.2)
print(s1.getName())
print(s1.getMarks())

list_of_students = ["Vaibhav", "Ritesh", "Avnish", "Apoorv", "Ashwin"]
list_of_marks = [10, 20, 30, 40, 50]

s1.listofstudents(list_of_students)
s1.students()
s1.listofmarks(list_of_marks)
s1.marks_update()