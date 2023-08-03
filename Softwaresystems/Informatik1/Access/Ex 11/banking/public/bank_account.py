from public.currency_converter import convert
from public.exchange_rates import EXCHANGE_RATES as er

class BankAccount:

    def __init__(self, currency="CHF"):
        if currency not in er: raise Warning('invalid currency')
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        try: convert(amount, currency, currency)
        except Warning: raise Warning
        self.__balance += convert(amount, currency, self.__currency)
    
    def withdraw(self, amount, currency="CHF"):
        try: convert(amount, currency, currency)
        except Warning: raise Warning
        if self.get_balance() < convert(amount, currency, self.__currency):
            raise Warning('insufficient funds')
        self.__balance -= convert(amount, currency, self.__currency)
