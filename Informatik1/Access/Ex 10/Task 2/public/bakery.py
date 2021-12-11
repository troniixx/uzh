#!/usr/bin/env python3

#import shop


from shop import Shop

from shop import Shop
class Bakery(Shop):

    def __init__(self, capital):
        super().__init__(capital)
        self.__bread = 0
        self.__dough = 0

    def produce(self, costs_per_unit):
        while self.__dough > 0 and self._capital >= costs_per_unit:
            self.__bread += 1
            self.__dough -= 1
            self._capital -= costs_per_unit
            if self._capital < costs_per_unit:
                raise Warning("Shop ran out of money")

    def sell(self, price_per_unit, units:int):
        return super().sell(0.75 * price_per_unit, units)

    def procure(self, price_per_unit, units:int):
        return super().procure(price_per_unit, units)

    def add_procured_units(self, units:int):
        self.__dough += units

    def get_produced_units(self):
        return self.__bread

    def set_produced_units(self, units:int):
        self.__bread = units

    def pay_rent_and_loan(self, rent):
        return super().pay_rent_and_loan(0.8 * rent)
    
    def get_status(self):
        stats = list(super().get_status())
        stats.extend([self.__dough, self.__bread])
        return tuple(stats)