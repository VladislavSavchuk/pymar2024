"""Bank deposit.
This program calculates the monthly capitalization of the user's deposit.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s')


class Bank:
    """Initialize bank deposit attributes"""
    def __init__(self, deposit_amount: float, period: int, rate: float):
        self.deposit_amount = deposit_amount  # starting deposit
        self.period = period  # period of the deposit in months
        self.rate = rate  # annual rate % divided by 100

    def __str__(self):
        return (f"Deposit created. Amount: {self.deposit_amount}$, "
                f"period: {self.period} month, rate: {self.rate}%")

    def calculate_monthly_capitalization(self):
        """This method calculates the monthly capitalization
        of the customer's amount"""
        result = round((self.deposit_amount * (1 + (self.rate / 100) / 12)
                        ** self.period), 2)
        return result


class Customer:
    """Initialize customer's"""
    def __init__(self, name: str):
        """This method outputs the name of the bank's customer"""
        self.name = name


if __name__ == "__main__":
    person_1 = Customer('Lionel Messi')
    person_2 = Customer('LeBron James')

    logging.info(f'Customer created: {person_1.name}')
    deposit_person1 = Bank(1000000, 120, 10)
    logging.info(deposit_person1)
    logging.info(f'Monthly capitalization: '
                 f'{deposit_person1.calculate_monthly_capitalization()}')

    logging.info(f'Customer created: {person_2.name}')
    deposit_person2 = Bank(999999.99, 60, 10)
    logging.info(deposit_person2)
    logging.info(f'Monthly capitalization: '
                 f'{deposit_person2.calculate_monthly_capitalization()}')
