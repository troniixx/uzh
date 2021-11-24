from abc import ABC, abstractmethod


class GeometricObject:
    
    #color = str, filled = bool

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled

    @abstractmethod
    def get_area(self): #float
        pass

    @abstractmethod
    def get_volume(self): #float
        pass