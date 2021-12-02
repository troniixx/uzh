import geometric_object


#from geometric_object import GeometricObject


class Cylinder(GeometricObject):
    def __init__(self, radius:float, height:float, color:str, filled:bool):
        super().__init__(color, filled)
        self.__PI = 3.14
        self.__radius = radius
        self.__height = height
    
    def get_radius(self):
        return round(self.__radius, 2)
    
    def get_height(self):
        return round(self.__height, 2)
    
    def get_area(self):
        area = self.__PI * self.__radius ** 2 + 2 * self.__PI * self.__radius * self.__height
        return round(area, 2)
    
    def get_volume(self):
        volume = self.__PI * self.__radius ** 2 * self.__height
        return round(volume, 2)
