import turtle

# wn = turtle.Screen()
# wn.bgcolor("#EEEEEC")
# wn.title("Object-based Turtles")
# wn.setup(1000,1000)

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

class PlayerHp(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("black")
        self.width(3)
        # self.units = []

    def fullHp(self):
        self.setpos(-400,-480)
        self.pendown()
        self.shape("square")
        self.color("#ffae00")
        self.shapesize(0.1,0.1,0)
        self.setx(self.xcor() + 50)
        self.sety(self.ycor() + 4)
        self.stamp()
        self.sety(self.ycor() - 4)
        while(self.xcor() < 280):
            self.setx(self.xcor() + 100)
            self.sety(self.ycor() + 4)
            self.stamp()
            self.sety(self.ycor() - 4)
        self.goto(400,-480)
        self.goto(400,-430)
        self.setx(self.xcor() - 50)
        self.sety(self.ycor() - 4)
        self.stamp()
        self.sety(self.ycor() + 4)
        while(self.xcor() > -280):
            self.setx(self.xcor() - 100)
            self.sety(self.ycor() - 4)
            self.stamp()
            self.sety(self.ycor() + 4)
        self.goto(-400,-430)
        self.goto(-400,-480)
        self.penup()

        self.setpos(-380,-455)
        self.color("#00ff6e")
        self.shapesize(1.8,0.8,0)
        x = self.xcor()
        for i in range(0,39):
            unit = self.stamp()
            # self.units.append(unit)
            x += 20
            self.setx(x)


    def decrement(self, units):
        self.clearstamps(-units)


# BossHp = BossHp()
# BossHp.fullHp()

# PlayerHp = PlayerHp()
# PlayerHp.fullHp()

# BossHp.decrement(2)
# BossHp.decrement(10)

# PlayerHp.decrement(2)
# PlayerHp.decrement(5)


# wn.exitonclick()
