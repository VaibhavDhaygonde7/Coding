def searcher():
    #this function will search something in the book 
    import time
    # some 3 seconds time consuming task
    book = "This is a book on harry and code with harry"
    time.sleep(3)

    # while running the coroutine second time it will start from the while True which is written below
    while True:
        text = (yield)   #this will tell python that it is a coroutine and yield will be replaced by the string passed in searcher
        if text in book:
            print("Your text is available in the book")
        else:
            print("Your text is not available in the book")

search = searcher()    #making an instance of the coroutine searcher
print("Search started....")
next(search)
print("Next method ran....")
search.send("harry")    #harry will be send to the searcher 

# releasing sources of the coroutine searcher
search.close()   # we cannot send anything to the coroutine now because we have closed it