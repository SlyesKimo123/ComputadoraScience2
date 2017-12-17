
from graphics import *
import pyautogui
# import time

class Pen:
    def __init__(self, width):
        self.width = width

    def mousePos(self):
        """ Returns the coords of current mouse position """
        while True:
            return pyautogui.position()

    def click1(self, window):
        click1 = window.checkMouse()
        print(click1)
        return click1

    def click2(self, window):
        click2 = window.checkMouse()
        print(click2)
        return click2

    def draw(self, window):
        p = Line(self.click1(window), Point(100, 100))
        p.draw(window)

    def line_color(self, line, el_color):
        line.setFill(el_color)

    def line_width(self, object, wideness):
        object.setWidth(wideness)
