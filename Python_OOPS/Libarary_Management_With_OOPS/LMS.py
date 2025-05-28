class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.copies} copies available"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        self.books.append(Book(title, author, copies))
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                print(f"You have borrowed '{book.title}'.")
                return
        print(f"Sorry, '{title}' is not available or out of stock.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Thank you for returning '{book.title}'.")
                return
        print(f"'{title}' does not belong to this library.")


def main():
    library = Library()
    while True:
        print("\nLibrary Management System\n")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, copies)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()