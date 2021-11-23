from abc import ABC, abstractmethod


class GeometricObject:
    
    #color = str, filled = bool

    def __init__(self, color, filled):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        pass

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        pass

    @abstractmethod
    def get_area(self): #float
        pass

    @abstractmethod
    def get_volume(self): #float
        pass