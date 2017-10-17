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
        y_intercept = (self.y - (m * self.x))
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

    def dist_between(self, other_punto):
        XDiff = other_punto.getX() - self.getX()
        YDiff = other_punto.getY() - self.getY()
        distance = math.sqrt(XDiff**2 + YDiff**2)
        print("The distance between is ", distance, "units.")
        return distance

    # Ignore this below function.  Working on a new one, but this is the one I was trying for HW

    def circle_fail(self, punto, punto_dos):
        x = self.getX()
        xx = punto.getX()
        xxx = punto_dos.getX()
        y = self.getY()
        yy = punto.getY()
        yyy = punto_dos.getY()
        xdist = (math.fabs(x) + math.fabs(xx))
        ydist = (math.fabs(y) + math.fabs(yy))
        secret_formular = math.sqrt((xdist ** 2) + (ydist ** 2))
        theanswer = print(secret_formular)
        return theanswer

    def circle(self, p2, p3):
        l = self.dist_between(p2)
        l2 = self.dist_between(p3)
        l3 = p2.dist_between(p3)
        midpoint_punto = self.halfway(p3)
        height = p2.dist_between(midpoint_punto)
        area = (l2 * height) / 2
        radius = (l * l2 * l3) / (4 * area)
        return radius

#p = Point(math.sqrt(2), math.sqrt(2))
#pp = Point(math.sqrt(3), math.sqrt(1))
#ppp = Point(0, 2)

p = Point(2, 0)
pp = Point(-2, 0)
ppp = Point(0, 2)

circle_radius = p.circle(pp, ppp)
print("Radius: ", circle_radius)
