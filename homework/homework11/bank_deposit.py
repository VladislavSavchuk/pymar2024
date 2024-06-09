"""Bank deposit.
This program calculates the monthly capitalization of the user's deposit.
"""


class Bank:
    """Initialize bank deposit attributes"""
    def __init__(self, deposit_amount: float, period: int, rate: float):
        self.deposit_amount = deposit_amount  # starting deposit
        self.period = period  # period of the deposit in months
        self.rate = rate  # annual rate % divided by 100
        print('Deposit created')

    def calculate_monthly_capitalization(self):
        """This method calculates the monthly capitalization
        of the customer's amount"""
        result = round((self.deposit_amount * (1 + (self.rate / 100) / 12)
                        ** self.period), 2)
        return (f'Monthly capitalization of amount {self.deposit_amount}$ '
                f'for {self.period} months equals to {result}$')


class Customer:
    """Initialize customer's"""
    def __init__(self, name):
        """This method outputs the name of the bank's customer"""
        self.name = name

    @staticmethod
    def create_deposit(deposit_amount: float, period: int, rate: float) -> str:
        """This method creates a deposit and calculates
        monthly capitalization"""
        deposit = Bank(deposit_amount, period, rate)
        return deposit.calculate_monthly_capitalization()


person_1 = Customer('Lionel Messi')
person_2 = Customer('LeBron James')
print(person_1.name)
print(person_1.create_deposit(1000000, 120, 10))
print()
print(person_2.name)
print(person_2.create_deposit(999999.99, 60, 10))
