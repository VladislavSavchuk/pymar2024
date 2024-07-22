"""This file contains the keywords for the library."""

from robot.api.deco import keyword
from homework.homework11.library import Books, User


@keyword
def create_book_instance(book_name, author, isbn, page_count):
    """ Create an instance of the Books class. """
    return Books(book_name, author, isbn, page_count)


@keyword
def create_user_instance():
    """ Create an instance of the User class. """
    return User()


@keyword
def reserve_book(book, user):
    """ Reserve a book. """
    return book.reservation(user)


@keyword
def borrow_book(book, user):
    """ Borrow a book. """
    return user.take_book(book)


@keyword
def return_book(book):
    """ Return a book. """
    return book.returning()
