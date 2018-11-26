class Game():
    health = 100
    spellToCast = 0

    def castSpell(fail):
        if fail == True:
            return player.hit()
        else:
            return boss.hit()

    def hit(self):
        self.health -= self.spellToCast
        #animation to decrease health bar

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
    finally:
        if eval(playerMove) == attack1:
            boss.spellToCast = 10
            player.spellToCast = 0
            fail = False
        #more elif for other spell
        else:
            boss.spellToCast = 0
            player.spellToCast = 10
            fail = True
        return Game.castSpell(fail)

flag = True
fail = False
player = Game()
boss = Game()
attack1 = 1

while flag:
    getPlayerInput(attack1)
    flag = Game.checkHealth()

if player.health == 0:
    continue
    #die animation

if boss.health == 0:
    continue
    #die animation
