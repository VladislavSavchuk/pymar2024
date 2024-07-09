"""This program covers the "Bank Deposit" program with tests"""

import logging
import unittest
from bank_deposit import Bank, Customer

# Configure logger
logging.basicConfig(filename='test_app.log',
                    filemode='w',
                    encoding='utf-8',
                    format="%(asctime)s - %(name)s - %(levelname)s - "
                           "%(message)s",
                    level=logging.INFO
                    )

logger = logging.getLogger(__name__)


class TestBank(unittest.TestCase):
    """Test cases for the Bank class."""

    def setUp(self):
        """Set up logging before each test case."""
        logger.info("Starting a test case Bank")

    def tearDown(self):
        """Log after each test case."""
        logger.info("Finished a test case Bank")

    def test_bank_initialization(self):
        """Test initialization of the Bank class."""

        bank = Bank(1500, 24, 3.5)
        self.assertEqual(bank.deposit_amount, 1500)
        self.assertEqual(bank.period, 24)
        self.assertEqual(bank.rate, 3.5)

    def test_calculate_monthly_capitalization(self):
        """Test the calculation of monthly capitalization."""

        bank = Bank(1500, 24, 3.5)
        result = bank.calculate_monthly_capitalization()
        self.assertEqual(result, 1608.6)

        bank = Bank(5000, 36, 4)
        result = bank.calculate_monthly_capitalization()
        self.assertEqual(result, 5636.36)

        bank = Bank(20000, 48, 5)
        result = bank.calculate_monthly_capitalization()
        self.assertEqual(result, 24417.91)

    def test_calculate_monthly_capitalization_edge_cases(self):
        """Test edge cases for monthly capitalization calculation."""

        # Test with zero deposit amount
        bank = Bank(0, 12, 5)
        result = bank.calculate_monthly_capitalization()
        self.assertEqual(result, 0.0)

        # Test with zero period
        bank = Bank(1000, 0, 5)
        result = bank.calculate_monthly_capitalization()
        self.assertEqual(result, 1000.0)

        # Test with zero rate
        bank = Bank(1000, 12, 0)
        result = bank.calculate_monthly_capitalization()
        self.assertEqual(result, 1000.0)

    def test_calculate_monthly_capitalization_negative(self):
        """Test negative cases for monthly capitalization calculation."""

        bank = Bank(1500, 24, 3.5)
        result = bank.calculate_monthly_capitalization()
        self.assertNotEqual(result, 1500)

        bank = Bank(5000, 36, 4)
        result = bank.calculate_monthly_capitalization()
        self.assertNotEqual(result, 5000)


class TestCustomer(unittest.TestCase):
    """Test cases for the Customer class."""

    def setUp(self):
        """Set up logging before each test case."""
        logger.info("Starting a test case Customer")

    def tearDown(self):
        """Log after each test case."""
        logger.info("Finished a test case Customer")

    def test_customer_initialization(self):
        """Test initialization of the Customer class."""

        customer = Customer('LeBron James')
        self.assertEqual(customer.name, 'LeBron James')

    def test_customer_initialization_negative(self):
        """Test negative case for initialization of the Customer class."""

        customer = Customer('LeBron James')
        self.assertNotEqual(customer.name, 'LaBron James')

    @unittest.expectedFailure
    def test_customer_name_update(self):
        """Test updating the name attribute of the Customer class."""

        customer = Customer('LeBron James')
        customer.name = 'Koba Bryant'
        self.assertEqual(customer.name, 'Kobe Bryant')


if __name__ == '__main__':
    unittest.main()
