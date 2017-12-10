
from graphics import *
import pyautogui

class Pen:
    def __init__(self, width, color, ):
        self.width = width
        self.color = color

    def mousePos(self):
        """ Returns the coords of current mouse position """
        while True:
            return pyautogui.position()

    def mouseState(self, window):
        """ Checks to see if mouse has been clicked or not.  Returns True or False """
#        if getMouse
        return window.checkMouse()

    def pendown(self, window):
        if window.checkMouse():
            print()

    def draw(self, window):
        if window.checkMouse:
            window.Circle(Point(window.getMouse), 10, 10)


#    def line_color(self, el_color):
#        button(from interface).

#    def line_width(self, wideness):
#        fff

pen = Pen(3,2)
pen.mousePos()
