#!/usr/bin/env python3
from unittest import TestCase
from public.script import calculate_factorial

class MyTests(TestCase):

    # write here your tests for calculate_factorial
    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-10)

    def test_invalid_negative_str(self):
        with self.assertRaises(ValueError):
            calculate_factorial("-10")

    def test_zero(self):
        expected = 1
        actual = calculate_factorial(0)
        self.assertEqual(expected,actual)

    def test_zero_str(self):
        expected = 1
        actual = calculate_factorial("0")
        self.assertEqual(expected,actual)

    def test_invalid_too_big(self):
        with self.assertRaises(ValueError):
            calculate_factorial(11)

    def test_invalid_too_big_str(self):
        with self.assertRaises(ValueError):
            calculate_factorial("12")
    
    def test_invalid_string(self):
        with self.assertRaises(TypeError):
            calculate_factorial("abcdefg")

    def test_none(self):
        expected = None
        actual = calculate_factorial(None)
        self.assertEqual(expected,actual)
    
    def test_five(self):
        expected = 120
        actual = calculate_factorial(5)
        self.assertEqual(expected,actual)

    def test_five_str(self):
        expected = 120
        actual = calculate_factorial("5")
        self.assertEqual(expected,actual)

    def test_ten(self):
        expected = 3628800
        actual = calculate_factorial(10)
        self.assertEqual(expected,actual)

    def test_ten_str(self):
        expected = 3628800
        actual = calculate_factorial("10")
        self.assertEqual(expected,actual)
    
    
    
    #pass
