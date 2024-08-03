"""This program covers the "Library" program with tests"""

import logging
import pytest
from homework.homework11.library import Books, User

# Configure logger
logger = logging.getLogger(__name__)


class TestLibrary:
    """Test class for testing Library class"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup and teardown for each test"""
        logger.info("Setting up test")
        yield
        logger.info("Tearing down test")

    @pytest.fixture
    def book(self):
        """Fixture for creating a book object"""
        return Books('The Lord of the Rings',
                     'J.R.R. Tolkien',
                     9785171358136,
                     1120)

    @pytest.fixture
    def user_vasya(self):
        """Fixture for creating the first user"""
        return User(name="Vasya")

    @pytest.fixture
    def user_petya(self):
        """Fixture for creating a second user"""
        return User(name="Petya")

    def test_book_attributes_positive(self, book):
        """Testing Positive Scenarios for Verifying Book Attributes"""
        logger.info("Testing positive book attributes...")
        assert book.book_name == 'The Lord of the Rings'
        assert book.author == 'J.R.R. Tolkien'
        assert book.isbn == 9785171358136
        assert book.page_count == 1120
        assert not book.reserved
        assert not book.busy
        assert book.reserved_by is None

    def test_book_attributes_negative(self, book):
        """Testing Negative Scenarios for Verifying Book Attributes"""
        logger.info("Testing negative book attributes...")
        assert book.book_name != 'The Hobbit'
        assert book.author != 'George R.R. Martin'
        assert book.isbn != 1234567890123
        assert book.page_count != 0
        assert not book.reserved
        assert not book.busy
        assert book.reserved_by is None

    def test_book_reserved_attribute(self, book, user_vasya):
        """Testing changing the reserved attribute of a book when booking"""
        logger.info("Testing book reserved attribute...")
        user_vasya.reserve_book(book)
        assert book.reserved
        assert book.reserved_by == user_vasya.name

    def test_book_reserved_by_attribute(self, book, user_vasya):
        """Тестирование изменения атрибута reserved_by книги при возврате"""
        logger.info("Testing book reserved_by attribute...")
        user_vasya.take_book(book)
        user_vasya.return_book(book)
        assert book.reserved_by is None

    def test_book_busy_attribute(self, book, user_vasya):
        """Testing changing the book's busy attribute upon receipt"""
        logger.info("Testing book busy attribute...")
        user_vasya.take_book(book)
        assert book.busy

    def test_attributes_is_none(self, book, user_vasya, user_petya):
        """Testing detection of None objects"""
        logger.info("Testing return of a reserved book...")
        try:
            if book is None or user_vasya is None or user_petya is None:
                raise ValueError("One of the objects is None")
        except Exception as e:
            logger.error(f"Test failed: {str(e)}")
            raise

    def test_book_return_clears_attributes(self, book, user_vasya):
        """Testing book attributes reset when returned"""
        logger.info("Testing book attributes reset on return...")
        user_vasya.take_book(book)
        user_vasya.return_book(book)
        assert not book.busy
        assert not book.reserved
        assert book.reserved_by is None

    def test_book_receiving(self, book, user_vasya, user_petya):
        """Testing the book retrieval function"""
        logger.info("Testing book receiving...")
        user_vasya.take_book(book)
        assert user_petya.take_book(book) == "busy_or_reserved_by_other"

    def test_book_reservation(self, book, user_vasya, user_petya):
        """Testing the book reservation function"""
        logger.info("Testing book reservation...")
        assert user_vasya.reserve_book(book) == "reserved"
        assert user_petya.reserve_book(book) == "already_reserved"

    def test_book_returning(self, book, user_vasya, user_petya):
        """Testing the book return function"""
        logger.info("Testing book returning...")
        user_vasya.take_book(book)
        assert user_vasya.return_book(book) == "returned"
        assert user_petya.take_book(book) == "taken"
        assert book.busy
        assert book.reserved_by == user_petya.name

    def test_reserved_book_receiving(self, book, user_vasya, user_petya):
        """Testing the function of obtaining a reserved book"""
        logger.info("Testing reserved book receiving...")
        user_vasya.reserve_book(book)
        assert user_petya.take_book(book) == "busy_or_reserved_by_other"
        assert user_vasya.take_book(book) == "taken"

    def test_reserved_book_returning(self, book, user_vasya, user_petya):
        """Testing the reserved book return function"""
        logger.info("Testing reserved book returning...")
        user_vasya.reserve_book(book)
        assert user_vasya.return_book(book) == "not_taken_by_user"
        assert user_petya.take_book(book) == "busy_or_reserved_by_other"
