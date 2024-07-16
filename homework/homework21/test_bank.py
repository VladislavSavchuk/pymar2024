"""This program covers the "Bank Deposit" program with tests"""

import datetime
import pytest
from loguru import logger
from homework.homework11.bank_deposit import Bank, Customer

# Configure logger
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logger.add(f'logs/{current_time}_test_bank_deposit.log',
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
                  "{file}:{line} | {message}",
           level='INFO')


class TestBankPositive:
    """Positive tests for bank deposit"""
    def test_bank_positive(self):
        """"""
        bank = Bank(deposit_amount=1000, period=12, rate=5)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 1051.16

    def test_bank_positive_large_amount(self):
        """"""
        bank = Bank(deposit_amount=100000, period=24, rate=3)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 106175.7

    def test_bank_positive_no_interest(self):
        """"""
        bank = Bank(deposit_amount=500, period=6, rate=0)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 500.0

    def test_bank_positive_short_period(self):
        """"""
        bank = Bank(deposit_amount=1000, period=1, rate=12)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankPositive: Calculated result: {result}")
        assert result == 1010.0


class TestBankNegative:
    """Negative tests for bank deposit"""
    def test_bank_negative(self):
        """"""
        bank = Bank(deposit_amount=1000, period=12, rate=5)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankNegative: Calculated result: {result}")
        assert result != 1100

    def test_bank_negative_large_amount(self):
        """"""
        bank = Bank(deposit_amount=100000, period=24, rate=3)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankNegative: Calculated result: {result}")
        assert result != 107000

    def test_bank_negative_no_interest(self):
        """"""
        bank = Bank(deposit_amount=500, period=6, rate=0)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankNegative: Calculated result: {result}")
        assert result == 500.0

    def test_bank_negative_short_period(self):
        """"""
        bank = Bank(deposit_amount=1000, period=1, rate=12)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankNegative: Calculated result: {result}")
        assert result == 1010.0


class TestBankBoundary:
    """Boundary tests for bank deposit"""
    def test_bank_boundary_zero_amount(self):
        """"""
        bank = Bank(deposit_amount=0, period=12, rate=5)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankBoundary: Calculated result: {result}")
        assert result == 0

    def test_bank_boundary_zero_period(self):
        """"""
        bank = Bank(deposit_amount=1000, period=0, rate=5)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankBoundary: Calculated result: {result}")
        assert result == 1000

    def test_bank_boundary_zero_rate(self):
        """"""
        bank = Bank(deposit_amount=1000, period=12, rate=0)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankBoundary: Calculated result: {result}")
        assert result == 1000

    def test_bank_boundary_high_rate(self):
        """"""
        bank = Bank(deposit_amount=1000, period=12, rate=100)
        result = bank.calculate_monthly_capitalization()
        logger.info(f"TestBankBoundary: Calculated result: {result}")
        assert result == 2613.04


class TestBankInvalid:
    """Invalid tests for bank deposit"""
    def test_bank_invalid_negative_amount(self):
        """"""
        with pytest.raises(ValueError):
            logger.info("TestBankInvalid: Creating bank with negative amount")
            Bank(deposit_amount=-1000, period=12, rate=5)

    def test_bank_invalid_negative_period(self):
        """"""
        with pytest.raises(ValueError):
            logger.info("TestBankInvalid: Creating bank with negative period")
            Bank(deposit_amount=1000, period=-12, rate=5)

    def test_bank_invalid_negative_rate(self):
        """"""
        with pytest.raises(ValueError):
            logger.info("TestBankInvalid: Creating bank with negative rate")
            Bank(deposit_amount=1000, period=12, rate=-5)


class TestCustomer:
    """Customer tests"""
    def test_customer_creation(self):
        """"""
        customer = Customer(name="Lionel Messi")
        logger.debug(f"TestCustomer: Created customer with name: "
                     f"{customer.name}")
        assert customer.name == "Lionel Messi"

    def test_customer_creation_empty_name(self):
        """"""
        customer = Customer(name="")
        logger.debug("TestCustomer: Created customer with empty name")
        assert customer.name == ""

    def test_customer_creation_special_characters(self):
        """"""
        customer = Customer(name="@#!$%^&*()")
        logger.debug(f"TestCustomer: Created customer with special "
                     f"characters: {customer.name}")
        assert customer.name == "@#!$%^&*()"

    def test_customer_creation_long_name(self):
        """"""
        long_name = "a" * 256
        customer = Customer(name=long_name)
        logger.debug(f"TestCustomer: Created customer with "
                     f"long name: {customer.name}")
        assert customer.name == long_name
