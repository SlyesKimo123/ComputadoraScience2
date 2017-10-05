import math
class Point:

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

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def dist_between(self, other_punto):
        XDiff = other_punto.getX() - self.getX()
        YDiff = other_punto.getY() - self.getY()
        distance = math.sqrt(XDiff**2 + YDiff**2)
        print("The distance between is ", distance, "units.")
        return distance

p = Point(3, 4)
q = Point(5, 12)
p.dist_between(q)
