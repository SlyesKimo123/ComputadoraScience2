# Sphere Class
# Luke Chase

import math

class Sphere:
    """Class of a theoretical sphere."""

    def __init__(self, radius):
        """Creates a sphere with a given radius"""
        self.r = radius

    def get_radius(self):
        """Returns the radius"""
        return self.r

    def surface_area(self):
        """Find surface area with inputted radius"""
        sa = (4) * (math.pi) * (self.r ** 2)
        print("Surface area = ", sa)

    def volume(self):
        """Finds volume of cube with inputted radius
        Sphere Volume = 4/3(pi)(r**2)"""
        volume = (4/3) * (math.pi) * (self.r ** 2)
        print("Volume = ", volume)
