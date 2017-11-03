# Button program

from graphics import *

class Button:

    def __init__(self, win, center, radius, label):
        r = radius
        x,y = center.getX(), center.getY()

        self.xmax, self.xmin = x+r, x-r
        self.ymax, self.ymin = y+r, y-r

#        p1 = Point(self.xmin, self.ymin)
#        p2 = Point(self.xmax, self.ymax)

#        self.rect = Rectangle(p1, p2)
        self.circle = Circle(center, r)
        self.circle.setFill('lightgray')
        self.circle.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)

        self.deactivate()

    def clicked(self, p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
