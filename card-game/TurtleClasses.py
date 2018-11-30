import turtle
import math
import time

class HpBar(turtle.Turtle):
    def __init__(self, width, height, screenObject):
        turtle.Turtle.__init__(self)

        self.penup()
        self.speed(0)

        self.hpBarWidthUnit = width // 100
        self.hpBarHeightUnit = height // 100
        # print(self.hpBarWidthUnit, self.hpBarHeightUnit)


        self.hpUnitWidth = self.hpBarWidthUnit * 5
        self.hpUnitHeight = self.hpBarHeightUnit * 5
        self.hpUnitGap = self.hpBarWidthUnit
        # self.hpUnitGap = self.hpBarHeightUnit

        screenObject.register_shape("HpUnit",
            (
            (0, 0),
            (self.hpUnitWidth, 0),
            (self.hpUnitWidth, self.hpUnitHeight),
            (0, self.hpUnitHeight),
            )
        )
        self.shape("HpUnit")

class BossHp(HpBar):
    def __init__(self, width, height, screenObject):
        # turtle.Turtle.__init__(self)
        HpBar.__init__(self, width, height, screenObject)

        # print(self.hpBarWidthUnit, self.hpBarHeightUnit)

        self.hideturtle()
        startPos = (self.hpBarWidthUnit*3, self.hpBarHeightUnit*2)
        self.setpos(startPos)

        self.color("#BE0016")

        for i in range(10):
            self.stamp()
            self.forward(self.hpUnitWidth + self.hpUnitGap)

    def fancyLine(self, xcoord, ycoord, units):
        fancyLine = turtle.Turtle()

        fancyLine.speed(0)
        fancyLine.hideturtle()
        fancyLine.penup()
        fancyLine.color("#FB001D")
        fancyLine.width(4)

        fancyLine.setpos(xcoord - self.hpBarWidthUnit, ycoord - self.hpBarHeightUnit)

        fancyLine.pendown()
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() + 1*self.hpBarHeightUnit)
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() - self.hpBarHeightUnit)
        fancyLine.speed(5)
        fancyLine.backward((self.hpUnitWidth + self.hpUnitGap)*units)
        fancyLine.speed(0)
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() + 1*self.hpBarHeightUnit)
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() - self.hpBarHeightUnit)
        return fancyLine

    def decrement(self, units, currentHp):
        if (units > currentHp):
            hitpoints = currentHp
        else:
            hitpoints = units

        redLine = BossHp.fancyLine(self, BossHp.xcor(self), BossHp.ycor(self), hitpoints)

        count = 2
        while count > 0:
            for i in range(hitpoints):
                self.undo()
                self.undo()
            time.sleep(0.3)
            for j in range(hitpoints):
                self.stamp()
                self.forward(self.hpBarWidthUnit * 6)
            time.sleep(0.1)
            count -= 1

        for i in range(hitpoints):
            self.undo()
            self.undo()

        time.sleep(0.1)
        redLine.clear()

class PlayerHp(HpBar):
    def __init__(self, width, height, screenObject):
        HpBar.__init__(self, width, height, screenObject)

        self.hideturtle()
        startPos = (self.hpBarWidthUnit*3, self.hpBarHeightUnit*93)
        self.setpos(startPos)

        self.color("#6BE400")

        for i in range(10):
            self.stamp()
            self.forward(self.hpUnitWidth + self.hpUnitGap)

    def fancyLine(self, xcoord, ycoord, units):
        fancyLine = turtle.Turtle()

        fancyLine.speed(0)
        fancyLine.hideturtle()
        fancyLine.penup()
        fancyLine.color("#428D00")
        fancyLine.width(4)

        fancyLine.setpos(xcoord - self.hpBarWidthUnit, ycoord - self.hpBarHeightUnit)

        fancyLine.pendown()
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() + 1*self.hpBarHeightUnit)
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() - self.hpBarHeightUnit)
        fancyLine.speed(5)
        fancyLine.backward((self.hpUnitWidth + self.hpUnitGap)*units)
        fancyLine.speed(0)
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() + 1*self.hpBarHeightUnit)
        fancyLine.setpos(fancyLine.xcor(), fancyLine.ycor() - self.hpBarHeightUnit)
        return fancyLine


    def decrement(self, units, currentHp):
        if (units > currentHp):
            hitpoints = currentHp
        else:
            hitpoints = units

        redLine = PlayerHp.fancyLine(self, PlayerHp.xcor(self), PlayerHp.ycor(self), hitpoints)

        count = 2
        while count > 0:
            for i in range(hitpoints):
                self.undo()
                self.undo()
            time.sleep(0.3)
            for j in range(hitpoints):
                self.stamp()
                self.forward(self.hpBarWidthUnit * 6)
            time.sleep(0.1)
            count -= 1

        for i in range(hitpoints):
            self.undo()
            self.undo()

        time.sleep(0.1)
        redLine.clear()
