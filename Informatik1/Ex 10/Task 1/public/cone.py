from public.geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius, vertical_height, slant_height, color, filled):
        self.__PI = 3.14
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height
        self.color = color
        self.filled = filled

    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height

    def get_slant_height(self):
        return self.__slant_height

    def get_area(self):
        return (self.__PI * (self.__radius**2)) * (self.__PI * self.__radius * self.__slant_height)

    def get_volume(self):
        x = 1/3
        return x * self.__PI * (self.__radius**2) * self.__vertical_height