#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from restaurant import Restaurant

class DeliveryRestaurant(Restaurant):

    def __init__(self, name, cuisine_type, delivery_radius, is_open=False):
        super().__init__(name, cuisine_type, is_open)
        self.__delivery_radius = delivery_radius

    def is_in_range(self, distance):
        if distance <= self.__delivery_radius: return True
        else: return False