#skipped bc of time reasons
import unittest

class MyTestSuite(unittest.TestCase):
    def test_less_than_three_chars(self):
        with self.assertRaises(TypeError):
            is_palindrome("mem")

