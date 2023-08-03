#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
from restaurant import Restaurant


class OnsiteRestaurant(Restaurant):

    def __init__(self, name, cuisine_type, num_tables, is_open=False):
        super().__init__(name, cuisine_type, is_open)
        self.__num_tables = num_tables
        self.__available_tables = num_tables

    def occupy_table(self):
        if self.__available_tables < 1:
            raise Warning("No tables available")
        else: self.__available_tables -= 1

    def free_table(self):
        if self.__available_tables == self.__num_tables:
            raise Warning("Every table is free")
        else: self.__available_tables += 1

    def get_available_tables(self):
        return self.__available_tables