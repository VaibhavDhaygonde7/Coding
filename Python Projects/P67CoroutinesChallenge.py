def searcher():
    import time 
    names = ["Vaibhav", "Suresh", "Vaishali", "Ritika"]
    time.sleep(3)

    while True:
        text = (yield)
        if text in names:
            print("Your name is available in the book")
        else:
            print("Your name is not available in the book")


search = searcher()
print("Enter your name: ", end="")
name = input()
next(search)

search.send(name)

search.close()