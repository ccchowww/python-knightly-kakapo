# "Animation 1"
# Part 5(String example)

import turtle
t = turtle.Turtle()
t.speed(10)
t.ht()

# Header 1
t.up()
t.goto(-620,265)
t.down()
t.write("e.g. String", align="left", font=("Ariel", 35, "normal"))
t.up()

# Header 2
t.goto(-620,170)
t.down()
t.write("X = 10 \nX = 20", align="left", font=("Ariel", 30, "normal"))
t.up()

# X's Square
t.goto(-550,100)
t.down()
t.fillcolor("orange")
t.begin_fill()
for i in range(4):
        t.fd(150)
        t.rt(90)
t.end_fill()
t.up()

# X
t.goto(-485,5)
t.down()
t.write("X", align="left", font=("Ariel", 30, "normal"))
t.up()

# Line
t.goto(-365,30)
t.down()
t.fd(300)
t.up()
t.goto(-65,30)
t.down()
t.lt(160)
t.fd(40)
t.up()
t.goto(-65,30)
t.down()
t.lt(40)
t.fd(40)
t.lt(160)
t.up()

# 10's square
t.pencolor("blue")
t.width(5)
t.goto(-20,100)
t.down()
for i in range(4):
        t.fd(150)
        t.rt(90)
t.up()

# ID 1
t.pencolor("black")
t.width(1)
t.goto(30,100)
t.down()
t.write("ID 1", align="left", font=("Ariel", 30, "normal"))
t.up()

# 10
t.goto(30,5)
t.down()
t.write("10", align="left", font=("Ariel", 30, "normal"))
t.up()

# Dotted line
t.goto(-380,-10)
t.down()
t.rt(30)
for i in range(19):
        t.up()
        t.fd(10)
        t.down()
        t.fd(10)
t.up()
t.goto(-40,-205)
t.down()
t.lt(160)
t.fd(40)
t.up()
t.goto(-40,-205)
t.down()
t.lt(40)
t.fd(40)
t.lt(160)
t.lt(30)
t.up()

# 20's square
t.pencolor("red")
t.width(5)
t.goto(-20,-130)
t.down()
for i in range(4):
        t.fd(150)
        t.rt(90)
t.up()

# ID 2
t.pencolor("black")
t.width(1)
t.goto(30,-130)
t.down()
t.write("ID 2", align="left", font=("Ariel", 30, "normal"))
t.up()

# 20
t.goto(30,-230)
t.write("20", align="left", font=("Ariel", 30, "normal"))

turtle.done()
