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

p = Point(7, 6)
print(p)

p.move(4, 6)
print(p)
print("¡BOOM CHAKALAKA!")
