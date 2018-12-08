import turtle
import math
import time

"""
Colour Palette:
    BossHp:
        HpUnit = #EB001B
        Limiter = #BE0016

        brightest to darkest
        1. #FB001D
        2. #EB001B
        3. #BE0016
        4. #940011
        5. #64000C
    PlayerHp:
        HpUnit = #6BE400
        Limiter = #438D00

        brightest to darkest
        1. #78FE00
        2. #75F800
        3. #6BE400
        4. #57B800
        5. #438D00
    Spell List
        Borders = 
        Text = 
    
        brightest to darkest
        1. B027FC
        2. A708FF
        3. 9400E5
        4. 6D00A8
        5. 560085
"""

def ResizeScreen(width, height):
    screenWidthUnit = width // 140
    screenHeightUnit = height // 180

    effectiveScreenWidth = screenWidthUnit * 140
    effectiveScreenHeight = screenHeightUnit * 180

    return (effectiveScreenWidth, effectiveScreenHeight, screenWidthUnit, screenHeightUnit)

class SpellList(turtle.Turtle):
    def __init__(self, width, height, spellDictionary):
        turtle.Turtle.__init__(self)

        self.hideturtle()
        self.penup()
        self.speed(0)

# width and height only occasionally needed for placement, in HpBar, only used by PlayerHp to position
#   off bottom edge of window
class HpBar(turtle.Turtle):
    def __init__(self, screenObject, width, height, widthUnit, heightUnit):
        turtle.Turtle.__init__(self)

        self.hideturtle()
        self.penup()
        self.speed(0)

        self.screenWidthUnit = widthUnit
        self.screenHeightUnit = heightUnit

        self.hpUnitWidth = self.screenWidthUnit * 2
        self.hpUnitHeight = self.screenHeightUnit * 6
        self.hpUnitGap = self.screenWidthUnit

        # (y-axis, x-axis)
        screenObject.register_shape("HpUnit",
            (
            (0, 0),
            (self.screenHeightUnit*6, 0),
            (self.screenHeightUnit*6, self.screenWidthUnit*2),
            (0, self.screenWidthUnit*2),
            )
        )
        screenObject.register_shape("Limit",
            (
            (0, 0),
            (self.screenHeightUnit*6 + 4, 0),
            (self.screenHeightUnit*6 + 4, 2),
            (0, 2)
            )
        )

    def decrement(self, units, currentHp):
        if (units > currentHp):
            hitpoints = currentHp
        else:
            hitpoints = units

        # Times to flash hp units to be removed.
        count = 2
        while count > 0:
            for i in range(hitpoints):
                self.undo()
                self.undo()
            time.sleep(0.3)
            for j in range(hitpoints):
                self.stamp()
                self.forward(self.hpUnitWidth + self.hpUnitGap)
            time.sleep(0.1)
            count -= 1

        for i in range(hitpoints):
            self.undo()
            self.undo()

    def increment(self, units, currentHp):
        # Times to flash hp units to increment
        count = 2
        while count > 0:
            for j in range(units):
                self.stamp()
                self.forward(self.hpUnitWidth + self.hpUnitGap)
            time.sleep(0.1)
            for i in range(units):
                self.undo()
                self.undo()
            time.sleep(0.1)
            count -= 1

        for j in range(units):
            self.stamp()
            self.forward(self.hpUnitWidth + self.hpUnitGap)

class BossHp(HpBar):
    def __init__(self, screenObject, width, height, widthUnit, heightUnit):
        HpBar.__init__(self, screenObject, width, height, widthUnit, heightUnit)

        startPos = (self.screenWidthUnit, 0)
        self.setpos(startPos)

        self.color("#BE0016")
        self.shape("Limit")
        self.stamp()
        self.forward(6)

        self.sety(self.ycor() + 2)

        self.shape("HpUnit")
        self.color("#EB001B")
        for i in range(30):
            self.stamp()
            self.forward(self.hpUnitWidth + self.hpUnitGap)
        endLimit = self.clone()
        endLimit.shape("Limit")
        endLimit.color("#BE0016")
        endLimit.sety(self.ycor() - 2)
        endLimit.setx(self.xcor() - self.hpUnitGap + 4)
        endLimit.stamp()


class PlayerHp(HpBar):
    def __init__(self, screenObject, width, height, widthUnit, heightUnit):
        HpBar.__init__(self, screenObject, width, height, widthUnit, heightUnit)

        startPos = (self.screenWidthUnit, height - self.hpUnitHeight - self.screenHeightUnit*2)
        self.setpos(startPos)

        self.shape("Limit")
        self.color("#438D00")
        self.stamp()
        self.forward(6)

        self.sety(self.ycor() + 2)

        self.shape("HpUnit")
        self.color("#6BE400")
        for i in range(30):
            self.stamp()
            self.forward(self.hpUnitWidth + self.hpUnitGap)
        endLimit = self.clone()
        endLimit.shape("Limit")
        endLimit.color("#438D00")
        endLimit.sety(self.ycor() - 2)
        endLimit.setx(self.xcor() - self.hpUnitGap + 4)
        endLimit.stamp()