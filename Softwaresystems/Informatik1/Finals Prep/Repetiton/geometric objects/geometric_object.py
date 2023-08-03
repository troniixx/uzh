from abc import ABC, abstractmethod


class GeometricObject(ABC):
    def __init__(self, color:str, filled:bool):
        self.__color = color
        self.__filled = filled
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color:str):
        self.__color = color
    
    def get_filled(self):
        return self.__filled
    
    def set_filled(self, filled:bool):
        self.__filled = filled
        
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_volume(self):
        pass
