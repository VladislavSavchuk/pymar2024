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
    def __init__(self, name: str):
        """This method outputs the name of the bank's customer"""
        self.name = name


person_1 = Customer('Lionel Messi')
person_2 = Customer('LeBron James')
print(person_1.name)
deposit_person1 = Bank(1000000, 120, 10)
print(deposit_person1.calculate_monthly_capitalization())
print()
print(person_2.name)
deposit_person2 = Bank(999999.99, 60, 10)
print(deposit_person2.calculate_monthly_capitalization())
