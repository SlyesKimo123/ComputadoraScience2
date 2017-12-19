# Luke Chase
# Final Project --- Computer Science II

# This is the DRAW program, where the pen class and methods are created.

from graphics import *

class Pen:

    def clicks(self, window):
        """ Returns the points of the two mouse clicks.  Calls from the
            getMouse method in graphics module """
        click1 = window.getMouse()
        click2 = window.getMouse()
        return click1, click2

    def draw(self, window, color):
        """ Draws a line from mouse click 1 to mouse click 2 and
            returns the line """
        click1, click2 = self.clicks(window)
        line = Line(click1, click2)
        line.draw(window)
        line.setFill(color)
        midpoint = line.getCenter()
        circle = Circle(midpoint, 2)
        circle.setFill("black")
        circle.draw(window)

    def line_width(self, object, wideness):
        """ Adjusts the width of the last line drawn"""
        object.setWidth(wideness)
