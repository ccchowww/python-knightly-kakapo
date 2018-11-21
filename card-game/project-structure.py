Stage 1:
    Turtle draw boss, boss health
    Turtle draw player, player attacks, player health

    while True:
        playerMove = getplayerinput(): need to use normal input() for this, ive tried turtle textinput,
                                        cant set where turtle textinput box opens
            try:
                eval(userInput)
            except:
                print("code runtime error")
            finally: Check result of eval(userinput) here, if doesnt match any spells, set playerFail True
                if eval(userInput) == attack1: if eval(userinput) matches a spellname, return the spellname
                    castSpell = attack1
                    fail = False
                    return (castSpell, playerFail) we could add another element to store error message
                                                    then the except block can be more useful,
                                                    then maybe show the message in turtle for a few secs
                ...more elifs for other spell names

                else:
                    playerFail = True
                    castSpell = ""
                    return (castSpell, playerFail)

        CastSpell(playerMove):
            if playerMove[1] == True:
                Boss hit player() Boss hits player, potentially increment counter to track number of fails
            else:
                player hit boss(playerMove[0]) Hit boss with playerMove[0] spell name. Spells defined here

        CheckHealth():
            if bossHealth <= 60%: this is optional, without it then we only need to make attack spells
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
                break
    

    player hit boss (attack):
        attack1 - deal x damage -> turtle draw attack1
        attack2 - deal x+y damage -> turtle draw attack2
        ...

    boss hit player (attack):
        attack - deal z damage to player -> draw boss attack1

