#Stage 1
"""Turtle draw boss, boss health
   Turtle draw player, player attacks, player health"""

"""
INPUT: none
RETURN: tuple (string castSpell, boolean fail)
"""
def getPlayerInput(): #use normal input()
    try:
        eval(playerMove)
    except:
        print("code runtime error")
        castSpell = ""
    finally:
        if eval(userInput) == attack1:
            castSpell = attack1
            fail = False
            return (castSpell, playerFail) 
            """could add another element to store error message, maybe show 
            the message in turtle for few secs"""
            """more elifs for other spell name"""
        else:
            fail = True
            return (castSpell, fail)
 #??is castSpell a string, if it is, when will we convert it into integer since 
 #it needs to be the degree of damage rite????

"""
calls playerHitBoss or bossHitPlayer
INPUT: (string castSpell, boolean fail)
RETURN: health
"""
def castSpell(playerMove):
    if playerMove[1] == True:
        bossHitPlayer(attack, bossHealth)
        #potentially increment counter to track number of fails
        return bossHealth
    else:
        playerHitBoss(playerMove[0], playerHealth)
        #player hit boss(playerMove[0]) Hit boss with playerMove[0] spell name. Spells defined here
        return playerHealth

"""
decrease boss health by (attack)
INPUT: attack, bossHealth
RETURN: bossHealth
"""
def playerHitBoss(attack, bossHealth):
    return
"""attack1 - deal x damage -> turtle draw attack1
attack2 - deal x+y damage -> turtle draw attack2
..."""

"""
decrease player health by (attack)
INPUT: attack, playerHealth
RETURN: playerHealth
"""
def bossHitPlayer(attack, playerHealth):
    #attack - deal z damage to player -> draw boss attack1
    return


"""
if health <0 return false else return true
INPUT: playerHealth, bossHealth
RETURN: boolean
"""
def checkHealth(playerHealth, bossHealth):
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
        castSpell(playerMove)
        flag = checkHealth()

