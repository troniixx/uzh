from accounting import BankAccount
import unittest
from unittest import TestCase

class BankAccountTest(TestCase):

    def test_balance(self):
        acc = BankAccount(100)
        self.assertEqual(acc.balance(), 0)
    
    def test_available(self):
        acc = BankAccount(100)
        self.assertEqual(acc.available(), 100)

    def test_deposit(self):
        acc = BankAccount(12)
        acc.deposit(23)
        self.assertEqual(acc.balance(), 23)

    def test_withdraw(self):
        acc = BankAccount(12)
        acc.withdraw(3)
        self.assertEqual(acc.balance(), -3)

    def test__fail_negative_limit(self):
        with self.assertRaises(AssertionError):
            BankAccount(-1)

    def test__fail_negative_deposit(self):
        acc = BankAccount(0)
        with self.assertRaises(AssertionError):
            acc.deposit(-1)

    def test__fail_negative_withdraw(self):
        acc = BankAccount(0)
        with self.assertRaises(AssertionError):
            acc.withdraw(-1)

    def test__fail_too_big_withdraw(self):
        acc = BankAccount(10)
        with self.assertRaises(AssertionError):
            acc.withdraw(11)