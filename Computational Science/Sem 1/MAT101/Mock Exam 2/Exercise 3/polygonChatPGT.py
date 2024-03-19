import numpy as np

class RegularPolygon:
    def __init__(self, n, l):
        self.n = n  # number of edges
        self.l = l  # length of one edge
        # Calculate the radius of the inscribed circle
        self.R = self.l / (2 * np.sin(np.pi / n))

    def area(self):
        # Calculate the area using the formula for regular polygons
        return 0.5 * self.n * self.R * self.l

class Circle(RegularPolygon):
    def __init__(self, radius):
        # A circle is considered a polygon with an infinite number of sides
        super().__init__(n=np.inf, l=0)
        self.R = radius

    def area(self):
        # Calculate the area using the formula for a circle
        return np.pi * self.R**2

# Example usage:
polygon = RegularPolygon(n=5, l=1)
print(f"Area of regular polygon with 5 edges: {polygon.area()}")

circle = Circle(radius=1)
print(f"Area of circle with radius 1: {circle.area()}")
