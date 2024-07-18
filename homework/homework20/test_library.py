"""This program covers the "Library" program with tests"""

import unittest
import datetime
from loguru import logger
from homework.homework11.library import Books, User

# Configure logger
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logger.add(f'logs/{current_time}_test_library.log',
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
                  "{file}:{line} | {message}",
           level='INFO')


class TestBooks(unittest.TestCase):
    """Testing the Books class"""

    def setUp(self):
        """Set up logging before each test case."""
        logger.info("Starting a test case Book")

        self.book = Books('The Lord of the Rings', 'J.R.R. Tolkien',
                          9785171358136, 1120)
        self.user1 = User()
        self.user2 = User()

    def tearDown(self):
        """Log after each test case."""
        logger.info("Finished a test case Book")

    def test_book_initialization(self):
        """Testing book attributes"""
        logger.info("Testing book attributes")

        self.assertEqual(self.book.book_name, 'The Lord of the Rings')
        self.assertEqual(self.book.author, 'J.R.R. Tolkien')
        self.assertEqual(self.book.isbn, 9785171358136)
        self.assertEqual(self.book.page_count, 1120)
        self.assertFalse(self.book.reserved)
        self.assertFalse(self.book.busy)
        self.assertIsNone(self.book.reserved_by)

    def test_book_reservation(self):
        """Book reservation testing"""
        logger.info("Book reservation testing")

        result = self.user1.reserve_book(self.book)
        logger.info("User 1 reserves a book: %s" % result)
        self.assertEqual(result, True)
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, self.user1)

        result = self.user2.reserve_book(self.book)
        logger.info("User 2 trying reserves a book: %s" % result)
        self.assertEqual(result, "reserved", )
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, self.user1)

    def test_book_receiving(self):
        """Testing getting a book"""
        logger.info("Testing getting a book")

        result = self.user1.take_book(self.book)
        logger.info("User 1 takes a book: %s" % result)
        self.assertEqual(result, True)
        self.assertTrue(self.book.busy)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

        result = self.user2.take_book(self.book)
        logger.info("User 2 tries to take a book: %s" % result)
        self.assertEqual(result, "taken")
        self.assertTrue(self.book.busy)

    def test_book_returning(self):
        """Testing book returns"""
        logger.info("Testing book returns")

        self.user1.take_book(self.book)
        result = self.user1.return_book(self.book)
        logger.info("User 1 returns a book: %s" % result)
        self.assertEqual(result, "returned")
        self.assertFalse(self.book.busy)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_reserve_and_take(self):
        """Testing reserving and receiving book"""
        logger.info("Testing reserving and receiving book")

        self.user1.reserve_book(self.book)
        result = self.user1.take_book(self.book)
        logger.info("User 1 reserves and takes a book: %s" % result)
        self.assertEqual(result, True)
        self.assertTrue(self.book.busy)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_invalid_return(self):
        """Testing the return of a book that has not been taken"""
        logger.info("Testing the return of a book that has not been taken")

        result = self.user1.return_book(self.book)
        logger.info("User 1 is trying to return a book: %s" % result)
        self.assertEqual(result, "free")
        self.assertFalse(self.book.busy)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_cancel_reservation(self):
        """Reservation cancellation testing"""
        logger.info("Reservation cancellation testing")

        self.user1.reserve_book(self.book)
        result = self.user1.return_book(self.book)
        logger.info("User 1 cancels a book reservation: %s" % result)
        self.assertEqual(result, "reserve_cancelled")
        self.assertFalse(self.book.busy)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_reserved_by_other_user(self):
        """Testing an attempt to take a book reserved by another user"""
        logger.info("Testing an attempt to take a book reserved "
                    "by another user")

        self.user1.reserve_book(self.book)
        result = self.user2.take_book(self.book)
        logger.info("User 2 is trying to take a reserved book: %s" % result)
        self.assertEqual(result, "reserved_by_other")
        self.assertFalse(self.book.busy)
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, self.user1)

    def test_double_reservation_by_same_user(self):
        """Testing double reservations of the same book by a user"""
        logger.info("Testing double reservations of the same book by a user")

        result = self.user1.reserve_book(self.book)
        logger.info("First reservation by user 1: %s" % result)
        self.assertEqual(result, True)

        result = self.user1.reserve_book(self.book)
        logger.info("Re-booking by user 1: %s" % result)
        self.assertEqual(result, "reserved")
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, self.user1)

    def test_take_reserved_book_by_reserver(self):
        """Testing the receipt of a reserved book by the same user"""
        logger.info("Testing the receipt of a reserved book by the same user")

        self.user1.reserve_book(self.book)
        result = self.user1.take_book(self.book)
        logger.info("User 1 takes a reserved book: %s" % result)
        self.assertEqual(result, True)
        self.assertTrue(self.book.busy)
        self.assertFalse(self.book.reserved)
        self.assertIsNone(self.book.reserved_by)

    def test_take_reserved_book_by_another_user(self):
        """Testing an attempt to take a book reserved by another user"""
        logger.info("Testing an attempt to take a book reserved "
                    "by another user")

        self.user1.reserve_book(self.book)
        result = self.user2.take_book(self.book)
        logger.info("User 2 is trying to take a reserved book: %s" % result)
        self.assertEqual(result, "reserved_by_other")
        self.assertFalse(self.book.busy)
        self.assertTrue(self.book.reserved)
        self.assertEqual(self.book.reserved_by, self.user1)


if __name__ == '__main__':
    unittest.main()
