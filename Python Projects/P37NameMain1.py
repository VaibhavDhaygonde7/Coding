def hello(string):
    return f"hello {string}"

def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    #in this program the value of __name__ is __main__
    #this content will not be executed if imported in another files
    print("The value of name is", __name__)
    print(hello("Vaibhav"))
    print(add(3, 7))