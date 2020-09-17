def hello():
    print("hello")

hello2 = hello
del hello
# hello2()       #this function will be executed

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum

a = funcret(0)
print(a)

#passing function as an argument
def executor(func):
    func("Hello")

executor(print)


def dec1(func):
    def nowexec():
        print("Executing....")
        func()
        print("Executed!!")
    return nowexec

@dec1      #now vaibhav() will be passed to the dec1() just like the 35th line of this program
def vaibhav():
    print("Vaibhav is Coding")

# vaibhav = dec1(vaibhav)
vaibhav()