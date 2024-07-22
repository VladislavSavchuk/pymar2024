"""This file contains the keywords for the library."""


import logging
from robot.api.deco import keyword
from homework.homework11.bank_deposit import Bank, Customer

logger = logging.getLogger(__name__)


@keyword
def create_bank_instance(deposit_amount, period, rate):
    """Create an instance of the Bank class."""
    return Bank(deposit_amount, period, rate)


@keyword
def calculate_monthly_capitalization(bank):
    """Calculate the monthly capitalization for a given bank instance."""
    return bank.calculate_monthly_capitalization()


@keyword
def create_customer_instance(name):
    """Create an instance of the Customer class."""
    return Customer(name)


@keyword
def log_message(message):
    """Log a message."""
    logger.info(message)
