#draw boss
#draw bosshp
#draw playerhp
#draw card
#draw attack
from TurtleClasses import (
    BossHp,
    PlayerHp
)
import turtle

class Spell():
    def __init__(self, attack, card1, card2):
        self.attack = attack
        self.card1 = card1
        self.card2 = card2

attack1 = Spell("Hello World", "Hello", " World")
attack2 = Spell([1, 3, 5, 7], [1, 3, 5], [7, 9])
attack3 = Spell(["Python", "fun"], "Python", "fun")

class Game():
    health = 100
    spellToCast = 0

    def castSpell(fail):
        if fail == True:
            return Game.hitPlayer()
        else:
            return Game.hitBoss()

    def hitBoss():
        boss.health -= boss.spellToCast
        BossHp.decrement(boss.spellToCast)

    def hitPlayer():
        player.health -= player.spellToCast
        PlayerHp.decrement(player.spellToCast)

    def checkHealth():
        flag = True
        if boss.health <= 0:
            flag = False
        if player.health <= 0:
            flag = False
        return flag

def getPlayerInput(attack1):
    playerMove = input("Enter spell: ")
    try:
        eval(playerMove)

    except:
        print("code runtime error")
        boss.spellToCast = 0
        player.spellToCast = 10
        fail = True
        return Game.castSpell(fail)
    finally:
        if (eval(playerMove) == attack1.attack):
            boss.spellToCast = 10
            player.spellToCast = 0
            fail = False
            #animation to replace attack1 with new attack
            #animation to replace cards with new cards???
        #more elif for other spell
        else:
            boss.spellToCast = 0
            player.spellToCast = 10
            fail = True
        return Game.castSpell(fail)

flag = True
player = Game()
boss = Game()

wn = turtle.Screen()
wn.bgcolor("#EEEEEC")
wn.title("Object-based Turtles")
wn.setup(1000,1000)

PlayerHp = PlayerHp()
BossHp = BossHp()

PlayerHp.fullHp()

BossHp.fullHp()

while flag:
    getPlayerInput(attack1)
    flag = Game.checkHealth()

if player.health == 0:
    pass
    #die animation

if boss.health == 0:
    pass
    #die animation
