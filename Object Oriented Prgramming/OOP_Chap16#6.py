import math
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
        multiply = slope(x)
        subtract = multiply - y
        y_intercept = subtract
        equation = print("y =", slope, "x +", y_intercept)
        return equation

    def move(self, dx, dy):
        self.x = (self.x + dx)
        self.y = (self.y + dy)
        return self.x, self.y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(my, mx)

    # Ignore this below function.  Working on a new one, but this is the one I was trying for HW

    def circle(self, punto, punto_dos):
        x = self.getX()
        xx = punto.getX()
        xxx = punto_dos.getX()
        y = self.getY()
        yy = punto.getY()
        yyy = punto_dos.getY()
        xdist = (math.fabs(x) + math.fabs(xx))
        ydist = (math.fabs(y) + math.fabs(yy))
        secret_formular = math.sqrt((xdist ** 2) + (ydist ** 2))
        print(secret_formular)





p = Point(math.sqrt(2), math.sqrt(2))
pp = Point(math.sqrt(1), math.sqrt(3))
ppp = Point(1, 0)

p.circle(pp, ppp)
