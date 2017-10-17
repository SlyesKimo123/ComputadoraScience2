import math

def main():
    angle = eval(input("Enter the launch angle por favor (in degrees): \n"))
    velocity = eval(input("Enter the velocity monguir (in meters/second): \n"))
    height0 = eval(input("Enter the initial height pongü (in meters) \n"))
    time = eval(input("Enter time interval between calculations if you may: \n"))

    xpos = 0.0
    ypos = height0

    theta = math.radians(angle)
    xvel = velocity * math.cos(theta)
    yvel = velocity * math.sin(theta)

    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2
        yvel = yvel1

    print("\nDistance travelled: {0:0.1f} meters.".format(xpos))

main()
