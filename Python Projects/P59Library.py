class Library:
    bookdonate = []
    name = []
    def __init__(self, listofbooks, library_name):
        self.books = listofbooks
        self.library_name = library_name

    def lendbook(self, lend):
        self.books.remove(lend)

    def displaybook(self):
        for i in self.books:
            print(i)

    def donatebook(self, lender, book):
        self.bookdonate.append(lender)
        self.books.append(lender)
        self.name.append(book)

    def displaydonatedbook(self):
        for book, name in self.bookdonate, self.name:
            print(f"{book} is donated by {name}")

books = ["The Jungle Book", "CooperField", "Ramayana", "Mahabharat"]
vaibhav = Library(books, "Vaibhav")

vaibhav.lendbook("The Jungle Book")    #this book is given to the customer
vaibhav.donatebook("Atharva", "Oliver Twist")
vaibhav.displaybook()