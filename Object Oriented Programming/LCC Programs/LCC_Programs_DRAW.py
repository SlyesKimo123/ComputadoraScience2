
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

    def clicks(self, window):
        click1 = window.checkMouse()
        click2 = window.checkMouse()
        return click1, click2


    def draw(self, window):
        click1, click2 = self.clicks(window)
        p = Line(click1, click2)
        p.draw(window)

    def line_color(self, line, el_color):
        line.setFill(el_color)

    def line_width(self, object, wideness):
        object.setWidth(wideness)
