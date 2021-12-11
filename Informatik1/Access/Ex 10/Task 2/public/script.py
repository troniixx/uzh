#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from public.bakery import Bakery
from public.clothing_store import ClothingStore
from public.shopping_center import ShoppingCenter

bakery = Bakery(1000) # (capital, loan, interest, initial_loan_amount, dough, bread) = (1000, 0, 0, 0, 0, 0)
bakery.take_loan(0.1, 1000) # (2000, 1000, 0.1, 1000, 0, 0)
amount_paid_b = bakery.pay_rent_and_loan(100) # (1720.0, 900, 0.1, 1000, 0, 0)
bakery.procure(1, 100) # (1620.0, 900, 0.1, 1000, 100, 0)
bakery.produce(1) # (1520.0, 900, 0.1, 1000, 0, 100)
bakery.sell(6, 50) # (1745.0, 900, 0.1, 1000, 0, 50)
try:
    bakery.take_loan(0.1, 1000)
except Warning:
    print("Bakery already has a loan")
else:
    raise Warning("Here should have been raised a warning!")

clothing_store = ClothingStore(2000) # (capital, loan, interest, initial_loan_amount, clothing_pieces) = (2000, 0, 0, 0, 0)
clothing_store.take_loan(0.1, 1000) # (3000, 1000, 0.1, 1000, 0)
amount_paid_c = clothing_store.pay_rent_and_loan(100) # (2700.0, 900, 0.1, 1000, 0)
clothing_store.procure(1, 100) # (2620.0, 900, 0.1, 1000, 100)
clothing_store.sell(10, 10) # (2720.0, 900, 0.1, 1000, 90)

bakery_two = Bakery(1000)
shopping_center = ShoppingCenter(10000, [bakery_two]) # capital = 10000
shopping_center.add_shop(ClothingStore(2000)) # capital = 10000
shopping_center.grant_loan(bakery_two, 0.05, 1000) # capital = 9000
shopping_center.collect_rent_and_loan(100) # capital = 9330

