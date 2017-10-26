# dieview.py
from graphics import *
from random import randrange
from ButtonProgram_LukeChase import Button

from graphics import *

class DieView:

    def __init__(self, win, center, size):

        self.win = win
        self.background = "white"
        self.foregroud = "black"
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)

        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)

        self.setValue(1)

    def __makePip(self, x, y):
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        if value == 1:
            self.pip4.setFill(self.foregroud)
        elif value == 2:
            self.pip1.setFill(self.foregroud)
            self.pip7.setFill(self.foregroud)
        elif value == 3:
            self.pip1.setFill(self.foregroud)
            self.pip7.setFill(self.foregroud)
            self.pip4.setFill(self.foregroud)
        elif value == 4:
            self.pip1.setFill(self.foregroud)
            self.pip3.setFill(self.foregroud)
            self.pip5.setFill(self.foregroud)
            self.pip7.setFill(self.foregroud)
        elif value == 5:
            self.pip1.setFill(self.foregroud)
            self.pip3.setFill(self.foregroud)
            self.pip4.setFill(self.foregroud)
            self.pip5.setFill(self.foregroud)
            self.pip7.setFill(self.foregroud)
        else:
            self.pip1.setFill(self.foregroud)
            self.pip2.setFill(self.foregroud)
            self.pip3.setFill(self.foregroud)
            self.pip5.setFill(self.foregroud)
            self.pip6.setFill(self.foregroud)
            self.pip7.setFill(self.foregroud)
