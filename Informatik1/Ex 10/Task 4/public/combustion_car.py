#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class CombustionCar:

    def __init__(self, gas_capacity, gas_per_100km):
        self.__gas_capactiy = gas_capacity
        self.__gas_per_100km = gas_per_100km

    def fuel(self, f):
        pass

    def get_gas_tank_status(self):
        pass

    def get_remaining_range(self):
        pass

    def drive(self, dist):
        pass
