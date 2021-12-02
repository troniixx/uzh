#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from onsite_restaurant import OnsiteRestaurant
from delivery_restaurant import DeliveryRestaurant
from restaurant import Restaurant



restaurant_one = Restaurant('Restaurant One', "Mixed Cuisine")
restaurant_one.add_consumption_unit("Caesar Salad", 15)
restaurant_one.open_restaurant()
restaurant_one.sell_unit("Caesar Salad")
restaurant_one.sell_unit("Caesar Salad")
restaurant_one.sell_unit("Caesar Salad")
print(restaurant_one.get_sales()) # 3 * 15


onsite_one = OnsiteRestaurant("Onsite Steak One", "Steaks", 10)
onsite_one.occupy_table()
onsite_one.free_table()
print(onsite_one.get_available_tables())

deli_one = DeliveryRestaurant("Kebab Delivery One", "Kebab", 20)
print(deli_one.is_in_range(10))

