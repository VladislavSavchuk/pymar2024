from robot.api.deco import keyword
from homework.homework11.library import Books, User


@keyword
def create_book_instance(book_name, author, isbn, page_count):
    return Books(book_name, author, isbn, page_count)


@keyword
def create_user_instance(name):
    return User()


@keyword
def reserve_book(book, user):
    return book.reservation(user)


@keyword
def borrow_book(book, user):
    return user.take_book(book)


@keyword
def return_book(book):
    return book.returning()
