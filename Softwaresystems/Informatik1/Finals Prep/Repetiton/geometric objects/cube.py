import geometric_object

class Cube(geometric_object):
    def __init__(self,side_length:float, color:str, filled:bool):
        super().__init__(color, filled)
        self.__PI = 3.14
        self.__side_length = side_length

    def get_side_length(self):
        return self.__side_length

    def get_area(self):
        return 6*(self.__side_length**2)

    def get_volume(self):
        return self.__side_length**3