import turtle
from TurtleClasses import (
    HpBar,
    BossHp,
    PlayerHp
)
import math
import time

# Setup turtle window
wn = turtle.Screen()
# wn.bgcolor("#EEEEEC")
wn.title("Card-Game")
# wn.setup(width=0.7,height=0.9)
wn.setup(width=0.7,height=0.95) #14:19

wnWidth = wn.window_width()
wnHeight = wn.window_height()
wn.setworldcoordinates(0,wnHeight,wnWidth,0)

BossHp = BossHp(wnWidth, wnHeight, wn)

PlayerHp = PlayerHp(wnWidth, wnHeight, wn)

# time.sleep(0.2)
# BossHp.decrement(3)
# time.sleep(0.2)
# PlayerHp.decrement(4)
# time.sleep(0.2)
# BossHp.decrement(1)
# time.sleep(0.2)
# PlayerHp.decrement(1)

# wn.register_shape("HpUnit", ((-4,-2),(-4,2),(4,2),(4,-2)))
# wn.register_shape("HpUnit", ((-(wnHeight*0.018//2),-(wnWidth)),(-(wnHeight),(wnWidth)),(wnHeight,wnWidth),(wnHeight,-(wnWidth))))

# PlayerHp = PlayerHp()
# BossHp = BossHp()

# PlayerHp.fullHp()

# BossHp.fullHp()

def hitBoss(boss, hitpoints):
    boss -= hitpoints
    BossHp.decrement(hitpoints, boss)

def hitPlayer(player, hitpoints):
    player -= hitpoints
    PlayerHp.decrement(hitpoints, player)

def EndTurn(a, boss, player):
    rawUserCode = userCode
    try:
        # print(globals()) # a and cards will be in <--
        exec(compile(rawUserCode, "<string>", "exec"), globals())

    except:
        print("compile error, hit for 6")
        hitPlayer(6)
    else:
        print("Result: a =", a)
        if a == Spells[atk]["requirement"]:
            hitBoss(boss, Spells[atk]["hitpoints"])
            print("***woosh wooosh***")
        else:
            print("Invalid Spell Use!")
            hitPlayer(player, 3)


Spells = [{"a" : "", "cards": [], "requirement": "hello dog", "hitpoints": 5},
{"a": [1, 2], "cards": [], "requirement": [1, 2, 3], "hitpoints": 5}]

# turtle.listen()
# turtle.onkey(Player.EndTurn, "r")
boss = 10
player = 10

a = "" #help idk how to do the global thing, the a is not working here
atk = 0 #index of spell
while True:
    spell = Spells[atk]
    userCode = ""
    buffer = []
    print("cards =", spell["cards"])
    print("requirement:", "\""+spell["requirement"]+"\"")
    print("assign spell requirement to variable a")
    print("enter a line with only . to end input")
    print('e.g( a = cards[1][1:3] + " " + cards[3][:4] <enter>)')
    print(" . <enter>")
    while True:
        print(">>>", end="")
        line = input()
        if line == ".":
            break
        buffer.append(line)
        userCode = "\n".join(buffer)
    endTurn = input("Press Enter to end turn")
    #a = "hello dog"
    EndTurn(a, boss, player)
    print("boss hp:",boss, "player hp:",player)
    if (boss <= 0):
        print("Player wins")
        break
    if (player <= 0):
        print("Boss wins")
        break
    atk += 1 #to move to next requirement

preventFallingOff = input("end of file\n")