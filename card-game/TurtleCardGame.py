#!/usr/bin/python
import turtle
from TurtleClasses import (
    ResizeScreen,
    HpBar,
    BossHealth,
    PlayerHealth,
    SpellList,
    PlayerModel,
    BossModel,
    DrawSpell
)
import time
import copy

# # Setup turtle window
# wn = turtle.Screen()
# wn.title("Card Game")
# # Set window to percentages to get pixels
# wn.setup(width=0.7,height=0.9) #7:9
# wnWidth = wn.window_width()
# wnHeight = wn.window_height()

# # Get new dimensions that will be compatible with any user's screen.
# newScreen = ResizeScreen(wnWidth, wnHeight)

# # return from ResizeScreen:
# #   newScreen = (effectiveWidth, effectiveHeight, widthUnit, heightUnit)
# newScreenWidth = newScreen[0]
# newScreenHeight = newScreen[1]
# print(newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# # Convert window to compatible dimensions
# wn.setup(width=newScreenWidth,height=newScreenHeight)
# # Set coords, coords start at Top Left, end at Bottom Right
# wn.setworldcoordinates(0,newScreenHeight,newScreenWidth,0)
# wn.bgcolor("#f7f7f7")

Spells = [
    {
        "name": "Strings",
        "level": 1,
        "base": "",
        "baseDescription": "empty string",
        "requirement": "spongebob",
        "cards": ("sponge", "bob"),
        "suggestedMethods": ["+"],
        "damageOnSuccess": 8,
        "damageOnFail": 10
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
        "name": "List Looping",
        "level": 2,
        "base": ["spongebob","round","pants"],
        "baseDescription": "list, 3 elements",
        "requirement": ["spongebob", "square", "pants"],
        "cards": ("square", "bottom"),
        "damageOnSuccess": 10,
        "damageOnFail": 14
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
        "level": 2,
        "base": ("sponge"),
        "requirement": ("spg", "one"),
        "cards" : ("s", "p", "g"),
        "damageOnSuccess": 8,
        "damageOnFail": 2
    },
    {
        "level": 3,
        "base": [("sponge", "bob"), "pants"],
        "requirement": [("spongebob"), "squarepants"],
        "cards": ("squa", "re"),
        "damageOnSuccess": 15,
        "damageOnFail": 20
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
    # Spells used to test game
    # {
    #     "level": 3,
    #     "base": (("test"), ["test"]),
    #     "requirement": "balls",
    #     "cards": ["balls"],
    #     "damageOnSuccess": 30,
    #     "damageOnFail": 30
    # },
    # {
    #     "level": 2,
    #     "base": (("test"), ["test"]),
    #     "requirement": "balls",
    #     "cards": ["balls"],
    #     "damageOnSuccess": 30,
    #     "damageOnFail": 30
    # },
    # {
    #     "level": 1,
    #     "base": (("test"), ["test"]),
    #     "requirement": "balls",
    #     "cards": ["balls"],
    #     "damageOnSuccess": 30,
    #     "damageOnFail": 30
    # },
    {
        "level": 3,
        "base": [("spg", 1), ("bob", 2), ("spg", 3), ("spg", 4)],
        "requirement": ["bob", "spgspg", "bobbobbob", "bobbobbobbob"],
        "cards": ("sponge", "bob"),
        "damageOnSuccess": 10,
        "damageOnFail": 2
    }
]

# get highest level spell in Spells list
# print(max([spell["level"] for spell in Spells]))

# selectedLevelSpells = []
# selectedSpell = {}
# codingFail = False
# codingSuccess = False

# BossHp = BossHp(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# BossCurrentHp = 30

# PlayerHp = PlayerHp(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# PlayerCurrentHp = 30

# playerChar = PlayerModel(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# bossChar = BossModel(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# drawSpell = DrawSpell(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# selectedLevelSpells = []
# selectedSpell = {}
# codingFail = False
# codingSuccess = False


# Setup turtle window
wn = turtle.Screen()
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
print(newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
# Convert window to compatible dimensions
wn.setup(width=newScreenWidth,height=newScreenHeight)


while True:
    levelSelect = input("Press Enter to play through normally\nfrom level 1 to 3\nEnter 1, 2 or 3 to start from that level: ")
    if levelSelect == "":
        selectedLevel = 1
        print("Starting from Level: 1")
        gameState = "newgame"
        break
    elif levelSelect.isdigit():
        if int(levelSelect) > 0 and int(levelSelect) <= max([spell["level"] for spell in Spells]):
            print("Starting from Level:", levelSelect)
            selectedLevel = int(levelSelect)
            gameState = "newgame"
            break
        else:
            print("invalid level entered, must be between 1-3")
    else:
        print("invalid entry")

while True:
    if gameState == "newgame":
        # Set coords, coords start at Top Left, end at Bottom Right
        wn.setworldcoordinates(0,newScreenHeight,newScreenWidth,0)

        wn.bgcolor("#f7f7f7")
        
        BossHp = BossHealth(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
        BossCurrentHp = 30

        PlayerHp = PlayerHealth(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
        PlayerCurrentHp = 30

        playerChar = PlayerModel(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
        bossChar = BossModel(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])
        drawSpell = DrawSpell(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3])

        selectedLevelSpells = []
        selectedSpell = {}
        codingFail = False
        codingSuccess = False

        gameState = "showspells"

    elif gameState == "showspells":
        displaySpellsByLevel = SpellList(wn, newScreenWidth, newScreenHeight, newScreen[2], newScreen[3], Spells, selectedLevel)
        for spell in Spells:
            if spell["level"] == selectedLevel:
                selectedLevelSpells.append(spell)

        gameState = "spellselection"

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

                            print("-----")
                            print("Use Tab or 4 spaces to indent your code")
                            print("End code block by entering a line containing only '.'")
                            print("Arrow keys won't work to move your cursor.")
                            print("-----")
                            print("If you want to write a new code block, end this one")
                            print("then just press enter.")
                            print("-----")
                            print("The cards listed for your selected spell must be used")
                            print("Entering strings manually (using \"abc\" or \'abc\')")
                            print("is not allowed and spongebob will be damaged")
                            print("Write a block of code to make:")
                            print("-----")
                            print("  cast =", playerGoal)
                            print("Currently,")
                            print("  cast =", playerBaseCast)
                            print("-----")

                            gameState = "getplayerinput"
                else:
                    print("invalid spell index")
            else:
                print("spell index is an integer")


    elif gameState == "getplayerinput":

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

        # print("end of getplayerinput, printing userCode and cast")
        # print(userCode)
        # print(cast)
        gameState = "checkplayerinput"

    elif gameState == "checkplayerinput":
        # check fails
        if codingFail:
            # print("fail before checkplayerinput")
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
            drawSpell.draw(69, bossChar)
            PlayerHp.decrement(damage, PlayerCurrentHp)
            PlayerCurrentHp -= damage
        elif codingSuccess:
            damage = selectedSpell["damageOnSuccess"]
            drawSpell.draw(selectedSpell["level"], bossChar)
            BossHp.decrement(damage, BossCurrentHp)
            BossCurrentHp -= damage

        if PlayerCurrentHp <= 0:
            print("boss win")
            playerChar.lose(bossChar)
            time.sleep(2)
            break

        elif BossCurrentHp <= 0:
            print("player win")
            playerChar.win(bossChar)
            time.sleep(2)
            if selectedLevel == 3:
                print("All levels completed!")
                break
            else:
                selectedLevel += 1
                print("Advancing to Level:", selectedLevel)
                wn.clearscreen()
                gameState = "newgame"

        codingFail = False
        codingSuccess = False
        if BossCurrentHp > 0:
            gameState = "spellselection"
        else:
            pass
