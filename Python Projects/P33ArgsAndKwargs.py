#note: it is not compulsory to use the word args we can also other words
def funargs(normal, *args, **kwargs):
    print(normal)     #this is a normal argument 
    print(type(args))    #remember that a tuple is passed in args 
    for items in args:
        print(items)
        #args help us to print the whole list or tuple

    for key, value in kwargs.items():
        print(f"{key} is {value}")

#REMEMBER: Order of the arguments in a function = (normal_argument, *args, **kwargs)
#write the order of the arguments in the same order

names = ["Ratan", "Mukesh", "Adani", "Poonawala"]
normal = "hello, this is a normal argument"
kw = {"Ratan":"Tata", "Mukesh":"Reliance", "Adani":"Food", "Poonawala":"Gold"}

funargs(normal, *names, **kw)
#args and kwargs are optional, if we don't pass them then they are not used!!!