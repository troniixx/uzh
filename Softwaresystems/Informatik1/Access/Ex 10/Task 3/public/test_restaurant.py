#!/usr/bin/env python3

from unittest import TestCase
from onsite_restaurant import OnsiteRestaurant
from delivery_restaurant import DeliveryRestaurant
from restaurant import Restaurant

class RestaurantTest(TestCase):

    def test_restaurant_sales(self):
        r = Restaurant("Random Restaurant", "Mixed Cuisine")
        r.add_consumption_unit("Caesar Salad", 15)
        r.open_restaurant()
        r.sell_unit("Caesar Salad")
        r.sell_unit("Caesar Salad")
        self.assertEqual(30, r.get_sales())

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
