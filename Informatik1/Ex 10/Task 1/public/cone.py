import geometric_object


#from geometric_object import GeometricObject


class Cone(GeometricObject):
    def __init__(self, radius:float,vertical_height:float,slant_height:float,color:str,filled:bool):
        super().__init__(color, filled)
        self.__PI = 3.14
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height
    
    def get_radius(self):
        return round(self.__radius, 2)
    
    def get_vertical_height(self):
        return round(self.__vertical_height, 2)
    
    def get_slant_height(self):
        return round(self.__slant_height, 2)
    
    def get_area(self):
        area = self.__PI * self.__radius ** 2 + self.__PI * self.__radius * self.__slant_height
        return round(area, 2)
    
    def get_volume(self):
        volume = 1/3 * self.__PI * self.__radius ** 2 * self.__vertical_height
        return round(volume, 2)