class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def findEquation(self, punto):
        x = self.getX()
        xx = punto.getX()
        y = self.getY()
        yy = punto.getY()
        slope = int((x - xx) / (y - yy))
        y_intercept = int(self.y - slope * self.x)
        equation = print("y =", slope, "x +", y_intercept)
        return equation

p = Point(4, 5)
pp = Point(6, 7)
p.findEquation(pp)
