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

    def findEquation(self):
        run = (7 - Point.getX)
        rise = (6 - Point.getY)
        slope = rise / run
        y-intercept =
        equation = "y = ", slope, "x + ", y-intercept, " with the points (7, 6) and ", p)
        print(equation)
        return equation

p2 = Point(6, 8)
