# Cube Class
# Luke Chase

class Cube:
    """Class of a theoretical cube."""

    def __init__(self, side_length):
        self.s = side_length

    def get_s(self):
        """Returns side length"""
        return self.s

    def surface_area(self):
        """Finds the surface area with the inputted side length"""
        sa = (6) * (self.s ** 2)
        print("Surface area = ", sa)

    def volume(self):
        """Finds the volume with the inputted side length"""
        volume = (self.s ** 3)
        print("Volume = ", volume)

