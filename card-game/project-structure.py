#Stage 1
"""Turtle draw boss, boss health
   Turtle draw player, player attacks, player health"""
def getPlayerInput(): #use normal input()
    return

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
    while True:
        playerMove = getPlayerInput()
        try:
            eval(playerMove)
        except:
            print("code runtime error")
        finally:
            if eval(userInput) == attack1:
                castSpell = attack1
                fail = False
                castSpell()
                return(castSpell, playerFail) #return to whr?
                """could add another element to store error message, maybe show 
                the message in turtle for few secs"""
                """more elifs for other spell name"""
            else:
                fail = True
                castSpell = ""

                #attackBoss = certain number? *see suggestion below

                return(castSpell, playerFail) #return to whr?

        playerHitBoss(attack)
        bossHitPlayer(attackBoss)

        flag = checkHealth() #can return false if health<0 to exit loop?

        """
        should we use different variable for attackPlayer and attackBoss? 

        let initial attackPlayer = 0, if input matches the spell, 
        only we set attack using castSpell, and set attackPlayer back to 0
        after we decrease boss health

        let initial attackBoss = 0, if input doesnt match the spell,
        set attackBoss to a certain number(will the damage to user will be the same
        for every round?), and set attackBoss back to 0 at the end of bossHitPlayer

        so we can still call both playerHitBoss and bossHitPlayer every round
        """
