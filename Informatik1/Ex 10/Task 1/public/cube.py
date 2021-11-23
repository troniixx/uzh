from public.geometric_object import GeometricObject


class Cube(GeometricObject):
    
    def __init__(self, side_length, color, filled):
        self.__side_length = side_length
        self.color = color
        self.filled = filled

    def get_side_length(self):
        return self.__side_length

    def get_area(self):
        return 6* (self.__side_length**2)

    def get_volume(self):
        return self.__side_length**3