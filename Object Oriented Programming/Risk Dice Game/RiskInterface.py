# riskdicegame.py

##############################
#                            #
#        Version 5.0         #
#                            #
##############################

""" The aim of this project is to create a unique dice game using classes.
    Risk Dice Game is a 100% original game. """

import time
from graphics import *
from RiskBackup import ColorDieView, RiskApp, Dice
from ButtonProgramCOPY import Button

class RiskInterface:
    """" Graphics-related methods of Risk dice game """

    def __init__(self):
        self.win = GraphWin("Risk Dice", 600, 400)
        self.win.setBackground("yellow1")
        banner = Text(Point(300,30), "¡Risk Dice Game!")
        banner.setSize(24)
        banner.setFill("blue")
        banner.setStyle("bold")
        banner.draw(self.win)
        intro = Text(Point(300, 240),
                "Rules: The computer picks a number between 3-11.  The player picks the option of higher or lower.\n"
                "Two dice are rolled. If the number rolled matches the player's guess of higher or lower than the given number,\n"
                "then the player gets a point.  If the player guesses wrong then the game is over.\n" )
        intro.setSize(12)
        intro.draw(self.win)
        self.equal = Text(Point(100, 100), "The numbers were equal! Roll again.")
        self.equal.setSize(12)
        self.equal.draw(self.win)
        self.correct = Text(Point(100, 120), "You are correct!  You get a punto!")
        self.correct.setSize(12)
        self.correct.draw(self.win)
        self.wrong = Text(Point(100, 140), "You guessed wrong!  Game Over!")
        self.wrong.setSize(12)
        self.wrong.draw(self.win)
        self.text_hidden()
        self.num = Text(Point(300, 170), " ")
        self.num.setSize(18)
        self.num.draw(self.win)
        self.p = Text(Point(50, 10), " ")
        self.p.setSize(14)
        self.p.draw(self.win)
        self.createDice(Point(467.5, 100), 75)
        self.game = Text(Point(290, 300), "What's your pick? Higher or Lower?")
        self.game.setSize(14)
        self.game.draw(self.win)
        self.buttons = []
        self.gen_b = Button(self.win, Point(300, 350), 200, 40, "Generate Number")
        self.buttons.append(self.gen_b)
        self.higher_b = Button(self.win, Point(450, 350), 50, 40, "Higher")
        self.buttons.append(self.higher_b)
        self.lower_b = Button(self.win, Point(150, 350), 50, 40, "Lower")
        self.buttons.append(self.lower_b)
        self.quit_b = Button(self.win, Point(570, 20), 40, 30, "Quit")
        self.buttons.append(self.quit_b)
        self.points = Text(Point(50, 50), "Score: 0")
        self.points.setSize(18)
        self.points.draw(self.win)

    def createDice(self, center, size):
        """ Creates the two dice and their position """
        center.move(-3*size,0)
        self.dice = []
        for i in range(2):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def rectangles(self):
        """ Draws two rectangles over the dice to hide the values of the dice
            until the user's guess has been made """
        self.rectangle = Rectangle(Point(205, 70), Point(280, 130))
        self.rectangle.setFill("red")
        self.rectangle.draw(self.win)

        self.rectangle2 = Rectangle(Point(318, 70), Point(393, 130))
        self.rectangle2.setFill("red")
        self.rectangle2.draw(self.win)

    def gen_text(self, num):
        """ Creates the text of the generated number for the start of the round """
        self.num.setText("The number is {0}.".format(num))

    def theScore(self, amount):
        """ Creates the text of the score in the upper left corner """
        self.points.setText("Score: {0}".format(amount))

    def hide(self, text):
        """ Hides the text given for the parameter by setting it as background color """
        text.setTextColor("yellow1")

    def show(self, text):
        """ Un-hides the text given in the parameter by setting its color (back) to black """
        text.setTextColor("black")

    def text_hidden(self):
        """ Hides the text that is displayed according to whether the user
            guessed correctly, incorrectly, or the numbers were equal.  This
            is called on first when roundBegins to hide these text phrases until
            they are needed """
        self.hide(self.equal)
        self.hide(self.correct)
        self.hide(self.wrong)

    def setDice(self, values):
        """ Creates the two dice with random values. Calls from class Dice """
        for i in range(2):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        """ Returns True if the user clicks the 'Generate Number' button,
            which starts the round and the game """
        ans = self.choose(["Generate Number", "Quit"])
        return ans == "Generate Number"

    def close(self):
        """ Closes window """
        self.win.close()

    def choose(self, choices):
        """ Activates the button(s) given for the parameter and deactivates those
            that are not needed at the time when the method is callec"""
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def activate(self, buttons):
        """ Activates button in self.buttons """
        for b in self.buttons:
            b.activate()

    def deactivate(self, buttons):
        """ Deactivates button in self.buttons """
        for b in self.buttons:
            b.deactivate()

    def clicked(self, buttons):
        """ Returns the button that was clicked """
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b

    def check(self, values, gnum):
        """ Checks to see if the user's guess was correct and shows the result.
            Window closes if wrong and starts the next round if correct """
        b = self.clicked(self.higher_b), self.clicked(self.lower_b)
        for i in b:
            if i.getLabel() == "Higher":
                if gnum < values:
                    self.show(self.correct) # user's guess is correct
                    return True
                elif gnum == values: # values are equal
                    self.show(self.equal)
                else:
                    self.show(self.wrong) # user's guess is wrong
                    time.sleep(1)
                    self.close()
            elif i.getLabel() == "Lower":
                if gnum > values:
                    self.show(self.correct) # user's guess is correct
                    return True
                elif gnum == values: # values are equal
                    self.show(self.equal)
                else:
                    self.show(self.wrong) # user's guess is wrong
                    time.sleep(1)
                    self.close()

# Defines interface and riskApp.  Calls both classes to begin the program
inter = RiskInterface()
app = RiskApp(inter)
app.run()
