import turtle
turtle.setup(width = 1000,height=1000,startx = None, starty=None)
turtle.penup()
turtle.setpos(-450.00,50.00)
turtle.speed(20)

#information
turtle.pendown()
turtle.write("Example\n"
             " Given this code:\n "
             "\n"
             " x=[5,4]\n"
             " print(id(x))\n"
             " x*=2\n"
             " print(id(x))\n"
             "\n"
             "When this code is executed the list is updated\n"
             "without generating a new copy of x\n"
             "or changing its reference\n"
             , align="left",font=("Ariel",20,"normal"))


#squarebox
turtle.penup()
turtle.left(90)
turtle.forward(210)
turtle.pendown()
turtle.right(90)
for i in range(4):
    turtle.forward(110)
    turtle.right(90)
turtle.penup()

#Animation
turtle.right(90)
turtle.forward(350)
turtle.left(90)
turtle.write("x\n",align="left",font=("Ariel",20,"normal"))
turtle.forward(30)
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.pendown()
turtle.fillcolor("light green")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.end_fill()
turtle.pendown()

#arrow
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.left(160)
turtle.forward(15)
turtle.backward(15)
turtle.left(45)
turtle.forward(15)
turtle.backward(15)
turtle.right(205)

#box
turtle.penup()
turtle.forward(10)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()
#4boxes
turtle.fillcolor("light grey")
turtle.begin_fill()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
for j in range(3):
    turtle.forward(100)
    turtle.right(90)
    for i in range(3):
        turtle.forward(50)
        turtle.right(90)
turtle.end_fill()
turtle.penup()

#small boxes

turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.pendown()

turtle.forward(35)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.penup()
turtle.forward(25)
turtle.write("4",align="center",font=("Ariel",20,"normal"))
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(55)
turtle.left(90)

turtle.pendown()
turtle.forward(35)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.penup()
turtle.forward(25)
turtle.write("5",align="center",font=("Ariel",20,"normal"))
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(55)
turtle.left(90)

turtle.pendown()
turtle.forward(35)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.penup()
turtle.forward(25)
turtle.write("4",align="center",font=("Ariel",20,"normal"))
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(55)
turtle.left(90)

turtle.pendown()
turtle.forward(35)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.forward(35)
turtle.left(90)
turtle.penup()
turtle.forward(25)
turtle.write("5",align="center",font=("Ariel",20,"normal"))
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(55)
turtle.left(90)









    
    
    



