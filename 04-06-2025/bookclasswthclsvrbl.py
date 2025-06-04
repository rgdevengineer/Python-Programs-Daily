
# Book Class with Class Variable

class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("Python Basics")
book2 = Book("OOPS Concepts")
book3 = Book("Advance Python")

print("Total Books = ", Book.total_books)