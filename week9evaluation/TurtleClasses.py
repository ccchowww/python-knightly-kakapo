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

Object sizes on screen:
    Hpbars:
        Boss:
            width 0 - 93 screenWidthUnit
            height 0 - 6 screenHeightUnit + 4
        Player:
            width 0 - 93 screenWidthUnit
            height 172 - 178 screenHeightUnit + 4
"""

def ResizeScreen(width, height):
    screenWidthUnit = width // 140
    screenHeightUnit = height // 180

    effectiveScreenWidth = screenWidthUnit * 140
    effectiveScreenHeight = screenHeightUnit * 180

    return (effectiveScreenWidth, effectiveScreenHeight, screenWidthUnit, screenHeightUnit)

class ScreenUnits():
    def __init__(self, screenWidth, screenHeight, widthUnit, heightUnit):
        self.screenWidthUnit = widthUnit
        self.screenHeightUnit = heightUnit
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

class PlayerModel(turtle.Turtle, ScreenUnits):
    def __init__(self, wn, width, height, widthUnit, heightUnit):
        turtle.Turtle.__init__(self)
        ScreenUnits.__init__(self, width, height, widthUnit, heightUnit)

        self.hideturtle()
        self.penup()
        self.speed(0)

        wn.register_shape("./images/player.gif")

        self.shape("./images/player.gif")

        self.setpos(self.screenWidthUnit*20, height - self.screenHeightUnit*40)

        self.showturtle()
        self.speed(2)
        # self.goto(self.xcor()-20, self.ycor())
        # self.goto(self.xcor()+40, self.ycor())

class BossModel(turtle.Turtle, ScreenUnits):
    def __init__(self, wn, width, height, widthUnit, heightUnit):
        turtle.Turtle.__init__(self)
        ScreenUnits.__init__(self, width, height, widthUnit, heightUnit)

        self.hideturtle()
        self.penup()
        self.speed(0)

        wn.register_shape("./images/boss.gif")

        self.shape("./images/boss.gif")

        self.setpos(self.screenWidthUnit*71, self.screenHeightUnit*43)

        self.showturtle()
        self.speed(2)
        # self.goto(self.xcor()-20, self.ycor())
        # self.goto(self.xcor()+40, self.ycor())
        

class SpellList(turtle.Turtle, ScreenUnits):
    def __init__(self, screenObject, width, height, widthUnit, heightUnit, spellDictionary, chosenLevel):
        turtle.Turtle.__init__(self)
        ScreenUnits.__init__(self, width, height, widthUnit, heightUnit)

        self.hideturtle()
        self.penup()
        self.speed(0)

        self.spellsToShow = []

        for spell in spellDictionary:
            for field in spell:
                if field == "level":
                    if spell[field] == chosenLevel:
                        self.spellsToShow.append(spell)

        startPos = (self.screenWidthUnit*95, self.screenHeightUnit*6 + 4)
        self.setpos(startPos)

        screenObject.register_shape("SpellSeparator",
            (
            (0,0),
            (self.screenWidthUnit,0),
            (self.screenWidthUnit,self.screenHeightUnit*162),
            (0,self.screenHeightUnit*162)
            )
        )
        # screenObject.register_shape("SpellSectionSeparator",
        #     (
        #     (-self.screenWidthUnit*6,-self.screenHeightUnit*2),
        #     (self.screenWidthUnit*7,-self.screenHeightUnit*2),
        #     (self.screenWidthUnit*7,math.floor(-self.screenHeightUnit*2.5)),
        #     (-self.screenWidthUnit*6,math.floor(-self.screenHeightUnit*2.5))
        #     )
        # )

        # Font sizes, biggest to smallest
        self.fontHeader = math.floor(self.screenWidthUnit*2.5)
        self.fontH1 = math.floor(self.screenWidthUnit*2.0)
        self.fontH2 = math.floor(self.screenWidthUnit*1.8)
        self.fontH3 = math.floor(self.screenWidthUnit*1.6)
        self.fontH4 = math.floor(self.screenWidthUnit*1.4)

        self.shape("SpellSeparator")
        self.color("#6D00A8")

        # stamp separator
        self.setheading(90)
        self.stamp()

        spellsHeaderPos = (self.screenWidthUnit*99, self.screenHeightUnit*6)
        self.setpos(spellsHeaderPos)
        self.write("Level: "+str(self.spellsToShow[0]["level"]), font=("Arial", self.fontHeader, "bold"))
        self.setpos(self.xcor() + self.screenWidthUnit*2, self.ycor() + self.screenHeightUnit*3)

        spellListStartPos = (self.screenWidthUnit*97, self.screenHeightUnit*7 + (self.screenHeightUnit*6 + 4))
        self.setpos(spellListStartPos)

        self.shape("triangle")
        self.shapesize(0.6,0.6,1)
        self.setheading(0)

        for i in range(len(self.spellsToShow)):
            spellIndex = str(i)
            if type(self.spellsToShow[i]["base"]) is str:
                spellBase = '"' + self.spellsToShow[i]["base"] + '"'
            else:
                spellBase = str(self.spellsToShow[i]["base"])
            if type(self.spellsToShow[i]["requirement"]) is str:
                spellRequirement = '"' + self.spellsToShow[i]["requirement"] + '"'
            else:
                spellRequirement = str(self.spellsToShow[i]["requirement"])

            spellCards = {}
            for j in range(len(self.spellsToShow[i]["cards"])):
                if type(self.spellsToShow[i]["cards"][j]) is str:
                    spellCards["c"+str(j)] = '"' + self.spellsToShow[i]["cards"][j] + '"'
                else:
                    spellCards["c"+str(j)] = self.spellsToShow[i]["cards"][j]

            # Stamp arrow beside spell index
            self.color("#6D00A8")
            self.setpos(self.xcor() - self.screenWidthUnit*2, self.ycor() - self.screenHeightUnit*3)
            self.stamp()
            self.setpos(self.xcor() + self.screenWidthUnit*2, self.ycor() + self.screenHeightUnit*3)
            self.color("#9400E5")
            self.write("Spell: " + spellIndex, font=("Arial", self.fontH2, "bold"))
            self.setpos(self.xcor(), self.ycor() + self.screenHeightUnit*6)

            self.write("Goal : " + spellRequirement, font=("Arial", self.fontH2, "bold"))
            self.setpos(self.xcor(), self.ycor() + self.screenHeightUnit*6)

            self.write("Start : " + spellBase, font=("Arial", self.fontH2, "normal"))
            self.setpos(self.xcor() + self.screenWidthUnit*2, self.ycor() + self.screenHeightUnit*6)

            self.write("Cards :", font=("Arial", self.fontH2, "normal"))
            self.setpos(self.xcor(), self.ycor() + self.screenHeightUnit*5)

            self.setpos(self.xcor() + self.screenWidthUnit*3, self.ycor())
            for card in spellCards:
                self.write(card + " | "+ str(spellCards[card]), font=("Arial", self.fontH2, "normal"))
                self.setpos(self.xcor(), self.ycor() + self.screenHeightUnit*5)

            # self.color("#b567e0")
            # self.stamp()
            # self.color("#6D00A8")
            self.setpos(self.xcor() - self.screenWidthUnit*5, self.ycor() + self.screenHeightUnit*4)
            # self.setpos(self.xcor(), self.ycor() + self.screenHeightUnit*4)

            # self.write("Description: " + spellBaseDescription, font=("Arial", self.fontH4, "normal"))
            # self.setpos(self.xcor() - self.screenWidthUnit*2, self.ycor() + self.screenHeightUnit*4)


# width and height only occasionally needed for placement, in HpBar, only used by PlayerHp to position
#   off bottom edge of window
class HpBar(turtle.Turtle, ScreenUnits):
    def __init__(self, screenObject, width, height, widthUnit, heightUnit):
        turtle.Turtle.__init__(self)
        ScreenUnits.__init__(self, width, height, widthUnit, heightUnit)

        self.hideturtle()
        self.penup()
        self.speed(0)

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
            time.sleep(0.2)
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