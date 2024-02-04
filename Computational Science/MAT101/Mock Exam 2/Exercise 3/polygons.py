import numpy

class regular_polygons():
    def __init__(self, n, l):
        self.n = n
        self.l = l
        
    def area(self, r):
        return (self.n/2)*self.l*r
    
class circles(regular_polygons):
    def __init__(self, n, l):
        self.n = numpy.inf
        self.l = l
    
    def area(self, r):
        return numpy.pi*(r**2)
    
    
if __name__ == "__main__":
    circ1 = circles(3, 2)
    print(circ1.area(3))
    
    poly1 = regular_polygons(3, 2)
    print(poly1.area(3))