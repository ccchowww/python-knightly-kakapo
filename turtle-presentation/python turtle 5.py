# "Animation 2"
# Part 6(List example)

import turtle
t = turtle.Turtle()
t.speed(10)
t.ht()

# Header 1
t.up()
t.goto(-620,265)
t.write("e.g. List", align="left", font=("Ariel", 35, "normal"))

# Header 2
t.goto(-620,150)
t.write("X = [10] \nX[0] = 20", align="left", font=("Ariel", 30, "normal"))

# X's square
t.begin_fill()
t.fillcolor("orange")
t.goto(-550,80)
t.down()
for i in range(4):
        t.fd(150)
        t.rt(90)
t.end_fill()
t.up()

# X
t.goto(-485,-15)
t.down()
t.write("X", align="left", font=("Ariel", 30, "normal"))
t.up()

# Forward Line
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(115)
t.down()
t.fd(200)
t.up()
t.goto(-170,5)
t.down()
t.lt(160)
t.fd(40)
t.up()
t.goto(-170,5)
t.down()
t.lt(40)
t.fd(40)
t.lt(160)
t.up()

# Blank Square
t.pencolor("lightgreen")
t.width(5)
t.goto(-125,80)
t.down()
for i in range(4):
        t.fd(150)
        t.rt(90)

# ID
t.goto(-70,80)
t.pencolor("black")
t.width(1)
t.write("ID", align="left", font=("Ariel", 30, "normal"))
t.up()

# Split Line(Up)
t.goto(50,25)
t.lt(30)
t.down()
t.fd(170)
t.up()
t.goto(205,115)
t.down()
t.lt(160)
t.fd(40)
t.up()
t.goto(205,115)
t.down()
t.lt(40)
t.fd(40)
t.lt(160)
t.rt(30)
t.up()

# 10's Square
t.pencolor("blue")
t.width(5)
t.goto(220,220)
t.down()
for i in range(4):
    t.fd(150)
    t.rt(90)
t.up()

# 10
t.pencolor("black")
t.width(1)
t.goto(275,125)
t.write(10, align="left", font=("Ariel", 30, "normal"))
t.up()

# Dotted Split Line(Down)
t.goto(50,-15)
t.rt(30)
t.down()
for i in range(9):
        t.up()
        t.fd(10)
        t.down()
        t.fd(10)
t.up()
t.goto(210,-107)
t.down()
t.lt(160)
t.fd(40)
t.up()
t.goto(210,-107)
t.down()
t.lt(40)
t.fd(40)
t.lt(190)
t.up()

# 20's Square
t.pencolor("red")
t.width(5)
t.goto(220,-50)
t.down()
for i in range(4):
    t.fd(150)
    t.rt(90)
t.up()

# 20
t.pencolor("black")
t.width(1)
t.goto(275, -145)
t.write(20, align="left", font=("Ariel", 30, "normal"))

turtle.done()
