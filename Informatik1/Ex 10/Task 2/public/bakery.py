#!/usr/bin/env python3

import shop


class Bakery(shop):

    def __init__(self, capital):
        self._capital = capital
        self.__produced_units = 0
        self.__loan = 0
        self.__initial_loan_amount = 0
        self.__interest = 0
        self.__dough = 0
        self.__bread = 0

    def sell(self, price_per_unit, units):
        self._capital += (price_per_unit*0.25)*units

    def produce(self, costs_per_unit):
        self._capital -= costs_per_unit

    def add_procured_units(self, units):
        self.__produced_units.append(units)

    def get_produced_units(self):
        return self.__produced_units

    def set_produced_units(self, units):
        self.units = units

    def pay_rent_and_loan(self, rent):
        return super().pay_rent_and_loan(rent)

    def get_status(self):
        return super().get_status()