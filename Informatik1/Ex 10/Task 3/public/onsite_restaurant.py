#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
import restaurant


class OnsiteRestaurant:

    def __init__(self, name, cuisine_type, num_tables, is_open=False):
        self.__name = name
        self.__cuisine_type = cuisine_type
        self.__num_tables = num_tables
        self.__is_open = is_open

    def occupy_table(self):
        pass

    def free_table(self):
        pass

    def get_available_tables(self):
        pass