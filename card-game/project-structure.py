#Stage 1
"""Turtle draw boss, boss health
   Turtle draw player, player attacks, player health"""

class Game(): #or should we name the class as Player(), den the two objects are boss and USER,
#then we might replace every "player" we typed wv "user", or do u hv a better name
	health = 100
	fail = False
	attack = 0
	castSpell = 0
	"""i am confused with attack and castSpell, are both of them actually integer?
	attack is the target and castSpell is the damage deal right?"""

	#move all the functions inside, except stage()?
	#we may not need playerMove?
	#and we may only need one function for hit(attack, (user or boss))?
	#like this-?
	def castSpell(player):
		if player.fail == True:
			return hit(player)
		else:
			return hit(boss)

	def hit(player):
		player.health -= player.castSpell

	#we can create another class for the different spells


"""
INPUT: none
RETURN: tuple (string castSpell, boolean fail)
"""
def getPlayerInput(): 
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

"""
helper function, calls playerHitBoss or bossHitPlayer
INPUT: playerMove
RETURN: none
"""
def castSpell(playerMove):
    if playerMove[1] == True:
        return bossHitPlayer(attack, playerHealth)
        #potentially increment counter to track number of fails
    else:
        return playerHitBoss(playerMove[0], bossHealth)
        #player hit boss(playerMove[0]) Hit boss with playerMove[0] spell name. Spells defined here

"""
decrease boss health by (attack)
INPUT: attack, bossHealth
RETURN: none
"""
def playerHitBoss(attack, bossHealth):
    return
"""attack1 - deal x damage -> turtle draw attack1
attack2 - deal x+y damage -> turtle draw attack2
..."""

"""
decrease player health by (attack)
INPUT: attack, playerHealth
RETURN: none
"""
def bossHitPlayer(attack, playerHealth):
    #attack - deal z damage to player -> draw boss attack1
    return


"""
if playerHealth or bossHealth <0 change flag to false
INPUT: none
RETURN: none
"""
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
        castSpell(playerMove)
        flag = checkHealth()

"""
Nope this is too hard.
instead of separate functions calling draw animations,
we could use a dictionary to store those values, in this case it would be playerHealth = 100
bossHealth = 100, then we could add hitplayer = x, hitboss = y, spelltodraw = playerattack1
Then we pass this dict into a drawing function (dict), that will for example check
difference in health and draw the change, draw the spell, draw death animation, etc
Essentially have all drawing related functions in one function.
okies
"""