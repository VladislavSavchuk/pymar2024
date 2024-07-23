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
        return descr

    def reservation(self, user):
        """This method allows the user to reserve a book if it is not busy"""
        if not self.busy and not self.reserved:
            self.reserved = True
            self.reserved_by = user
            return True
        if self.busy:
            return "busy"
        if self.reserved:
            return "reserved"
        return None

    def receiving(self, user):
        """This method allows a user to borrow a book if it is not reserved
        or busy by another user."""
        if not self.busy and (not self.reserved or self.reserved_by == user):
            self.busy = True
            self.reserved = False
            self.reserved_by = None
            return True
        if self.reserved and self.reserved_by != user:
            return "reserved_by_other"
        return "taken"

    def returning(self):
        """This method allows the user to return the book"""
        if self.busy:
            self.busy = False
            if not self.reserved:
                return "returned"
            return "returned_reserved"
        if self.reserved:
            self.reserved = False
            self.reserved_by = None
            return "reserve_cancelled"
        return "free"


class User:
    """Initialize user actions"""
    def take_book(self, book):
        """This method allows the user to take the book"""
        return book.receiving(self)

    def reserve_book(self, book):
        """This method allows the user to reserve a book"""
        return book.reservation(self)

    def return_book(self, book):
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
