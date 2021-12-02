#!/usr/bin/env python3

class ShoppingCenter:

    def __init__(self, capital, shops:list):
        if shops == []:
            raise Warning("No shops")
        self._capital = capital
        self.__shops = shops
        self.__debtors = []

    def collect_rent_and_loan(self, rent):
        for shop in self.__shops:
            self._capital += shop.pay_rent_and_loan(rent)
            if shop in self.__debtors and shop.get_loan() == 0:
                self.__debtors.remove(shop)

    def grant_loan(self, shop, interest, amount):
        if shop not in self.__shops: raise Warning("Shop not in center")
        if amount > self._capital: raise Warning("Not enough capital")
        self.__debtors.append(shop)
        shop.take_loan(interest, amount)
        self._capital -= amount

    def add_shop(self, shop):
        self.__shops.append(shop)

    def remove_shop(self, shop):
        self.__shops.remove(shop)
        return shop

    def get_status(self):
        return (
        self._capital, tuple(self.__shops), tuple(self.__debtors))

    def __len__(self):
        return len(self.__shops)