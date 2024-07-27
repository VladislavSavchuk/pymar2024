"""This program covers the "Bank Deposit" program with tests"""

import pytest
from logger_config import configure_logger
from homework.homework11.bank_deposit import Bank, Customer

# Name of the module used for logging
module_name = __name__

# Configure logger
logger = configure_logger(module_name)


@pytest.mark.positive
class TestBankPositive:
    """Positive tests for bank deposit"""

    @pytest.fixture
    def bank_1000_12_5(self):
        """Fixture for bank deposit"""
        return Bank(deposit_amount=1000, period=12, rate=5)

    @pytest.fixture
    def bank_100000_24_3(self):
        """Fixture for bank deposit with large amount"""
        return Bank(deposit_amount=100000, period=24, rate=3)

    @pytest.fixture
    def bank_1000_1_12(self):
        """Fixture for bank deposit with short period"""
        return Bank(deposit_amount=1000, period=1, rate=12)

    @pytest.fixture
    def bank_1000_12_100(self):
        """Fixture for bank deposit with high rate"""
        return Bank(deposit_amount=1000, period=12, rate=100)

    def test_bank_positive(self, bank_1000_12_5):
        """Positive test for bank deposit"""
        result = bank_1000_12_5.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 1051.16

    def test_bank_positive_large_amount(self, bank_100000_24_3):
        """Positive test with large amount"""
        result = bank_100000_24_3.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 106175.7

    def test_bank_positive_short_period(self, bank_1000_1_12):
        """Positive test with short period"""
        result = bank_1000_1_12.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 1010.0

    def test_bank_positive_high_rate(self, bank_1000_12_100):
        """Positive test with high rate"""
        result = bank_1000_12_100.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 2613.04


@pytest.mark.boundary
class TestBankBoundary:
    """Boundary tests for bank deposit"""

    @pytest.mark.parametrize("deposit, period, rate, expected", [
        (0, 12, 5, 0.0),  # Test with zero deposit amount
        (1000, 0, 5, 1000.0),  # Test with zero period
        (1000, 12, 0, 1000.0)  # Test with zero rate
    ])
    def test_bank_boundary_zero_amount(self, deposit, period, rate, expected):
        """Boundary test for zero amount, period and rate"""
        bank = Bank(deposit_amount=deposit, period=period, rate=rate)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"Test result: deposit={deposit}, period={period}, "
                    f"rate={rate} => result={result}")
        assert result == expected, f"Expected {expected}, got {result}"


@pytest.mark.invalid
class TestBankInvalid:
    """Invalid tests for bank deposit"""

    def test_bank_invalid_negative_amount(self):
        """Test with negative amount"""
        with pytest.raises(ValueError):
            logger.info("TestBankInvalid: Creating bank with "
                        "negative amount")
            Bank(deposit_amount=-1000, period=12, rate=5)

    def test_bank_invalid_negative_period(self):
        """Test with negative period"""
        with pytest.raises(ValueError):
            logger.info("TestBankInvalid: Creating bank with "
                        "negative period")
            Bank(deposit_amount=1000, period=-12, rate=5)

    def test_bank_invalid_negative_rate(self):
        """Test with negative rate"""
        with pytest.raises(ValueError):
            logger.info("TestBankInvalid: Creating bank with "
                        "negative rate")
            Bank(deposit_amount=1000, period=12, rate=-5)

    def test_bank_invalid_type_attribute(self):
        """Test with invalid type for deposit amount"""
        with pytest.raises(TypeError):
            logger.info("TestBankNegative: Creating bank with invalid "
                        "amount type")
            bank = Bank(deposit_amount="one thousand", period=12, rate=5)
            bank.calculate_monthly_capitalization()


@pytest.mark.customer
class TestCustomer:
    """Customer tests"""

    def test_customer_creation(self):
        """Test creating a customer with a valid name"""
        customer = Customer(name="Lionel Messi")
        logger.info(f"TestCustomer: Created customer with name: "
                    f"{customer.name}")
        assert customer.name == "Lionel Messi"

    def test_customer_creation_empty_name(self):
        """Test creating a customer with an empty name"""
        with pytest.raises(ValueError):
            logger.info("TestCustomer: Trying to create customer with "
                        "empty name")
            Customer(name="")

    def test_customer_creation_special_characters(self):
        """Test creating a customer with special characters in the name"""
        with pytest.raises(ValueError):
            logger.info("TestCustomer: Trying to create customer with "
                        "special characters in the name")
            Customer(name="@#!$%^&*()")

    def test_customer_creation_long_name(self):
        """Test creating a customer with a very long name"""
        long_name = "a" * 256
        with pytest.raises(ValueError):
            logger.info("TestCustomer: Trying to create customer with "
                        "long name")
            Customer(name=long_name)
