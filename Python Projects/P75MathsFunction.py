class Math():
    @staticmethod
    def squrt(n):
        return n * n

    @staticmethod
    def cuberoot(n):
        return n * n * n

class Square(Math):
    def __init__(self, side):
        self.side = side

    def areaofsquare(self):
        return Math.squrt(self.side)

class Rectangle(Math):
    def __init__(self, length, height):
        self.length = length
        self.height = height 

    def areaofrectangle(self):
        return self.length * self.height

sq1 = Square(int(input("Enter the side of the square: ")))
rec1 = Rectangle(int(input("Enter the length of the rectangle: ")), int(input("Enter the height of the rectangle: ")))

print("The area of the square is", sq1.areaofsquare())
print("The area of the rectangle is", rec1.areaofrectangle())