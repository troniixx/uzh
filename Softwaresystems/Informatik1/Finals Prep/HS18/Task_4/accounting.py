class BankAccount():
    def __init__(self, limit):
        assert limit >= 0
        self.bal = 0
        self.limit = limit
        

    def balance(self):
        return self.bal

    def deposit(self, amount):
        if amount > 0:
            self.bal += amount

    def withdraw(self, amount):
        assert amount > 0
        assert amount <= self.available()
        self.bal -= amount

    def available(self):
        return self.limit + self.bal

if __name__ == '__main__':
    # example usage
    acc = BankAccount(100)
    print(acc.balance()) # prints ’0’
    print(acc.available()) # prints ’100’
    acc.deposit(30) # balance: 30, available: 130 (illustration, no "print")
    acc.withdraw(40) # balance: -10, available: 90 (illustration, no "print")
    acc.withdraw(91) # AssertionError