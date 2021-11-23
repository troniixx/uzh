#!/usr/bin/env python3

from unittest import TestCase
from public.shop import Shop
from public.clothing_store import ClothingStore
from public.bakery import Bakery

class TestShops(TestCase):

    def test_bakery_loan(self):
        bakery = Bakery(1000)
        bakery.take_loan(0.1, 1000)
        actual = bakery.pay_rent_and_loan(100)
        self.assertEqual(280.0, actual)

    def test_bakery_already_has_a_loan(self):
        bakery = Bakery(1000)
        bakery.take_loan(0.1, 1000)
        try:
            bakery.take_loan(0.05, 1000)
        except Warning:
            pass
        except:
            self.fail("Wrong error raised")
        else:
            self.fail("No warning raised")

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.