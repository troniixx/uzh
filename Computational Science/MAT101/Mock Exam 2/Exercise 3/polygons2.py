import numpy as np
import math

class RegularPolygon:
    def __init__(self, n, l):
        self.n = n
        self.l = l

    def radius(self):
        return (self.l / 2) / math.tan(math.pi / self.n)

    def area(self):
        R = self.radius()
        return (self.n / 2) * self.l * R

class Circle(RegularPolygon):
    def __init__(self, r):
        super().__init__(n=np.inf, l=2 * r)
        self.r = r

    def area(self):
        return math.pi * self.r**2
    
if __name__ == "__main__":
    circ1 = Circle(3)
    print(circ1.area())
    
    poly1 = RegularPolygon(3, 2)
    print(poly1.area())