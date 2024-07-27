"""This program covers the "Library" program with tests"""

import pytest
from logger_config import configure_logger
from homework.homework11.library import Books, User

# Configure logger
logger = configure_logger(__name__)


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
    def user1(self):
        """Fixture for creating the first user"""
        return User()

    @pytest.fixture
    def user2(self):
        """Fixture for creating a second user"""
        return User()

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
        assert book.reserved is False
        assert book.busy is False
        assert book.reserved_by != ""

    def test_book_reserved_attribute(self, book, user1):
        """Testing changing the reserved attribute of a book when booking"""
        logger.info("Testing book reserved attribute...")
        user1.reserve_book(book)
        assert book.reserved
        assert book.reserved_by == user1

    def test_book_reserved_by_attribute(self, book, user1):
        """Тестирование изменения атрибута reserved_by книги при возврате"""
        logger.info("Testing book reserved_by attribute...")
        user1.take_book(book)
        user1.return_book(book)
        assert book.reserved_by is None

    def test_book_busy_attribute(self, book, user1):
        """Testing changing the book's busy attribute upon receipt"""
        logger.info("Testing book busy attribute...")
        user1.take_book(book)
        assert book.busy

    def test_attributes_is_none(self, book, user1, user2):
        """Testing detection of None objects"""
        logger.info("Testing return of a reserved book...")
        try:
            if book is None or user1 is None or user2 is None:
                raise ValueError("One of the objects is None")
        except Exception as e:
            logger.error(f"Test failed: {str(e)}")
            raise

    def test_book_return_clears_attributes(self, book, user1):
        """Testing book attributes reset when returned"""
        logger.info("Testing book attributes reset on return...")
        user1.take_book(book)
        user1.return_book(book)
        assert not book.busy
        assert not book.reserved
        assert book.reserved_by is None

    def test_book_receiving(self, book, user1, user2):
        """Testing the book retrieval function"""
        logger.info("Testing book receiving...")
        assert user1.take_book(book)
        assert user2.take_book(book) == "taken"

    def test_book_reservation(self, book, user1, user2):
        """Testing the book reservation function"""
        logger.info("Testing book reservation...")
        assert user1.reserve_book(book)
        assert user2.reserve_book(book) == "reserved"

    def test_book_returning(self, book, user1, user2):
        """Testing the book return function"""
        logger.info("Testing book returning...")
        user1.take_book(book)
        assert user1.return_book(book) == "returned"
        assert user2.take_book(book)

    def test_reserved_book_receiving(self, book, user1, user2):
        """Testing the function of obtaining a reserved book"""
        logger.info("Testing reserved book receiving...")
        user1.reserve_book(book)
        assert user2.take_book(book) == "reserved_by_other"
        assert user1.take_book(book)

    def test_reserved_book_returning(self, book, user1, user2):
        """Testing the reserved book return function"""
        logger.info("Testing reserved book returning...")
        user1.reserve_book(book)
        assert user1.return_book(book) == "reserve_cancelled"
        assert user2.take_book(book)
