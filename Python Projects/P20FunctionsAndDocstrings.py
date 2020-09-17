def function1(a, b):
    """This function will calculate average of the two numbers passed in it"""
    # the first comment written in the function is called a docstring
    average = (a + b)/2
    return average

num1 = 5
num2 = 9
num3 = function1(num1, num2)

print(num3)

print(function1.__doc__)