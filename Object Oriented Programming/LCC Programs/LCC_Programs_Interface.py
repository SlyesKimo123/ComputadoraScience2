# Luke Chase
# CS II Final Project --- Fall 2017
# Lukeman Clagl Corporation - LCC

# import statements
from ButtonProgram_LukeChase import Button
from LCC_Programs_DRAW import Pen
from graphics import *
# from tkinter import *

class LCC_Graphics:
    """" This class has all the methods for the drawing program """

    def __init__(self):
        self.icon = Image(Point(100, 50),
                                 "~/Documents/Computadora Science II/"
                                 "ComputadoraScience2/Object Oriented Programming/"
                                 "LCC Programs/LCC_Icon.gif")
                                # loads the LCC Programs logo
        self.pen = Pen(2)

    def createWindow(self, x, y):
        """ Creates the window of the program and allows for parameters
            to define x and y.  Returns the window created """
        self.window = GraphWin("LCC Programs", x, y)
        return self.window

    def run(self):
        """ This method is what starts the program when called.  It calls the startup
            and startup_buttons methods, and checks if the createDocumentario method
            returns True. If so, the program starts and if not, the window closes"""
        self.startup()
        if self.createDocumentario() == True:
            self.start_window.close()
            self.startProgram()
        self.close()

    def startup_buttons(self):
        """ Creates buttons for startup window and returns them in a list """
        self.createDocButton = Button(self.window, Point(100, 100), 100, 60,
                                      "Create Document")
        self.CANCELstartup_button = Button(self.window, Point(100, 180), 60, 30,
                                           "Cancel")
        start_up_buttonlist = []
        start_up_buttonlist.append(self.createDocButton)
        start_up_buttonlist.append(self.CANCELstartup_button)
        return start_up_buttonlist

    def startup(self):
        """ Creates the startup window and draws LCC Programs Logo,
            checks if the 'Cancel' button is clicked """
        self.start_window = self.createWindow(200, 300)
        # (Above) calls from createWindow method to set window size
        self.start_window.setBackground("black") # sets window BG color

        self.icon.draw(self.start_window)

    def createDocumentario(self):
        ans = self.choose(self.window, self.startup_buttons())
        return ans == "Create Document"

    def startProgram(self):
        self.createWindow(1000, 1000)
        self.window.setBackground("white")
        self.appearance()
        self.actionButtons()
        while True:
            self.pen.draw(self.window)
            self.doc_nombre()
            self.buttonFunctions()

    def choose(self, thewindow, button_set):
        while True:
            p = thewindow.getMouse()
            for b in button_set:
                if b.clicked(p):
                    return b.getLabel()

    def mousePos(self):
        """ Returns the coords of the current mouse position """
        self.mousePosition = self.window.getMouse()
        return self.mousePosition

    def cursorPicture(self):
        """ This is the little icon that represents the cursor and makes the icon
            follow the mouse around the screen. """
        self.penIcon = Image(self.mousePosition, "PenIcon.gif")

    def buttonFunctions(self):
        """ Each button will have their own function in a different method.
           In order to call these functions all at once, they will be
           activated in this method, which I can call when I run the program. """
        while True:
            self.closeButton()

    def clicked(self, button):
        """ Returns the LABEL of the button in parameter if clicked """
        while True:
            p = self.window.getMouse()
            if button.clicked(p):
                return button.getLabel()

    def doc_nombre(self):
        self.doc_name_text = Text(Point(65, 60), "Title Here")
        self.doc_name_button = Button(self.window,
                                      Point(65, 60),
                                      100,
                                      30,
                                      "{0}".format(self.doc_name_text.getText()))
        if self.clicked(self.doc_name_button):

            self.popup_win = self.createWindow(100, 100) # Tk()
#            self.popup_win.geometry(100 x 100 + 0 + 0)

            self.popup_button = Button(self.popup_win,
                                       Point(75, 75), 40, 30,
                                       "Title: ")
            self.done_button = Button(self.popup_win, Point(75, 10),
                                      30, 20, "Done")
            while True:
#                self.doc_name = Text("Document Title".format())#Tk input here))
#                self.doc_name_text.setText("{0}".format(self.doc_name))
                if self.clicked(self.popup_button):
                    self.popup_button.setText(" ")
                elif self.clicked(self.done_button):
                    self.popup_win.close()
#            self.doc_name = input("Title Here: ")


    def appearance(self):
        """ This method draws a bunch of shapes to make the document more
            visually appealing (I hope). """
        self.top_banner = Rectangle(Point(0, 0), Point(1000, 40))
        self.top_banner.setFill("blue")
        self.top_banner.draw(self.window)
        self.button_banner = Rectangle(Point(0, 40), Point(1000, 80))
        self.button_banner.setFill("grey")
        self.button_banner.draw(self.window)

    def actionButtons(self):
        """ Creates the buttons in the top of the document for user to click.
            Buttons are added to a list"""
        self.drawingbuttons = []
        self.drawWidthIncreaseButton = Button(self.window,
                                              Point(280, 60),
                                              20,
                                              20,
                                              "+")
        self.drawWidthDecreaseButton = Button(self.window,
                                              Point(310, 60),
                                              20,
                                              20,
                                              "-")
        self.blueButton = Button(self.window, Point(130, 60), 20, 20, "")
        self.blueButton.setFill("blue")
        self.greenButton = Button(self.window, Point(160, 60), 20, 20, "")
        self.greenButton.setFill("green")
        self.orangeButton = Button(self.window, Point(190, 60), 20, 20, "")
        self.orangeButton.setFill("orange")
        self.yellowButton = Button(self.window, Point(220, 60), 20, 20, "")
        self.yellowButton.setFill("yellow")
        self.redButton = Button(self.window, Point(250, 60), 20, 20, "")
        self.redButton.setFill("red")
        self.drawingbuttons.append([self.drawWidthIncreaseButton,
                                    self.drawWidthDecreaseButton,
                                    self.redButton,
                                    self.blueButton,
                                    self.greenButton,
                                    self.orangeButton,
                                    self.yellowButton])
        return self.drawingbuttons

    def closeButton(self):
        """ Creates the "X" button in the top left corner of the
            window.  It closes the program when clicked """
        self.X_button = Button(self.window, Point(20, 15), 15, 15, "X")
        # (Above) Creates 'X' button in top left corner
        self.X_button.setFill("red")
        if self.clicked(self.X_button): # Checks if button is clicked
            self.window.close()

    def close(self):
        """ Closes the window when called """
        self.window.close()

interface = LCC_Graphics()
interface.run()

""" Sources:
- http://simpleicon.com/pencil.html
- https://thenounproject.com/term/text-cursor/26475/
- https://www.piskelapp.com/
"""
