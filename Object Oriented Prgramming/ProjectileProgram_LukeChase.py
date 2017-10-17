import math

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

def getInputs():
    angle = eval(input("Enter the launch angle por favor (in degrees): \n"))
    velocity = eval(input("Enter the velocity monguir (in meters/second): \n"))
    height0 = eval(input("Enter the initial height pongü (in meters) \n"))
    time = eval(input("Enter time interval between calculations if you may: \n"))
    return angle, velocity, height0, time

def main():
    angle, velocity, height0, time = getInputs()
    p = Projectile(angle, velocity, height0)
    while p.getY() >= 0:
        p.update(time)
    print("\nDistance travelled: {0:0.1f} meters.".format(p.getX()))

main()
