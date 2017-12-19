# Luke Chase
# CS II Final Project --- Fall 2017
# Lukeman Clagl Corporation - LCC

# import statements
from ButtonProgram_LukeChase import Button
from LCC_Programs_DRAW import Pen
from graphics import *
import pyautogui

class LCC_Graphics:
    """" This class has all the methods for the drawing program """

    def __init__(self):
        self.icon = Image(Point(100, 50),
                                 "~/Documents/Computadora Science II/"
                                 "ComputadoraScience2/Object Oriented Programming/"
                                 "LCC Programs/LCC_Icon.gif")
                                # loads the LCC Programs logo
        self.pen = Pen()

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
        """ Returns True if Create Document button is clicked in the startup window"""
        ans = self.choose(self.window, self.startup_buttons())
        return ans == "Create Document"

    def startProgram(self):
        """ List of actions to be completed before the user can start drawing """
        self.window = self.createWindow(1000, 1000)
        self.window.setBackground("white")
        self.appearance()
        self.colorButtons()
        self.closeButton()
#        self.TTT(self.window) # This is a work in progress. It almost works, but if not clicked
                              # and unclicked it will not progress to the next action
#        self.doc_nombre()
        while True:
            self.pen.draw(self.window, self.color()) # DRAW

    def choose(self, thewindow, button_set):
        while True:
            p = thewindow.getMouse()
            for b in button_set:
                if b.clicked(p):
                    return b.getLabel()

    def cursorPicture(self):
        """ This is the little icon that represents the cursor and makes the icon
            follow the mouse around the screen. """
        self.penIcon = Image(self.mousePos(), "PenIcon.gif")

    def colorRed(self):                                                     ##
        choice = self.choose(self.window, self.colorButtons())              ##
        return choice == "r"                                                ##
                                                                            ##
    def colorGreen(self):                                                   ###
        choice = self.choose(self.window, self.colorButtons())              ####
        return choice == "g"                                                #####
                                                                            ###### These check to see if the which color buttons are selected all return True
    def colorBlue(self):                                                    #####
        choice = self.choose(self.window, self.colorButtons())              ###
        return choice == "b"                                                ##
                                                                            ##
    def colorOrange(self):                                                  ##
        choice = self.choose(self.window, self.colorButtons())              ##
        return choice == "o"                                                ##

    def color(self):
        """ Checks to see which button returned True and sets the color of the line to that color.
            It returns this color """
        while True:
            color = 'black'
            if self.colorRed() == True:
                color = 'red'
            elif self.colorGreen() == True:
                color = 'green'
            elif self.colorBlue() == True:
                color = 'blue'
            elif self.colorOrange() == True:
                color = 'orange'
            return color

    def TTT(self, window):
        """ Work-in-progress TIC-TAC-TOE board for users to click on when they want (button to turn it on in the button panel) """
        TTTButton = Button(window, Point(500, 60), 100, 40, "Tic-tac-toe")
        v1 = Line(Point(100, 400), Point(100, 700))
        v2 = Line(Point(700, 400), Point(700, 700))
        h1 = Line(Point(250, 600), Point(550, 600))
        h2 = Line(Point(250, 500), Point(550, 500))
        if self.clycked(TTTButton):
            v1.draw(window)
            v2.draw(window)
            h1.draw(window)
            h2.draw(window)
        if self.clycked(TTTButton):
            v1.undraw()
            v2.undraw()
            h1.undraw()
            h2.undraw()

    def clycked(self, button):
        """ Returns the LABEL of the button in parameter if clicked """
        while True:
            p = self.window.getMouse()
            if button.clicked(p):
                return button.getLabel()

    def doc_nombre(self):
        """ Another work-in-progress to allow the user to name the doc.  Right now all it does is ask for the user input on click of the button """
        self.doc_name_text = Text(Point(65, 60), "Title Here")
        self.doc_name_button = Button(self.window,
                                      Point(65, 60),
                                      100,
                                      30,
                                      "{0}".format(self.doc_name_text.getText()))
        if self.clycked(self.doc_name_button):
            self.doc_name = input("Title Here: ")
            print("this works")
            self.doc_name_text.setText("{0}".format(self.doc_name))


    def appearance(self):
        """ This method draws a bunch of shapes to make the document more
            visually appealing (I hope). """
        self.top_banner = Rectangle(Point(0, 0), Point(1000, 40))
        self.top_banner.setFill("blue")
        self.top_banner.draw(self.window)
        self.button_banner = Rectangle(Point(0, 40), Point(1000, 80))
        self.button_banner.setFill("grey")
        self.button_banner.draw(self.window)

    def mousePos(self):
        """ Returns the coords of current mouse position """
        while True:
            return pyautogui.position()

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
        self.drawingbuttons.append([self.drawWidthIncreaseButton,
                                    self.drawWidthDecreaseButton])
        return self.drawingbuttons

    def colorButtons(self):
        """ Creates all the color buttons for the line color and adds them to a list """
        self.redButton = Button(self.window, Point(250, 60), 20, 20, "r")
        self.redButton.setFill("red") # Creates the red button
        self.blackButton = Button(self.window, Point(220, 60), 20, 20, "")
        self.blackButton.setFill("black") # Creates yellow button
        self.blueButton = Button(self.window, Point(130, 60), 20, 20, "b")
        self.blueButton.setFill("blue") # Creates blue button
        self.greenButton = Button(self.window, Point(160, 60), 20, 20, "g")
        self.greenButton.setFill("green") # Creates green button
        self.orangeButton = Button(self.window, Point(190, 60), 20, 20, "o")
        self.orangeButton.setFill("orange") # Creates orange button
        self.color_buttons = []
        self.color_buttons.append(self.redButton)
        self.color_buttons.append(self.blackButton)
        self.color_buttons.append(self.blueButton)
        self.color_buttons.append(self.greenButton)
        self.color_buttons.append(self.orangeButton)
        return self.color_buttons

    def closeButton(self):
        """ Creates the "X" button in the top left corner of the
            window.  It closes the program when clicked """
        self.X_button = Button(self.window, Point(20, 15), 15, 15, "X")
        # (Above) Creates 'X' button in top left corner
        self.X_button.setFill("red")
        return self.X_button

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
