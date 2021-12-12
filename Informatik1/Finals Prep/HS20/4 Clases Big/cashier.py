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

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
assert(bottles[0].get_price() == 3.50)

c = Crate()
for b in bottles: c.add(b)
assert(c.get_size() == 5)
assert(c.get_price() == 20.00)

c = FixedPriceCrate(11.11)
for b in bottles: c.add(b)
assert(c.get_price() == 11.11)

c = DiscountCrate()
for b in bottles: c.add(b)
assert(c.get_price() == 18.00)

unittest.main()