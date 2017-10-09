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
        slope = (x - xx) / (y - yy)
#        multiply = slope(x)
#        subtract = multiply - y
#        y_intercept = subtract
        b = y - x*y
        t = (slope, b)
        equation = print("y =", slope, "x +", t)
        return equation

p = Point(7, 6)
pp = Point(6, 8)
p.findEquation(pp)
