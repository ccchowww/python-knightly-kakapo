#!/usr/bin/python
import turtle
from TurtleClasses import (
    ResizeScreen,
    HpBar,
    BossHp,
    PlayerHp
)
import time
import copy

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

# class GameData():
#     def __init__(self,)

Spells = [
    {
        "name": "Lvl 1 - Strings",
        "base": "",
        "baseType": "empty string",
        "requirement": "spongebob",
        "cards": ("sponge", "bob"),
        "suggestedMethods": ["+"],
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Lvl 1 - Lists",
        "base": ["sea"],
        "baseType": "list, 1 element",
        "requirement": ["pineapple", "under the", "sea"],
        "cards": ("pineapple", "under the"),
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Lvl 1 - Tuples",
        "base": "",
        "baseType": "empty string",
        "requirement": ("patrick", "starfish"),
        "cards": ("patrick", "starfish"),
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Lvl 2 - Tuples and Lists",
        "base": [],
        "baseType": "empty list",
        "requirement": [("patrick", "starfish"), "is a hoe"],
        "cards": (("patrick", "starfish"), "is a hoe"),
        "damageOnSuccess": 8,
        "damageOnFail": 2
    }
]

selectedSpell = {}
codingFail = False
codingSuccess = False

gameState = "spellselection"
# cast = "initial"

while True:
    if gameState == "spellselection":
        while gameState == "spellselection":
            selectSpell = int(input("input spell index: "))
            for i in range(len(Spells)):
                if Spells[i] == Spells[selectSpell]:
                    selectedSpell = copy.deepcopy(Spells[selectSpell])
                    # cast = selectedSpell["base"]

                    gameState = "getplayerinput"

    elif gameState == "getplayerinput":
        print(selectedSpell["name"])
        print(selectedSpell["base"])
        print(selectedSpell["requirement"])
        print("cards:", selectedSpell["cards"])
        numberOfCards = len(selectedSpell["cards"])

        cast = selectedSpell["base"]
        userCode = "initial"
        buffer = []
        while True:
            print(">>>", end="")
            line = input()
            if line == ".":
                break
            # for i in range(numberOfCards):
            #     if "c" + str(i) in line:
            #         line = line.replace("c"+str(i), selectedSpell["cards"][i])
            # print(line)
            buffer.append(line)
            # userCode = "\n".join(buffer)
        input("Press Enter to end turn")

        for i in range(len(buffer)):
            if str(selectedSpell["requirement"]) in buffer[i]:
                codingFail = True
                print("fail in getplayerinput")
                print("cards not used")

        userCode = "\n".join(buffer)

        print("end of getplayerinput",userCode)
        print(cast)
        gameState = "checkplayerinput"

    elif gameState == "checkplayerinput":
        # check fails
        if codingFail:
            print("fail before checkplayerinput")
            pass
        else:
            # replace c0, c1, ... with what is in cards[0], cards[1], ...
            try:
                for i in range(len(selectedSpell["cards"])):
                    if "c"+str(i) in userCode:
                        if type(selectedSpell["cards"][i]) is str:
                            userCode = userCode.replace("c"+str(i), "'" + selectedSpell["cards"][i] + "'")
                        else:
                            userCode = userCode.replace("c"+str(i), str(selectedSpell["cards"][i]))
                exec(compile(userCode, "<string>", "exec"), globals())

            except:
                codingFail = True
                print("fail in except block")
            else:
                if cast == selectedSpell["requirement"]:
                    codingSuccess = True
                else:
                    codingFail = True
                    print("fail in try-else-if block")

        print("end of checkplayerinput >>>", userCode)
        print(cast)
        gameState = "castspells"

    elif gameState == "castspells":
        if codingFail:
            damage = selectedSpell["damageOnFail"] 

            PlayerHp.decrement(damage, PlayerCurrentHp)
            PlayerCurrentHp -= damage
        elif codingSuccess:
            damage = selectedSpell["damageOnSuccess"]

            BossHp.decrement(damage, BossCurrentHp)
            BossCurrentHp -= damage

        if PlayerCurrentHp <= 0:
            print("boss win")
            break
        elif BossCurrentHp <= 0:
            print("player win")
            break

        codingFail = False
        codingSuccess = False

        gameState = "spellselection"

# getInput = input()
# if getInput == "hib":
#     BossHp.decrement(2, BossCurrentHp)
# elif getInput == "heb":
#     BossHp.increment(2, BossCurrentHp)
# elif getInput == "hip":
#     PlayerHp.decrement(2, PlayerCurrentHp)
# elif getInput == "hep":
#     PlayerHp.increment(2, PlayerCurrentHp)
# elif getInput == "q":
#     break



# preventFallingOff = input("end of file\n")