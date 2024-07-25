"""This file contains the keywords for the library."""

from robot.api.deco import keyword
from homework.homework11.bank_deposit import Bank, Customer
from logger_config import configure_logger

# Create and configure the logger
loger = configure_logger(__name__)


@keyword
def create_bank_instance(deposit_amount, period, rate):
    """Create an instance of the Bank class."""
    loger.info(f'Creating Bank instance with '
               f'deposit_amount={deposit_amount}, '
               f'period={period}, rate={rate}')
    bank = Bank(deposit_amount, period, rate)
    loger.info(f'Created Bank instance: {bank}')
    return bank


@keyword
def calculate_monthly_capitalization(bank):
    """Calculate the monthly capitalization for a given bank instance."""
    loger.info(f'Calculating monthly capitalization for '
               f'bank instance: {bank}')
    result = bank.calculate_monthly_capitalization()
    loger.info(f'Calculated monthly capitalization: {result}')
    return result


@keyword
def create_customer_instance(name):
    """Create an instance of the Customer class."""
    loger.info(f'Creating Customer instance with name={name}')
    customer = Customer(name)
    loger.info(f'Created Customer instance: {customer}')
    return customer
