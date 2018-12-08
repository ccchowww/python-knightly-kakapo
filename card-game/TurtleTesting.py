#!/usr/bin/python
import turtle
from TurtleClasses import (
    ResizeScreen,
    HpBar,
    BossHp,
    PlayerHp
)
import time


# Setup turtle window
wn = turtle.Screen()
# wn.bgcolor("#EEEEEC")
wn.title("Card Game")
# Set window to percentages to get pixels
wn.setup(width=0.7,height=0.9) #7:9
wnWidth = wn.window_width()
wnHeight = wn.window_height()

# Get new dimensions that will be compatible with any user's screen.
newScreen = ResizeScreen(wnWidth, wnHeight)

# return from ResizeScreen:
#   newScreen = (effectiveWidth, effectiveHeight, widthUnit, heightUnit)
newScreenWidth = newScreen[0]
newScreenHeight = newScreen[1]

# Convert window to compatible dimensions
wn.setup(width=newScreenWidth,height=newScreenHeight)
# Set coords, coords start at Top Left, end at Bottom Right
wn.setworldcoordinates(0,newScreenHeight,newScreenWidth,0)

# screen width: 0 - 90 units used by hp bar
BossHp = BossHp(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
BossCurrentHp = 30

PlayerHp = PlayerHp(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
PlayerCurrentHp = 30

# time.sleep(0.3)
# BossHp.decrement(2, BossCurrentHp)


def main():
    
    while True:
        getInput = input()
        if getInput == "hib":
            BossHp.decrement(2, BossCurrentHp)
        elif getInput == "heb":
            BossHp.increment(2, BossCurrentHp)
        elif getInput == "hip":
            PlayerHp.decrement(2, PlayerCurrentHp)
        elif getInput == "hep":
            PlayerHp.increment(2, PlayerCurrentHp)
        elif getInput == "q":
            break

main()



# preventFallingOff = input("end of file\n")