# Part 7 Why mutability matters?

import turtle
t = turtle.Turtle()
t.ht()
t.speed(10)

t.ht()
t.up()
t.goto(425, 250)
t.down()
t.write("Why does mutability matters in coding?", align = "right", font=("Ariel",40,"normal"))

t.up()
t.goto(0, -20)
t.down()
t.write('Python handles mutable and immutable objects differently. Immutable \n'
        'objects are quicker to access than mutable objects yet fundamentally \n'
        'expensive to "change", because doing so involves creating a copy, \n'
        'hence wasting much more memory creating and throwing away objects'
        , align="center", font=("Ariel", 30, "normal"))

turtle.done()
