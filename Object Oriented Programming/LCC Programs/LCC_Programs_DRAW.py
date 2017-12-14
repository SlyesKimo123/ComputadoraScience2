
from graphics import *
import pyautogui
import time

class Pen:
    def __init__(self, width):
        self.width = width

    def mousePos(self):
        """ Returns the coords of current mouse position """
        while True:
            return pyautogui.position()

    def mouseState(self, window):
        """ Checks to see if mouse has been clicked or not.  Returns True or False """
        click_pos = window.checkMouse()
        print(click_pos)
        return click_pos

    def mouseState2(self, window):
        if mouseState(window) == True and time > 0.1:
            click2_pos = window.checkMouse()
            print(click2_pos)
            return click2_pos

    def pendown(self, window):
        if window.checkMouse():
            print()

    def draw(self, window):
        if self.mouseState == True:
            p = Line(self.mouseState(window), self.mouseState2(window))
            p.draw(window)

    def line_color(self, line, el_color):
        line.setFill(el_color)

    def line_width(self, object, wideness):
        object.setWidth(wideness)
