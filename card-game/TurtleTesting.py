#!/usr/bin/python
import turtle
from TurtleClasses import (
    ResizeScreen,
    HpBar,
    BossHp,
    PlayerHp,
    SpellList,
    PlayerModel,
    BossModel
)
import time
import copy

# Setup turtle window
wn = turtle.Screen()
wn.bgcolor("#ffffff")
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
        "name": "Strings",
        "level": 1,
        "base": "",
        "baseDescription": "empty string",
        "requirement": "spongebob",
        "cards": ("sponge", "bob"),
        "suggestedMethods": ["+"],
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Lists - 1",
        "level": 1,
        "base": ["sea"],
        "baseDescription": "list, 1 element",
        "requirement": ["pineapple", "under the", "sea"],
        "cards": ("pineapple", "under the"),
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Lists - 2",
        "level": 1,
        "base": ["sea"],
        "baseDescription": "list, 1 element",
        "requirement": ["pineapple", 5, "sea"],
        "cards": ("pineapple", "under the", 5),
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Tuples",
        "level": 1,
        "base": "",
        "baseDescription": "empty string",
        "requirement": ("patrick", "starfish"),
        "cards": ("patrick", "starfish", ["bikini", "bottom"]),
        "damageOnSuccess": 6,
        "damageOnFail": 2
    },
    {
        "name": "Tuples and Lists",
        "level": 2,
        "base": [],
        "baseDescription": "empty list",
        "requirement": [("patrick", "starfish"), "is a hoe"],
        "cards": (("patrick", "starfish"), "is a hoe"),
        "damageOnSuccess": 8,
        "damageOnFail": 2
    },
    {
        "name": "List Looping",
        "level": 2,
        "base": ["spongebob","round","pants"],
        "baseDescription": "list, 3 elements",
        "requirement": ["spongebob", "square", "pants"],
        "cards": ("square", "bottom"),
        "damageOnSuccess": 8,
        "damageOnFail": 2
    },
    {
        "level": 2,
        "base": ("sponge"),
        "requirement": ("spg", "one"),
        "cards" : ("s", "p", "g"),
        "damageOnSuccess": 8,
        "damageOnFail": 2
    },
    {
        "level": 2,
        "base": "spongebab",
        "requirement": "spongebob",
        "cards": ("o", "b"),
        "damageOnSuccess": 8,
        "damageOnFail": 2
    },
    {
        "level": 3,
        "base": [("sponge", "bob"), "pants"],
        "requirement": [("spongebob"), "squarepants"],
        "cards": ("square"),
        "damageOnSuccess": 10,
        "damageOnFail": 2
    },
    {
        "level": 3,
        "base": [],
        "requirement": ["s", "sp", "spo", "spon", "spong", "sponge"],
        "cards": ("s", "sponge", "sp"),
        "damageOnSuccess": 10,
        "damageOnFail": 2
    },
    {
        "level": 3,
        "base": (("square"), ["pants"], "bab"),
        "requirement": ("bob", ("squarepants"), ["pants"]),
        "cards": ("o", "ob"),
        "damageOnSuccess": 10,
        "damageOnFail": 2
    },
    {
        "level": 3,
        "base": [("sponge", 1), ("bob", 2), ("sponge", 3), ("sponge", 4), ("sponge", 5)],
        "requirement": ["bob", "spongesponge", "bobbobbob", "bobbobbobbob", "bobbobbobbobbob"],
        "cards": ("sponge", "bob"),
        "damageOnSuccess": 10,
        "damageOnFail": 2
    }
]

# get highest level spell in Spells list
# print(max([spell["level"] for spell in Spells]))

selectedLevelSpells = []
selectedSpell = {}
codingFail = False
codingSuccess = False

gameState = "levelselection"
# cast = "initial"

playerChar = PlayerModel(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
bossChar = BossModel(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])

while True:
    if gameState == "levelselection":
        while gameState == "levelselection":
            selectLevel = input("input level")
            if selectLevel.isdigit():
                if int(selectLevel) > 0 and int(selectLevel) <= max([spell["level"] for spell in Spells]):
                    print("Level", selectLevel, "selected!")
                    selectedLevel = int(selectLevel)
                    displaySpellsByLevel = SpellList(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3], Spells, selectedLevel)
                    for spell in Spells:
                        if spell["level"] == selectedLevel:
                            selectedLevelSpells.append(spell)

                    gameState = "spellselection"
                else:
                    print("invalid level")
            else:
                print("level is an integer")

    elif gameState == "spellselection":
        while gameState == "spellselection":
            selectSpell = input("input spell index: ")
            if selectSpell.isdigit():
                selectSpell = int(selectSpell)
                if selectSpell >= 0 and selectSpell <= (len(selectedLevelSpells) - 1):
                    for i in range(len(selectedLevelSpells)):
                        if selectedLevelSpells[i] == selectedLevelSpells[selectSpell]:
                            selectedSpell = copy.deepcopy(selectedLevelSpells[selectSpell])

                            if type(selectedSpell["requirement"]) is str:
                                playerGoal = '"' + selectedSpell["requirement"] + '"'
                            else:
                                playerGoal = str(selectedSpell["requirement"])
                            if type(selectedSpell["base"]) is str:
                                playerBaseCast = '"' + selectedSpell["base"] + '"'
                            else:
                                playerBaseCast = str(selectedSpell["base"])

                            print("---")
                            print("Use Tab or 4 spaces to indent your code")
                            print("End code block by entering a line containing only '.'")
                            print("Arrow keys don't work to move your cursor.")
                            print("---")
                            print("  If you want to write a new code block, end this one")
                            print("then enter anything other than 'y' when prompted.")
                            print("---")
                            print("Write a block of code to make:")
                            print("  cast =", playerGoal)
                            print("---")
                            print("Currently,")
                            print("  cast =", playerBaseCast)

                            gameState = "getplayerinput"
                else:
                    print("invalid spell index")
            else:
                print("spell index is an integer")


    elif gameState == "getplayerinput":
        # print(selectedSpell["name"])
        # print(selectedSpell["base"])
        # print(selectedSpell["requirement"])
        # print("cards:", selectedSpell["cards"])

        cast = selectedSpell["base"]
        userCode = "initial"
        buffer = []
        while True:
            print(">>>", end="")
            line = input()
            if line == ".":
                userChoice = input("To enter new code block, just press Enter\nTo confirm, input 'y' and press Enter\n>>> ")
                if userChoice == "y":
                    break
                else:
                    line = "retry"
                    print("Previously entered code block removed.")
            if line != "retry":
                buffer.append(line)
            else:
                buffer = []
        # input("Press Enter to end turn.")

        for i in range(len(buffer)):
            if str(selectedSpell["requirement"]) in buffer[i] or '"' in buffer[i] or "'" in buffer[i]:
                codingFail = True
                print("fail in getplayerinput")
                print("cards not used")

        userCode = "\n".join(buffer)

        print("end of getplayerinput, printing userCode and cast")
        print(userCode)
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

        print("end of checkplayerinput, printing userCode and cast")
        print(userCode)
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