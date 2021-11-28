#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

import restaurant

class DeliveryRestaurant:

    def __init__(self, name, cuisine_type, delivery_radius, is_open=False):
        self.__name = name
        self.__cuisine_type = cuisine_type
        self.__delivery_radius = delivery_radius
        self.__is_open = is_open

    def is_in_range(self, distance):
        pass