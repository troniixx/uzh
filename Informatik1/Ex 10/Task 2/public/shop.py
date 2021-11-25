#!/usr/bin/env python3
import abc

class Shop:

    def __init__(self, capital):
        self._capital = capital
        self.__loan = 0
        self.__initial_loan_amount = 0
        self.__interest = 0

    def sell(self, price_per_unit, units):
        if self.get_produced_units() < units:
            self._capital += self.get_produced_units() * price_per_unit
            self.set_produced_units(0)
            raise Warning("Shop ran out of units")
        self.set_produced_units(self.get_produced_units() - units)
        self._capital += price_per_unit * units

    def procure(self, price_per_unit, units):
        if self._capital < price_per_unit * units:
            units_paid = self._capital // price_per_unit
            self.add_procured_units(units_paid)
            self._capital -= price_per_unit * units_paid
            raise Warning("Shop is out of money")
        self.add_procured_units(units)
        self._capital -= units * price_per_unit

    @abc.abstractmethod
    def add_procured_units(self, units):
        pass
    
    @abc.abstractmethod
    def get_produced_units(self):
        return self

    @abc.abstractmethod
    def set_produced_units(self, units):
        self.units = units

    def pay_rent_and_loan(self, rent):
        amount_owed = rent
        if self.__loan != 0:
            amount_owed += round(
                self.__loan * self.__interest + self.__initial_loan_amount / 10,
                0)
            self.__loan -= round(self.__initial_loan_amount / 10)
        if self._capital < amount_owed:
            raise Warning("Company cant pay rent due to lack of capital")
        self._capital -= amount_owed
        return amount_owed

    def take_loan(self, interest, amount):
        if self.__loan != 0.0:
            raise Warning("Already has a loan")
        self.__interest = interest
        self.__loan = amount
        self.__initial_loan_amount = amount
        self._capital += amount

    def get_loan(self):
        return self.__loan

    def get_status(self):
        return (
        self._capital, self.__loan, self.__interest, self.__initial_loan_amount)