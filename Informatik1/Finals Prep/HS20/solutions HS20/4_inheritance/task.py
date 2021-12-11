#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

from abc import ABC, abstractmethod
import unittest

class Product:
	pass

class Bottle:
	pass

class Crate:
	pass

class DiscountCrate:
	pass

class FixedPriceCrate:
	pass

class ShopTestSuite(unittest.TestCase):

	def test_crate_add(self):
		c = Crate()
		c.add(Bottle(4.50, "Light Beer"))
		self.assertEqual(c.get_size(), 1)

	def test_crate_max_size(self):
		pass

	def test_crate_price(self):
		pass

	def test_discount_crate_price(self):
		pass

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

