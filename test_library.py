class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The unique identifier for the book.
        total_copies (int): Total copies of the book in the library.
        available_copies (int): Currently available copies for borrowing.
    """
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies


class Library:
    """
    Represents a library that manages books.

    Attributes:
        books (dict): A dictionary mapping ISBNs to Book objects.
    """
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn, total_copies):
        """
        Adds a book to the library or updates an existing book's copies.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN of the book.
            total_copies (int): Number of copies to add.
        """
        if isbn in self.books:
            book = self.books[isbn]
            book.total_copies += total_copies
            book.available_copies += total_copies
        else:
            self.books[isbn] = Book(title, author, isbn, total_copies)
        print(f"Book '{title}' by {author} added successfully.")

    def borrow_book(self, isbn):
        """
        Borrows a book from the library if available.

        Args:
            isbn (str): ISBN of the book to borrow.
        """
        if isbn in self.books:
            book = self.books[isbn]
            if book.available_copies > 0:
                book.available_copies -= 1
                print(f"You have borrowed '{book.title}'.")
            else:
                print(f"Sorry, '{book.title}' is not available.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        """
        Returns a book to the library.

        Args:
            isbn (str): ISBN of the book to return.
        """
        if isbn in self.books:
            book = self.books[isbn]
            if book.available_copies < book.total_copies:
                book.available_copies += 1
                print(f"Thank you for returning '{book.title}'.")
            else:
                print(f"All copies of '{book.title}' are already in the library.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def view_books(self):
        """
        Displays all books in the library with their details.
        """
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books.values():
                print(f"{book.title} by {book.author} - ISBN: {book.isbn} - Available: {book.available_copies}/{book.total_copies}")


if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "123", 3)
    library.add_book("1984", "George Orwell", "456", 2)

    # Viewing books
    print("\nAvailable Books:")
    library.view_books()

    # Borrowing books
    print("\nBorrowing a book:")
    library.borrow_book("123")
    library.borrow_book("123")

    # Viewing books after borrowing
    print("\nAvailable Books After Borrowing:")
    library.view_books()

    # Returning books
    print("\nReturning a book:")
    library.return_book("123")

    # Viewing books after returning
    print("\nAvailable Books After Returning:")
    library.view_books()