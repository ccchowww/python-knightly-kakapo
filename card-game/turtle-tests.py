import turtle
import time

# boss health bar
# player health bar
# cards
# cards on click
# spell animations

# Game State dictionary that will be passed as arg.
# jk this is hard af
newGameState = {
    "bossHealth": 100,
    "playerHealth": 100,
    "playerSpellToCast": "attack1",
    "bossSpellToCast": "boss-attack1"
}

def AnimationHandler():
    s = turtle.Screen()
    s.setup(1500,1000)

    # Draw initial Boss health bar
    BossHpBar = turtle.Turtle()
    BossHpBar.color("green")
    BossHpBar.hideturtle()
    BossHpBar.speed(0)
    BossHpBar.width(40)
    BossHpBar.penup()
    BossHpBar.setposition(-600, 400)
    BossHpBar.pendown()
    BossHpBar.forward(1200)
    
    # Right now damageAmount is number of pixels, just for now
    def damageBoss(damageAmount):
        damager = BossHpBar.clone()

        BossHpBar.speed(damageAmount // 50)
        BossHpBar.color("red")
        BossHpBar.backward(damageAmount)
        BossHpBar.color("green")
        # BossHpBar.forward(0)

        time.sleep(0.2)

        damager.speed(damageAmount // 150)
        damager.color("white")
        damager.backward(damageAmount)
        damager.forward(0)
        damager.color("green")
        damager.forward(0)

    time.sleep(1)
    damageBoss(200)  # call this to animate decreasing health bar
    time.sleep(1)
    damageBoss(500) # can be called again to decrease further
    time.sleep(1)
    damageBoss(400)

    turtle.done()

AnimationHandler() # We cant actually do it this way, because this will redraw everything
                # so all turtle objects need to be in the same scope as the game.