import geometric_object


#from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length:float, color:str, filled:bool):
        super().__init__(color, filled)
        self.__side_length = side_length
    
    def get_side_length(self):
        return round(self.__side_length, 2)
    
    def get_area(self):
        return round(6 * self.__side_length ** 2, 2)
    
    def get_volume(self):
        return round(self.__side_length ** 3, 2)