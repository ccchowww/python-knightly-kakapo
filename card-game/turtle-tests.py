from TurtleClasses import (
    BossHp,
    PlayerHp
)
import turtle

wn = turtle.Screen()
wn.bgcolor("#EEEEEC")
wn.title("Object-based Turtles")
wn.setup(1000,1000)

PlayerHp = PlayerHp()
BossHp = BossHp()

PlayerHp.fullHp()

BossHp.fullHp()


# card1 = "hello "
# card2 = "world"
# card3 = "dogge"
cards = ["hello", "world", "dogge"]


answer = "initial"

def execR():
    print("R pressed")
    # print(globals()) # To see what variables/functions are available to exec()
    # print(locals())
    #                   using <string> is just a convention, supposed to be name of file userCode is from.
    codeObject = compile(userCode,"<string>","exec")
    exec(codeObject, globals())

def printAnswer():
    print("p pressed")
    print(answer)


userCode = ""
buffer = []
ending = ""


# while True:
    # playerInput = input("butt")
    # if playerInput == "exit":
    #     print("exiting game")
    #     break
    # elif playerInput == "playerhp":
    #     PlayerHp.decrement(1) # Units to decrement hp by
    # elif playerInput == "bosshp":
    #     BossHp.decrement(1)
    # else:
print("press enter to input another line, to end input, input only . and press enter")
print("assign to answer")
print("after ending input, focus turtle window, press r to exec, press p to print variable answer")
print(cards)
for card in cards:
    print("card:", cards.index(card), "card value:", card)
while True: # can input anything, def functions, for/while loops, can use variables in same scope as exec()
    print(">>>", end="")
    line = input()
    if line == ".":
        break
    buffer.append(line)
userCode = "\n".join(buffer)

turtle.listen() # This sets focus to turtle window without raising it, can press r / p
turtle.onkey(execR, "r")
turtle.onkey(printAnswer, "p")

preventFallingOff = input("end of file, press: R to exec, P to print answer\n")