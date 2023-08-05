class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                status = "Available" if book.available else "Borrowed by " + book.borrower
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

    def borrow_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    book.borrower = borrower
                    print(f"{book.title} has been borrowed by {borrower}.")
                else:
                    print(f"{book.title} is already borrowed by {book.borrower}.")
                return
        print("Book with the provided ISBN not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    book.borrower = None
                    print(f"{book.title} has been returned.")
                else:
                    print(f"{book.title} is already available in the library.")
                return
        print("Book with the provided ISBN not found.")

def main():
    library = Library()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            borrower = input("Enter your name: ")
            library.borrow_book(isbn, borrower)
        elif choice == 4:
            isbn = input("Enter the ISBN of the book you want to return: ")
            library.return_book(isbn)
        elif choice == 5:
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
