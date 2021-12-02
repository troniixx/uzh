#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not isinstance(battery_size, float) or not isinstance(battery_range_km, float):
            raise Warning
        if battery_size < 0 or battery_range_km < 0:
            raise Warning
        self.__e_max = battery_size
        self.__battery_range_km = battery_range_km
        self.__e = battery_size

    def charge(self, kwh):
        if not isinstance(kwh, float): raise Warning
        if kwh < 0: raise Warning
        if self.__e + kwh > self.__e_max:
            raise Warning('Car overcharged')
        else: self.__e += kwh

    def get_battery_status(self):
        return (self.__e, self.__e_max)

    def get_remaining_range(self):
        return self.__battery_range_km * self.__e / self.__e_max

    def drive(self, dist):
        if not isinstance(dist, float): raise Warning
        if dist < 0: raise Warning
        if dist > self.get_remaining_range():
            self.drive(self.get_remaining_range())
            raise Warning('battery depleted')
        self.__e -= dist * self.__e_max / self.__battery_range_km
