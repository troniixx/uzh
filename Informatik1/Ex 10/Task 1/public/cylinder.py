import geometric_object


class Cylinder(geometric_object):
    
    global Pi
    Pi = 3.14

    def __init__(self, radius, height, color, filled):
        self.__radius = radius
        self.__height = height
        super().__init__(color, filled)

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        return (Pi * (self.__radius**2)) * (2*Pi*self.__radius*self.__height)

    def get_volume(self):
        return Pi*(self.__radius**2)*self.__height
