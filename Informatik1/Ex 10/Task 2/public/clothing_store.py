#!/usr/bin/env python3
import shop


class ClothingStore(shop):

    def __init__(self, capital):
        super().__init__()
        self._capital = capital

    def procure(self, price_per_unit, units):
        pass

    def add_procured_units(self, units):
        pass

    def get_produced_units(self):
        pass

    def set_produced_units(self, units):
        pass

    def get_status(self):
        return super().get_status()