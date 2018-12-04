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

# havent found a way to pass variable from inside exec to outside scopes, without using global
a = "" # global a

class Life():
    def __init__(self):
        self.hp = 10

class Player(Life):
    def __init__(self):
        Life.__init__(self)
        # print(self.hp, self)

    def hitBoss(self, hitpoints):
        BossHp.decrement(hitpoints, Boss.hp)
        Boss.hp -= hitpoints

    def EndTurn(self):
        rawUserCode = userCode
        try:
            # print(globals()) # a and cards will be in <--
            exec(compile(rawUserCode, "<string>", "exec"), globals())

        except:
            print("compile error, hit for 6")
            Boss.hitPlayer(6)
        else:
            Spells.checkSpell()

class Boss(Life):
    def __init__(self):
        Life.__init__(self)

    def hitPlayer(self, hitpoints):
        PlayerHp.decrement(hitpoints, Player.hp)
        Player.hp -= hitpoints

class Spells():
    def __init__(self):
        self.atk1 = {
            "name": "attack spell 1",
            "requirement": "hello dog",
            "hitpoints": 5
        }

    def checkSpell(self):
        global a

        if a == self.atk1["requirement"]:
            Player.hitBoss(self.atk1["hitpoints"])
            self.AttackSpell1()

        else:
            print("Invalid Spell Use!")
            Boss.hitPlayer(3)

    def AttackSpell1(self):
        print(self.atk1["name"])
        print("***woosh wooosh***")


Player = Player()
Boss = Boss()

Spells = Spells()

# turtle.listen()
# turtle.onkey(Player.EndTurn, "r")

while True:
    userCode = ""
    buffer = []
    cards = ["helloo", "wurf", "dogge"]
    print("cards =", cards)
    print("requirement:", "\""+Spells.atk1["requirement"]+"\"")
    print("assign spell requirement to variable a")
    print("enter a line with only . to end input")
    print("e.g( a = cards[1][1:3] + " " + cards[3][:4] <enter>)")
    print(" . <enter>")
    while True:
        print(">>>", end="")
        line = input()
        if line == ".":
            break
        buffer.append(line)
        userCode = "\n".join(buffer)
    endTurn = input("Press Enter to end turn")
    Player.EndTurn()
    print("boss hp:",Boss.hp, "player hp:",Player.hp)
    if (Boss.hp <= 0):
        print("Player wins")
        break
    if (Player.hp <= 0):
        print("Boss wins")
        break




preventFallingOff = input("end of file\n")