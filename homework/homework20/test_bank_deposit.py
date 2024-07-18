"""This program covers the "Bank Deposit" program with tests"""

import unittest
import datetime
from loguru import logger
from homework.homework11.bank_deposit import Bank, Customer

# Configure logger
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logger.add(f'logs/{current_time}_test_bank_deposit.log',
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
                  "{file}:{line} | {message}",
           level='INFO')


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
        logger.info("Testing Bank attributes")

        bank = Bank(1500, 24, 3.5)
        assert bank.deposit_amount == 1500, \
            f"Expected deposit_amount to be 1500, got {bank.deposit_amount}"
        assert bank.period == 24, \
            f"Expected period to be 24, got {bank.period}"
        assert bank.rate == 3.5, \
            f"Expected rate to be 3.5, got {bank.rate}"

        logger.info("Successfully verified bank attributes")

    def test_calculate_monthly_capitalization(self):
        """Test the calculation of monthly capitalization."""
        logger.info("Testing calculation of monthly capitalization")

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
        logger.info("Testing calculation of monthly capitalization with"
                    " zero in deposit, period and rate""")

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
        logger.info("Testing negative calculation of monthly capitalization""")

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
        logger.info("Testing Customer name")

        customer = Customer('LeBron James')
        self.assertEqual(customer.name, 'LeBron James')

    def test_customer_initialization_negative(self):
        """Test negative case for initialization of the Customer class."""
        logger.info("Testing negative Customer name")

        customer = Customer('LeBron James')
        self.assertNotEqual(customer.name, 'LaBron James')

    def test_customer_name_update(self):
        """Test updating the name attribute of the Customer class."""
        logger.info("Testing updating Customer name")

        customer = Customer('LeBron James')
        customer.name = 'Kobe Bryant'
        self.assertEqual(customer.name, 'Kobe Bryant')


if __name__ == '__main__':
    unittest.main()
