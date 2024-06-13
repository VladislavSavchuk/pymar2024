"""Library.
This program shows whether the user can borrow a reserved book.
"""


class Books:
    """Initialize book attributes"""
    def __init__(self, book_name, author, isbn, page_count):
        self.book_name = book_name
        self.author = author
        self.isbn = isbn
        self.page_count = page_count
        self.reserved = False
        self.busy = False

    def get_description_book(self):
        """Get description of the book"""
        descr = (f'book_name: {self.book_name}, '
                 f'author: {self.author}, '
                 f'isbn: {str(self.isbn)}, '
                 f'page_count: {str(self.page_count)}')
        print(f'Book Description: {descr}')

    def reservation(self):
        """This method allows the user to reserve a book if it is not busy"""
        if not self.busy:
            self.reserved = True
            return "Book has been successfully reserved"
        return "The book is busy. You cannot book the book"

    def receiving(self):
        """This method allows a user to borrow a book if it is not reserved
        or busy by another user."""
        if not self.busy and not self.reserved:
            self.busy = True
            return "The book is free. You can take the book"
        if self.reserved:
            return "The book is reserved. You can't take the book"
        return "The book is already taken"

    def returning(self):
        """This method allows the user to return the book"""
        if self.busy:
            self.reserved = False
            self.busy = False
            return "The book has been returned"
        if self.reserved:
            self.reserved = False
            return "The book reserve has been canceled"
        return "The book was free"


class User:
    """Initialize user actions"""
    @staticmethod
    def take_book(book):
        """This method allows the user to take the book"""
        return book.receiving()

    @staticmethod
    def reserve_book(book):
        """This method allows the user to reserve a book"""
        return book.reservation()

    @staticmethod
    def return_book(book):
        """This method allows the user to return the book"""
        return book.returning()


book_1 = Books('The Lord of the Rings', 'J.R.R. Tolkien',
               9785171358136, 1120)
book_1.get_description_book()

user_1 = User()
user_2 = User()


print(user_1.take_book(book_1))
print(user_2.take_book(book_1))
print()

print(user_1.return_book(book_1))
print(user_2.reserve_book(book_1))
print()

print(user_1.take_book(book_1))
print(user_2.return_book(book_1))
print()

print(user_1.reserve_book(book_1))
print(user_2.take_book(book_1))
