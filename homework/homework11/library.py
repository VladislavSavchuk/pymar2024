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
        self.reserved_by = None

    def __str__(self):
        """Get description of the book"""
        descr = (f'book_name: {self.book_name}, '
                 f'author: {self.author}, '
                 f'isbn: {str(self.isbn)}, '
                 f'page_count: {str(self.page_count)}')
        return f'Book Description: {descr}'

    def reservation(self, user):
        """This method allows the user to reserve a book if it is not busy"""
        if not self.busy and not self.reserved:
            self.reserved = True
            self.reserved_by = user
            return "Book has been successfully reserved"
        if self.busy:
            return "The book is busy. You cannot reserve the book"
        if self.reserved:
            return "The book is already reserved. You cannot reserve the book"
        return None

    def receiving(self, user):
        """This method allows a user to borrow a book if it is not reserved
        or busy by another user."""
        if not self.busy and (not self.reserved or self.reserved_by == user):
            self.busy = True
            self.reserved = False
            self.reserved_by = None
            return "The book is free. You can take the book"
        if self.reserved and self.reserved_by != user:
            return "The book is reserved by another user"
        return "The book is already taken"

    def returning(self):
        """This method allows the user to return the book"""
        if self.busy:
            self.busy = False
            if not self.reserved:
                return "The book has been returned"
            return "The book has been returned, but it is still reserved"
        if self.reserved:
            self.reserved = False
            self.reserved_by = None
            return "The book reserve has been canceled"
        return "The book was free"


class User:
    """Initialize user actions"""
    @staticmethod
    def take_book(book):
        """This method allows the user to take the book"""
        return book.receiving(User)

    @staticmethod
    def reserve_book(book):
        """This method allows the user to reserve a book"""
        return book.reservation(User)

    @staticmethod
    def return_book(book):
        """This method allows the user to return the book"""
        return book.returning()


book_1 = Books('The Lord of the Rings', 'J.R.R. Tolkien',
               9785171358136, 1120)
print(book_1)

vasya = User()
petya = User()

print('1')
print(vasya.take_book(book_1))
print(petya.take_book(book_1))

print('2')
print(vasya.return_book(book_1))
print(petya.take_book(book_1))

print('3')
print(vasya.take_book(book_1))
print(petya.return_book(book_1))

print('4')
print(vasya.reserve_book(book_1))
print(petya.reserve_book(book_1))

print('5')
print(vasya.take_book(book_1))
print(petya.take_book(book_1))

print('6')
print(vasya.return_book(book_1))
print(petya.return_book(book_1))
