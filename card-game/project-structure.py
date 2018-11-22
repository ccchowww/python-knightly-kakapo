#Stage 1
"""Turtle draw boss, boss health
   Turtle draw player, player attacks, player health"""
def getPlayerInput(): #use normal input()
    try:
        eval(playerMove)
    except:
        print("code runtime error")
    finally:
        if eval(userInput) == attack1:
            castSpell = attack1
            fail = False
            castSpell()
            return(castSpell, playerFail)
            """could add another element to store error message, maybe show 
            the message in turtle for few secs"""
            """more elifs for other spell name"""
        else:
            fail = True
            castSpell = ""
            return [castSpell, fail]

def castSpell(playerMove):
    if playerMove[1] == True:
        #Boss hit player() Boss hits player, potentially increment counter to track number of fails
        return
    else:
        return
        #player hit boss(playerMove[0]) Hit boss with playerMove[0] spell name. Spells defined here

def playerHitBoss(attackBoss):
    return
"""attack1 - deal x damage -> turtle draw attack1
attack2 - deal x+y damage -> turtle draw attack2
..."""

def bossHitPlayer(attack):
    #attack - deal z damage to player -> draw boss attack1
    return

def checkHealth():
    return
    """if bossHealth <= 60%: this is optional, without it then we only need to make attack spells
        we can add it after the core stuff is done
        boss hits player(60% attack)
    if bossHealth <= 30%:
        boss hits player(30% attack)
        if bossHealth <= 10%:
         boss hits player(10% attack)

    elif playerHeatlh <= 0:
        playerDeathAnimation()
        exit this stage() show stats like damage dealt, damage taken, boss remaining hp etc
        break
    elif bossHealth <= 0:
        bossDeathAnimation()
        exit this stage()
        break"""
    

def stage():
    playerHealth = 100
    bossHealth = 100
    flag = True
    while flag:
        playerMove = getPlayerInput()


        playerHitBoss(attack)
        bossHitPlayer(attackBoss)

        flag = checkHealth()

