#!/usr/bin/env python3

import unittest

class MyTestSuite(unittest.TestCase):
    def test_len_3(self):
        self.assertTrue(is_palindrome("bob"))

    def test_len_less_than_3_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.assertTrue(is_palindrome("aa"))

    def test_basic(self):
        self.assertTrue(is_palindrome("atoyota"))

    def test_with_nonalpha(self):
        self.assertTrue(is_palindrome("a toyota!"))

    def test_with_mixed_casing(self):
        self.assertTrue(is_palindrome("AToyoTa"))

    def test_false(self):
        self.assertFalse(is_palindrome("Honda"))

    def test_rejects_non_string(self):
        with self.assertRaises(TypeError):
            is_palindrome(True)