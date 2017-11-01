# dieview12.py
# 12-sided die
from graphics import *
from random import randrange
from ButtonProgram_LukeChase import Button

from graphics import *

class DieView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
        d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size # radius of each pip
        hsize = size / 1.5 # half of size
        offset = 0.6 * hsize # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [ self.__makePip(cx, cy),
                      self.__makePip(cx-offset, cy-offset),
                      self.__makePip(cx+offset, cy+offset),
                      self.__makePip(cx-offset, cy+offset),
                      self.__makePip(cx+offset, cy-offset),
                      self.__makePip(cx, cy-offset),
                      self.__makePip(cx, cy+offset),
                      self.__makePip(cx+offset, cy),
                      self.__makePip(cx-offset, cy) ]

        # Create a table for which pips are on for each value
        self.onTable = [ [0], [1, 2], [0, 1 ,2], [1, 2, 3, 4],
                       [0, 1, 2, 3, 4], [1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8],[0 , 1 , 2 , 3 , 4 , 5 , 6 , 7, 8],
                       [0,1,2,3,4,5,6,7, 8] ]
        self.setValue(1)

    def __makePip(self, x, y):
        """Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)
        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
