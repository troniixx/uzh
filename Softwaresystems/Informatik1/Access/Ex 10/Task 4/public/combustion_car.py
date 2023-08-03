#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not isinstance(gas_capacity, float) or not isinstance(gas_per_100km, float):
            raise Warning
        if gas_capacity < 0 or gas_per_100km < 0:
            raise Warning
        
        self.__c_max = gas_capacity
        self.__gas_per_100km = gas_per_100km
        self.__c = gas_capacity

    def fuel(self, f):
        if not isinstance(f, float): raise Warning
        if f < 0 : raise Warning

        if self.__c + f > self.__c_max:
            raise Warning("Overfilled")
        else: self.__c += f

    def get_gas_tank_status(self):
        return (self.__c, self.__c_max)

    def get_remaining_range(self):
        return self.__c * 100 / self.__gas_per_100km

    def drive(self, dist):
        if not isinstance(dist, float): raise Warning
        if dist < 0: raise Warning
        if dist > self.get_remaining_range():
            self.drive(self.get_remaining_range())
            raise Warning('fuel depleted')
        self.__c -= dist * self.__gas_per_100km / 100
