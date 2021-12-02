#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__op_mode = 'e'

    def switch_to_combustion(self):
        self.__op_mode = 'c'

    def switch_to_electric(self):
        self.__op_mode = 'e'

    def get_remaining_range(self):
        return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, float): raise Warning
        if dist < 0: raise Warning
        c_range = CombustionCar.get_remaining_range(self)
        e_range = ElectricCar.get_remaining_range(self)
        if dist > self.get_remaining_range():
            CombustionCar.drive(c_range)
            ElectricCar.drive(e_range)
            raise Warning('both modes depleted')
        if self.__op_mode == 'c':
            if c_range <= dist:
                CombustionCar.drive(self, c_range)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - c_range)
            else: CombustionCar.drive(self, dist)
        elif self.__op_mode == 'e':
            if e_range <= dist:
                ElectricCar.drive(self, e_range)
                self.switch_to_combustion
                CombustionCar.drive(self, dist - e_range)
            else: ElectricCar.drive(self, dist)
