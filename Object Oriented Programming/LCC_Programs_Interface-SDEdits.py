# Luke Chase
# CS II Final Project --- Fall 2017
# Lukeman Clagl Corporation - LCC

# import statements
from ButtonProgram_LukeChase import Button
from graphics import *
import time

class LCC_Graphics:
    """" This class has all the methods for the drawing program """
    def __init__(self):
        self.startupwindow = GraphWin("LCC Programs", 200, 300)
        self.startupwindow.setBackground('black')
        self.window = GraphWin("LCC Programs", 1000, 800)
        self.window.setBackground('white')

        self.COimageICON = Image(Point(50, 50), "banana.gif")

        self.X_button = Button(self.window, Point(10, 10), 10, 10, "X")

    def startup(self, window):
        self.createDoc_button = Button(window, Point(100, 100), 50, 30., "Create Document")
        self.CANCELstartup_button = Button(window, Point(200, 100), 50, 30, "Cancel")
        self.startup_buttons = [self.createDoc_button, self.CANCELstartup_button]
        self.COimageICON.draw(window)
        #self.COimageICON.draw()
        print("Hello")

    def createDocumentario(self):
        ans = self.choose(["Create Document", "Cancel"])
        return ans == "Create Document"

#    def cursorPicture(self):
#        """ This is the little icon that represents the cursor and makes the icon
#            follow the mouse around the screen. """
#        # open two icon images here
#        getPos = self.window.getMouse()

    def choose(self, buttons):
        while True:
            p = self.window.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def actionButtons(self):
        self.drawingbuttons = []
        self.drawWidthIncreaseButton = Button(self.window, Point(100, 100), 10, 10, "+")
        self.drawWidthDecreaseButton = Button(self.window, Point(100, 100), 10, 10, "-")
        self.redButton = Button(self.window, Point(200, 200), 10, 10, "COLOR HERE")
        self.blueButton = Button(self.window, Point(200, 200), 10, 10, "COLOR HERE")
        self.greenButton = Button(self.window, Point(200, 200), 10, 10, "COLOR HERE")
        self.orangeButton = Button(self.window, Point(200, 200), 10, 10, "COLOR HERE")
        self.yellowButton = Button(self.window, Point(200, 200), 10, 10, "COLOR HERE")

    def run(self):
        self.startup(self.startupwindow)
        while self.createDocumentario():
            self.startProgram()
        self.close()

    def startProgram(self):
        time.sleep(10)

    def close(self):
        self.window.close()

### I really appreciate that you are including your sources as you go! This is a very good practice to get into early on.

""" Sources:
- http://www.iconarchive.com/tag/pencil
- https://thenounproject.com/term/text-cursor/26475/
- https://www.piskelapp.com/
"""

### LLC_graphics is its own class and you are not referring to it from another class so you can call it directly.
test = LCC_Graphics()
test.run()
