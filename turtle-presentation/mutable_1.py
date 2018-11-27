import turtle

# turtle.setup(width = 1000,height=1000,startx = None, starty=None)
# turtle.penup()
# turtle.setpos(-450.00,50.00)
# turtle.speed(20)

wn = turtle.Screen()
wn.bgcolor("#EEEEEC")
wn.title("Example 1")
wn.setup(1000,1000, startx = None, starty = None)

class BossHp(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("black")
        self.width(3)
        # self.units = []

    def fullHp(self):
        self.setpos(-400,480)
        self.pendown()
        self.shape("square")
        self.color("#ffae00")
        self.shapesize(0.1,0.1,0)
        self.setx(self.xcor() + 50)
        self.sety(self.ycor() - 4)
        self.stamp()
        self.sety(self.ycor() + 4)
        while(self.xcor() < 280):
            self.setx(self.xcor() + 100)
            self.sety(self.ycor() - 4)
            self.stamp()
            self.sety(self.ycor() + 4)
        self.goto(400,480)
        self.goto(400,430)
        self.setx(self.xcor() - 50)
        self.sety(self.ycor() + 4)
        self.stamp()
        self.sety(self.ycor() - 4)
        while(self.xcor() > -280):
            self.setx(self.xcor() - 100)
            self.sety(self.ycor() + 4)
            self.stamp()
            self.sety(self.ycor() - 4)
        self.goto(-400,430)
        self.goto(-400,480)
        self.penup()

        self.setpos(-380,455)
        self.color("#ff0043")
        self.shapesize(1.8,0.8,0)
        x = self.xcor()
        for i in range(0,39):
            unit = self.stamp()
            # self.units.append(unit)
            x += 20
            self.setx(x)


    def decrement(self, units):
        self.clearstamps(-units)

class Example1(turtle.Turtle):
        def __init__(self):
                turtle.Turtle.__init__(self)
                self.penup()
                self.setpos(-450.00,50.00)
                self.speed(20)

        def drawEx1(self):
                self.pendown()
                self.write("Example\n"
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
                # self.penup()
                # self.left(90)
                # self.forward(210)
                # self.pendown()
                # self.right(90)
                # for i in range(4):
                #         self.forward(110)
                #         self.right(90)
                # self.penup()

                #Animation
                self.penup()
                self.right(90)
                self.forward(350)
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

                #arrow
                self.forward(50)
                self.right(90)
                self.forward(25)
                self.left(90)
                self.forward(20)
                self.pendown()
                self.forward(50)
                self.left(160)
                self.forward(15)
                self.backward(15)
                self.left(45)
                self.forward(15)
                self.backward(15)
                self.right(205)

                #box
                self.penup()
                self.forward(10)
                self.left(90)
                self.forward(25)
                self.right(90)
                self.pendown()
                #4boxes
                self.fillcolor("light grey")
                self.begin_fill()
                for i in range(4):
                        self.forward(50)
                        self.right(90)
                for j in range(3):
                        self.forward(100)
                        self.right(90)
                        for i in range(3):
                                self.forward(50)
                                self.right(90)
                self.end_fill()
                self.penup()

                #small boxes

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
                self.write("4",align="center",font=("Ariel",20,"normal"))
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
                self.write("5",align="center",font=("Ariel",20,"normal"))
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
                self.write("4",align="center",font=("Ariel",20,"normal"))
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
                self.write("5",align="center",font=("Ariel",20,"normal"))
                self.left(90)
                self.forward(70)
                self.left(90)
                self.forward(55)
                self.left(90)

Ex1 = Example1()

# Ex1.drawEx1()

BossHp = BossHp()

# BossHp.fullHp()


while True:
    playerInput = input("exit, ex1 or ex2")
    if playerInput == "exit":
        print("exiting game")
        break
    elif playerInput == "ex1":
        Ex1.clear()
        BossHp.clear()
        Ex1.drawEx1() # Units to decrement hp by
    elif playerInput == "ex2":
        Ex1.clear()
        BossHp.clear()
        BossHp.fullHp()



                # #information
                # self.pendown()
                # self.write("Example\n"
                #         " Given this code:\n "
                #         "\n"
                #         " x=[5,4]\n"
                #         " print(id(x))\n"
                #         " x*=2\n"
                #         " print(id(x))\n"
                #         "\n"
                #         "When this code is executed the list is updated\n"
                #         "without generating a new copy of x\n"
                #         "or changing its reference\n"
                #         , align="left",font=("Ariel",20,"normal"))


                # #squarebox
                # self.penup()
                # self.left(90)
                # self.forward(210)
                # self.pendown()
                # self.right(90)
                # for i in range(4):
                #         self.forward(110)
                #         self.right(90)
                # self.penup()

                # #Animation
                # self.right(90)
                # self.forward(350)
                # self.left(90)
                # self.write("x\n",align="left",font=("Ariel",20,"normal"))
                # self.forward(30)
                # self.left(90)
                # self.forward(60)
                # self.right(90)
                # self.pendown()
                # self.fillcolor("light green")
                # self.begin_fill()
                # for i in range(4):
                #         self.forward(50)
                #         self.right(90)
                # self.end_fill()
                # self.pendown()

                # #arrow
                # self.forward(50)
                # self.right(90)
                # self.forward(25)
                # self.left(90)
                # self.forward(20)
                # self.pendown()
                # self.forward(50)
                # self.left(160)
                # self.forward(15)
                # self.backward(15)
                # self.left(45)
                # self.forward(15)
                # self.backward(15)
                # self.right(205)

                # #box
                # self.penup()
                # self.forward(10)
                # self.left(90)
                # self.forward(25)
                # self.right(90)
                # self.pendown()
                # #4boxes
                # self.fillcolor("light grey")
                # self.begin_fill()
                # for i in range(4):
                #         self.forward(50)
                #         self.right(90)
                # for j in range(3):
                #         self.forward(100)
                #         self.right(90)
                # for i in range(3):
                #         self.forward(50)
                #         self.right(90)
                # self.end_fill()
                # self.penup()

                # #small boxes

                # self.forward(50)
                # self.right(90)
                # self.forward(50)
                # self.right(90)
                # self.forward(25)
                # self.left(90)
                # self.pendown()

                # self.forward(35)
                # self.right(90)
                # self.forward(25)
                # self.left(90)
                # for i in range(4):
                #         self.forward(50)
                #         self.left(90)
                # self.forward(35)
                # self.left(90)
                # self.penup()
                # self.forward(25)
                # self.write("4",align="center",font=("Ariel",20,"normal"))
                # self.left(90)
                # self.forward(70)
                # self.left(90)
                # self.forward(55)
                # self.left(90)

                # self.pendown()
                # self.forward(35)
                # self.right(90)
                # self.forward(25)
                # self.left(90)
                # for i in range(4):
                #         self.forward(50)
                # self.left(90)
                # self.forward(35)
                # self.left(90)
                # self.penup()
                # self.forward(25)
                # self.write("5",align="center",font=("Ariel",20,"normal"))
                # self.left(90)
                # self.forward(70)
                # self.left(90)
                # self.forward(55)
                # self.left(90)

                # self.pendown()
                # self.forward(35)
                # self.right(90)
                # self.forward(25)
                # self.left(90)
                # for i in range(4):
                # self.forward(50)
                # self.left(90)
                # self.forward(35)
                # self.left(90)
                # self.penup()
                # self.forward(25)
                # self.write("4",align="center",font=("Ariel",20,"normal"))
                # self.left(90)
                # self.forward(70)
                # self.left(90)
                # self.forward(55)
                # self.left(90)

                # self.pendown()
                # self.forward(35)
                # self.right(90)
                # self.forward(25)
                # self.left(90)
                # for i in range(4):
                # self.forward(50)
                # self.left(90)
                # self.forward(35)
                # self.left(90)
                # self.penup()
                # self.forward(25)
                # self.write("5",align="center",font=("Ariel",20,"normal"))
                # self.left(90)
                # self.forward(70)
                # self.left(90)
                # self.forward(55)
                # self.left(90)









    
    
    



