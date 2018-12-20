import turtle

class Example1(turtle.Turtle):
        def __init__(self):
                turtle.Turtle.__init__(self)
                self.penup()
                self.setpos(-350.00,100.00)
                self.speed(20)

        def drawEx3(self):

                self.write("For immutable objects \n"
                        "x=x*2 and x*=2 behave the same way;\n"
                        "the copy of x is created as well as \n"
                        "its reference is updated.\n"
                        "This is shown below for a string x='hello'. "
                        ,align="left",font=("Ariel",20,"normal"))

                #xbox           
                self.penup()
                self.right(90)
                self.forward(150)
                self.left(90)
                self.write("x\n",align="left",font=("Ariel",20,"normal"))
                self.forward(30)
                self.left(90)
                self.forward(60)
                self.right(90)
                self.pendown()
                self.fillcolor("light green")
                self.begin_fill()
                for i in range(4):
                        self.forward(50)
                        self.right(90)
                self.end_fill()
                self.pendown()

                        
                #UPPERBOX
                #arrow
                self.penup()
                self.forward(50)
                self.right(90)
                self.forward(25)
                self.left(90)
                self.pendown()
                self.forward(10)
                for i in range(6):
                        self.pendown()
                        self.forward(5)
                self.penup()
                self.forward(5)
                self.pendown()
                self.left(160)
                self.forward(10)
                self.backward(10)
                self.left(45)
                self.forward(10)
                self.backward(10)
                self.right(205)

                #box
                self.penup()
                self.forward(10)
                self.left(90)
                self.forward(25)
                self.right(90)
                self.pendown()

                self.fillcolor("light grey")
                self.begin_fill()
                for i in range(4):
                        self.forward(50)
                        self.right(90)
                self.end_fill()

                self.right(90)
                self.forward(50)
                self.left(90)
                self.forward(25)
                self.right(90)
                self.pendown()

                #smallbox
                self.forward(35)
                self.right(90)
                self.forward(25)
                self.left(90)
                for i in range(4):
                        self.forward(50)
                        self.left(90)
                self.forward(35)
                self.left(90)
                self.penup()
                self.forward(25)
                self.write("hello",align="center",font=("Ariel",20,"normal"))
                self.left(90)
                self.forward(70)
                self.left(90)
                self.forward(105)
                self.right(90)
                self.forward(25)

                #DOWNBOXES
                self.right(170)
                self.pendown()
                self.forward(150)
                self.left(160)
                self.forward(15)
                self.backward(15)
                self.left(45)
                self.forward(15)
                self.backward(15)
                self.right(205)
                self.penup()
                self.left(80)

                #twoboxes
                self.forward(10)
                self.pendown()
                self.begin_fill()
                for i in range(4):
                        self.forward(50)
                        self.right(90)
                self.forward(50)
                for i in range(4):
                        self.forward(50)
                        self.right(90)
                self.end_fill() 

                self.forward(50)
                self.right(90)
                self.forward(50)
                self.right(90)
                self.forward(25)
                self.left(90)
                self.pendown()

                self.forward(35)
                self.right(90)
                self.forward(25)
                self.left(90)
                for i in range(4):
                        self.forward(50)
                        self.left(90)
                self.forward(35)
                self.left(90)
                self.penup()
                self.forward(25)
                self.write("hello",align="center",font=("Ariel",20,"normal"))
                self.left(90)
                self.forward(70)
                self.left(90)
                self.forward(55)
                self.left(90)

                self.pendown()

                self.forward(35)
                self.right(90)
                self.forward(25)
                self.left(90)
                for i in range(4):
                        self.forward(50)
                        self.left(90)
                self.forward(35)
                self.left(90)
                self.penup()
                self.forward(25)
                self.write("hello",align="center",font=("Ariel",20,"normal"))
                self.left(90)
                self.forward(70)
                self.left(90)
                self.forward(55)
                self.left(90)


