"""This file contains the keywords for the library."""

from robot.api.deco import keyword
from homework.homework11.library import Books, User
from logger_config import configure_logger

# Create and configure the logger
loger = configure_logger(__name__)


@keyword
def create_book_instance(book_name, author, isbn, page_count):
    """ Create an instance of the Books class. """
    loger.info(f"Creating book instance: {book_name} by {author}")
    return Books(book_name, author, isbn, page_count)


@keyword
def create_user_instance(name):
    """ Create an instance of the User class. """
    loger.info("Creating user instance", name)
    return User()


@keyword
def reserve_book(book, user):
    """ Reserve a book. """
    loger.info(f"User {user} is trying to reserve the book: {book.book_name}")
    result = book.reservation(user)
    if result:
        loger.info(f"Book '{book.book_name}' "
                   f"successfully reserved by user {user}")
    elif result == "busy":
        loger.warning(f"Book '{book.book_name}' is currently busy")
    elif result == "reserved":
        loger.warning(f"Book '{book.book_name}' is already reserved")
    return result


@keyword
def borrow_book(book, user):
    """ Borrow a book. """
    loger.info(f"User {user} is trying to borrow the book: {book.book_name}")
    result = user.take_book(book)
    if result:
        loger.info(f"Book '{book.book_name}' "
                   f"successfully borrowed by user {user}")
    elif result == "reserved_by_other":
        loger.warning(f"Book '{book.book_name}' is reserved by another user")
    elif result == "taken":
        loger.warning(f"Book '{book.book_name}' is currently taken")
    return result


@keyword
def return_book(book):
    """ Return a book. """
    loger.info(f"Returning the book: {book.book_name}")
    result = book.returning()
    if result == "returned":
        loger.info(f"Book '{book.book_name}' successfully returned")
    elif result == "returned_reserved":
        loger.info(f"Book '{book.book_name}' returned and is now reserved")
    elif result == "reserve_cancelled":
        loger.info(f"Reservation for the book '{book.book_name}' cancelled")
    return result
