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

while True:
    playerInput = input("exit, playerhp or bosshp")
    if playerInput == "exit":
        print("exiting game")
        break
    elif playerInput == "playerhp":
        PlayerHp.decrement(1) # Units to decrement hp by
    elif playerInput == "bosshp":
        BossHp.decrement(1)

# wn.exitonclick()