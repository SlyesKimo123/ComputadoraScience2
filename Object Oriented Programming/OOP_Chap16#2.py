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

    def reflect_x(self):
        getX = q.getX()
        getY = q.getY()
        reflection = getY * -1
        print("The reflection of (", getX, ", ", getY, ") ", "is (", getX, ", ", reflection, ").")
p = Point(3, 4)
q = Point(5, 12)
p.reflect_x()
