class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def display(self):
        print("Books List:")
        for book in self.books:
            if(book.available):
                isAvail="Available"
            else:
                isAvail="Not Available"
            print(f"{book.title} by {book.author} - {isAvail}")

    def add(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"'{title}' by {author} has been added successfully!")

    def borrow(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"'{title}': borrowed")
                return
        print(f"'{title}': Not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"'{title}': returned")
                return
        print("Invalid return")

def main():
    lib = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Display books")
        print("2. Add book")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            lib.display()
        elif choice == 2:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            lib.add(title, author)
        elif choice == 3:
            title = input("Enter the title of the book: ")
            lib.borrow(title)
        elif choice == 4:
            title = input("Enter the title of the book: ")
            lib.return_book(title)
        elif choice == 5:
            print("Thank you for Visiting!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
