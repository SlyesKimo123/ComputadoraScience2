from random import randrange
from DieViewListCopy import DieView

class ColorDieView(DieView):
    """ Creates the graphics of the dice view and animation IN COLOR. Calls from DieView class """

    def setValue(self, value):
        """ Sets the dice values with the number values from the DieView class """
        self.value = value      # remember this value (inputted value)
        DieView.setValue(self, value) # call setValue from parent class

    def setColor(self, color):
        """ Allows user to set the color of the background. Called from RiskInterface """
        self.foreground = color
        self.setValue(self.value)

class Dice:
    """ Creates the functionality of the dice """

    def __init__(self):
        self.dice = [0]*2
        self.rollAll()

    def roll(self, which):
        """ Rolls the dice to have a new set of random values.
            The parameter 'which' tells the method how many dice to
            do this for """
        for pos in which: # 'which' parameter is a integer value
            self.dice[pos] = randrange(1,7)

    def rollAll(self):
        """ Rolls all dice at one time """
        self.roll(range(2))

    def values(self):
        """ Returns the values shown on the dice """
        return self.dice[:]

    def total(self):
        """ Returns the sum of the dice values """
        total = self.values()
        return int(total[0]) + int(total[1])

class RiskApp:
    """ The behind-the-scenes non-graphics related aspects of Risk Dice game """

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface
        self.score = 0

    def generate(self):
        """ Returns a generated number for the computer between 3 and 11 """
        self.gnum = randrange(3, 12)
        return  int(self.gnum)

    def h_or_l(self):
        """ Activates the 'Higher' and 'Lower' buttons (previously were not active)
            in order for the user to guess """
        self.interface.activate([self.interface.higher_b,
                                 self.interface.lower_b,
                                 self.interface.quit_b])

    def run(self):
        """ Starts the game when called on.  The game begins when the 'wantToPlay' method
            from the Interface returns True AND the score is more than or eqaul to zero """
        while self.interface.wantToPlay() and self.score >= 0:
            self.playRound() # Begins the series of events that make up one round
        self.interface.close() # if 'wantToPlay' did not return True or score is less than zero,
                               # the window will close

    def previousScore(self):
        """ Returns the score of the round that just happened in order to compare it
            to the score of the next round """
        roundscore = self.interface.puntos
        return roundscore

    def playRound(self):
        """ Plays the round.  This series of methods that are being called here are
            what make up one round, from the first to the last task that needs completion """
        self.interface.text_hidden() # fist thing that needs to be done is hiding the result texts
        gen_number = self.generate()
        self.interface.gen_text(gen_number) # first action is the computer generating rand. num
        self.interface.theScore(self.score) # sets the score to its new value
                                            # (if previous round completed)
        self.h_or_l()    # Activates H and L buttons
        self.interface.rectangles() # draws the two rectangles before dice roll
        self.doRolls() # does rolls BEFORE guess has been made

        diceroll = self.dice.total()
        check = self.interface.check(diceroll, gen_number)
        # The line above is the meaty method that checks to see if the user's guess is correct
        # and returns True if correct.  If incorrect, window closes and game is over
        if check == True: # Checks to see if the user's guess was correct
            self.score += 1 # If so, a point is added to the score
        self.interface.rectangle.undraw()
        self.interface.rectangle2.undraw()

    def doRolls(self):
        """ Rolls all the dice and returns the values of the dice """
        self.dice.rollAll()
        self.interface.setDice(self.dice.values())
