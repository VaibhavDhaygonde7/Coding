def factorial_iterative(n):
    """
    this function will calculate the factorial of the passed number
    """
    #this is an example of iterative function
    fac = 1
    for i in range(n):
        fac = fac * (i+1)

    return fac

def factorial_recursive(n):
    """
    this function will calculate the factorial of the passed number using recursive method
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("Enter the number")
number = int(input())

# print(factorial_iterative.__doc__)
print("Factorial using iterative method ", factorial_iterative(number))
print("Factorial using recursive method ", factorial_recursive(number))