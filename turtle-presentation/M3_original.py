import turtle


turtle.penup()
turtle.setpos(-350.00,100.00)
turtle.speed(20)

turtle.write("For immutable objects \n"
"x=x*2 and x*=2 behave the same way;\n"
"the copy of x is created as well as \n"
"its reference is updated.\n"
"This is shown below for a string x='hello'. "
,align="left",font=("Ariel",20,"normal"))

#xbox
turtle.penup()
turtle.right(90)
turtle.forward(150)
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

                        
 #UPPERBOX
#arrow
turtle.penup()
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.pendown()
turtle.forward(10)
for i in range(6):
        turtle.pendown()
        turtle.forward(5)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.left(160)
turtle.forward(10)
turtle.backward(10)
turtle.left(45)
turtle.forward(10)
turtle.backward(10)
turtle.right(205)
#box
turtle.penup()
turtle.forward(10)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()
turtle.fillcolor("light grey")
turtle.begin_fill()
for i in range(4):
        turtle.forward(50)
        turtle.right(90)
turtle.end_fill()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

#smallbox
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
turtle.write("hello",align="center",font=("Ariel",20,"normal"))
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(105)
turtle.right(90)
turtle.forward(25)

#DOWNBOXES
turtle.right(170)
turtle.pendown()
turtle.forward(150)
turtle.left(160)
turtle.forward(15)
turtle.backward(15)
turtle.left(45)
turtle.forward(15)
turtle.backward(15)
turtle.right(205)
turtle.penup()
turtle.left(80)

#twoboxes
turtle.forward(10)
turtle.pendown()
turtle.begin_fill()
for i in range(4):
                turtle.forward(50)
                turtle.right(90)
turtle.forward(50)
for i in range(4):
                turtle.forward(50)
                turtle.right(90)
turtle.end_fill() 

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
turtle.write("hello",align="center",font=("Ariel",20,"normal"))
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
turtle.write("hello",align="center",font=("Ariel",20,"normal"))
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(55)
turtle.left(90)

