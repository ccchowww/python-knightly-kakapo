import turtle
turtle.setup(width = 800,height=800,startx = None, starty=None)
turtle.penup()
turtle.setpos(-350.00,100.00)
turtle.speed(20)

turtle.write("Example\n"
             "Given the following code:\n"
             "\n"
             "x=[5,4]\n"
             "print(id(x))\n"
             "x=x*2"
             "print(id(x))"
             "\n"
             "When this code is executed the: \n"
             "a new list is created which is assigned to x\n"
             "hence modifying the identifier of x"
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

#2boxes
turtle.fillcolor("light grey")
turtle.begin_fill()
for i in range(4):
        turtle.forward(50)
        turtle.right(90)
turtle.forward(50)
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

turtle.right(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(25)

#LOWERBOX
#arrow
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

#2box
turtle.left(80)
turtle.forward(10)
turtle.pendown()
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


               
                      
                      
                      
                      
                     


             
                                          

