# library-managemnt
Library Management System

This is a basic Python program for managing a library's collection of books.
It allows you to add books, borrow them, return them, and view all the available books in the library.


Features:
- Add Books: Add new books to the library or update the number of copies of an existing book.
- Borrow Books: Borrow a book if there are copies available.
- Return Books: Return a borrowed book to make it available again.
- View Books: See a list of all books in the library with details about their availability.

- 
How It Works:
1. Book Class:
 - Represents a single book with information like title, author, ISBN, and the number of copies.
2. Library Class:
 - Manages a collection of books using their ISBN as the identifier.

 - 
Usage:
1. Add Books:
 Use the `add_book` method with the book title, author, ISBN, and total number of copies to add a
book to the library.
 library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "123", 3)
2. Borrow Books:
 Use the `borrow_book` method with the ISBN to borrow a book. It checks if copies are available
before allowing the borrow.
 library.borrow_book("123")
3. Return Books:
 Use the `return_book` method with the ISBN to return a book. It ensures the library doesn't exceed
the total copies.
 library.return_book("123")
4. View Books:
 Use the `view_books` method to list all books and their current availability.
 library.view_books()


Example:
Here is what you can do with the program:
1. Add books like "The Great Gatsby" or "1984."
2. Borrow a book if it is available.
3. Return a book after borrowing.
4. Check the current status of the library's collection at any time
