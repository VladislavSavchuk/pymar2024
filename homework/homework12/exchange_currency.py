"""Bank deposit.
This program calculates the monthly capitalization of the user's deposit.
Converts the original amount to the target currency.
"""


class Bank:
    """Initialize bank deposit attributes"""
    def __init__(self, deposit_amount: float, period: int, rate: float):
        self.deposit_amount = deposit_amount  # starting deposit
        self.period = period  # period of the deposit in months
        self.rate = rate  # annual rate % divided by 100
        self.currency = Currency
        print('Deposit created')

    def calculate_monthly_capitalization(self):
        """This method calculates the monthly capitalization
        of the customer's amount"""
        result = round((self.deposit_amount * (1 + (self.rate / 100) / 12)
                        ** self.period), 2)

        return (f'Monthly capitalization of amount {self.deposit_amount}$ '
                f'for {self.period} months equals to {result}$')

    @staticmethod
    def exchange_currency(from_currency, amount, to_currency='BYN'):
        """This method return converted amount"""
        return currency.convert(from_currency, amount, to_currency)


class Customer:
    """Initialize customer's"""
    def __init__(self, name: str, curr: str, amount: float):
        """This method outputs the name, currency and
        amount of the bank's customer"""
        self.name = name
        self.currency = curr
        self.amount = amount


class Currency:
    """This class contains two methods: saving exchange rates,
    currency conversion"""
    def __init__(self):
        """This method stores exchange rates in the rates dictionary"""
        self.rates = {'USD': 3.19, 'EUR': 3.45, 'BYN': 1.0}

    def convert(self, from_currency, amount, to_currency='BYN'):
        """This method checks the current currency in list currency
        and then converts it"""
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Invalid currency")

        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]

        converted_amount = (amount / to_rate) * from_rate

        return round(converted_amount, 2), to_currency


person_1 = Customer('Lionel Messi', 'USD', 10)
person_2 = Customer('LeBron James', 'EUR', 5)
print(person_1.name)
deposit_person1 = Bank(1000000, 120, 10)
print(deposit_person1.calculate_monthly_capitalization())
print()
print(person_2.name)
deposit_person2 = Bank(999999.99, 60, 10)
print(deposit_person2.calculate_monthly_capitalization())

currency = Currency()

person_1 = Customer('Lionel', 'USD', 10)
person_2 = Customer('LeBron', 'EUR', 5)

assert (Bank.exchange_currency(person_1.currency, person_1.amount) ==
        (31.9, "BYN")), "Conversion error"
assert (Bank.exchange_currency(person_2.currency, person_2.amount) ==
        (17.25, "BYN")), "Conversion error"
assert (Bank.exchange_currency(person_1.currency, person_1.amount, 'EUR') ==
        (9.25, "EUR")), "Conversion error"
assert (Bank.exchange_currency(person_2.currency, person_2.amount, 'USD') ==
        (5.41, "USD")), "Conversion error"
