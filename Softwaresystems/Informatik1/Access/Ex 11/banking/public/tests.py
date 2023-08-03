from unittest import TestCase
from public.currency_converter import convert
from public.bank_account import BankAccount

class PrivateFunctionalTestSuite(TestCase):

    def test_0_convert(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)
        
    def test_1_basic_banking(self):
        sut = BankAccount("CHF")
        sut.deposit(100.0, "CHF")
        sut.withdraw(10.0, "EUR")
        actual = sut.get_balance()
        expected = 89.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_warnings(self):
        with self.assertRaises(Warning):
            acc = BankAccount("A")
        acc = BankAccount("USD")
        with self.assertRaises(Warning):
            acc.deposit("baum", "USD")
        with self.assertRaises(Warning):
            acc.deposit(-1, "USD")
        with self.assertRaises(Warning):
            acc.deposit(100, "A")
