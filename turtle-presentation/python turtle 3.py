# Part 4(Mechanics of mutability)

import turtle
t = turtle.Turtle()
t.ht()
t.speed(10)

t.up()
t.goto(0,250)
t.down()
t.write("So how does mutability works?", align="center", font=("Ariel", 50, "normal"))
t.up()
t.goto(0,-50)
t.write("An easy way to understand that is if you have a look at an objects ID.\n"
        "The built-in function id() returns the identity of an object as an integer. \n"
        "This integer usually corresponds to the object’s location in memory, \n"
        "although this is specific to the Python implementation and the platform\n"
        "being used. The is operator compares the identity of two objects."
        , align = "center", font=("Ariel",30,"normal"))

turtle.done()
