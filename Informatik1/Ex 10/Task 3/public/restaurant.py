#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
import copy


class Restaurant:

    def __init__(self, name, cuisine_type, is_open = False):
        self.__name = name
        self.__cuisine_type = cuisine_type
        self.__is_open = is_open

    def describe_restaurant(self):
        return self.__name

    def open_restaurant(self):
        self.__is_open = True

    def close_restaurant(self):
        self.__is_open = False
        

    def is_open(self):
        return self.__is_open

    def add_consumption_unit(self, name, price):
        d = {}
        d[name] = price

    def remove_consumption_unit(self, name):
        pass

    def get_menu(self):
        pass

    def sell_unit(self, name):
        pass

    def get_sales(self):
        pass

