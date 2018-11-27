import turtle
from TurtleClasses import (
    BossHp,
    PlayerHp
)

# Setup turtle window
wn = turtle.Screen()
wn.bgcolor("#EEEEEC")
wn.title("Object-based Turtles")
wn.setup(1000,1000)

PlayerHp = PlayerHp()
BossHp = BossHp()

PlayerHp.fullHp()

BossHp.fullHp()

# havent found a way to pass variable from inside exec to outside scopes, without using global
outputvar = "" # global outputvar

class Life():
    def __init__(self):
        self.hp = 100

class Player(Life):
    def __init__(self):
        Life.__init__(self)
        print(self.hp, self)

    def hitBoss(self, hitpoints):
        BossHp.decrement(hitpoints)

    def EndTurn(self):
        rawUserCode = userCode
        try:
            # print(globals()) # outputvar and cards will be in <--
            exec(compile(rawUserCode, "<string>", "exec"), globals())

        except:
            print("compile error, punish player")
            boss.hitPlayer(25)
        else:
            spells.checkSpell()

class Boss(Life):
    def __init__(self):
        Life.__init__(self)
        print(self.hp, self)

    def hitPlayer(self, hitpoints):
        PlayerHp.decrement(hitpoints)

# class CodeExecuter():
#     def __init__(self):
#         self.codeObject = "initial"

#     def Execute(self, userCode):
#         self.codeObject = compile(userCode, "<string>", "exec")
#         print(globals())
#         exec(self.codeObject, globals())
#         # call output checker/ spells.checkspell()

class Spells():
    def __init__(self):
        self.atk1 = {
            "name": "attack spell 1",
            "requirement": "hello dog",
            "hitpoints": 10
        }

    def checkSpell(self):
        global outputvar

        if outputvar == self.atk1["requirement"]:
            player.hitBoss(self.atk1["hitpoints"])
            self.AttackSpell1()

        else:
            print("Invalid Spell Use!")
            boss.hitPlayer(15)

    def AttackSpell1(self):
        print(self.atk1["name"])
        print("***woosh wooosh***")


player = Player()
boss = Boss()

spells = Spells()

userCode = ""
buffer = []
cards = ["helloo", "wurf", "dogge"]
print("press enter to input another line, to end input, input only . and press enter")
print("assign to outputvar")
print("after ending input, focus turtle window, press r to end turn")
print("cards =", cards)
while True:
    print(">>>", end="")
    line = input()
    if line == ".":
        break
    buffer.append(line)
    userCode = "\n".join(buffer)

turtle.listen()
turtle.onkey(player.EndTurn, "r")

preventFallingOff = input("end of file\n")