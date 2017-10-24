# dieview.py
from graphics.py import *, GraphWin, Point
from random import randrange
from button import Buton
from dieview import diview
class DieView:
    '''Dieview is a widget that displays a graphical representation of a standard sixsided die'''

    def __init__(self, win, center, size):
        '''Create a view of a die, eg:
        d1 = Dieview(myWin, Point(40, 50), 20)
        creates die centered at 40, 50 having sides of length 20'''

        #first define some standard values
        self.win = win             #save this for drawing pips later
        self.background = 'white'  #color of die face
        self.foreground = 'black'
        self.psize = .1*size
        hsize = size/2.0
        offset = .6*hsize

        cx, cy = center.getX(), center.getY()
        p1 = Point(cz=hsize, cy-hsize)
        p2 = Point(cx+size, cy-size)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pip1 = self.makePip(cx - offset, cy - offset)
        self.pip2 = self.makePip(cx - offset, cy)
        self.pip3 = self.makePip(cx - offset, cy + offset)
        self.pip4 = self.makePip(cx , cy )
        self.pip5 = self.makePip(cx + offset, cy - offset)
        self.pip6 = self.makePip(cx - offset, cy )
        self.pip7 = self.makePip(cx + offset, cy + offset)

        self.setValue(1)

    def __makePip(self, x, y):
        'internal helper method to draw pip'
        pip = Circle(Point(x, y, self.psize))
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        'display die value'
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 6:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)




def main():
    win = GraphWin("dice roller")
    win.setCoords(0,0,10,10)
    win.setBackground("green2")
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Pint(5, 1), 2, 1, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()
    win.close()
