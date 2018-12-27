import turtle
import time

def ResizeScreen(width, height):
    screenWidthUnit = width // 100
    screenHeightUnit = height // 100

    effectiveScreenWidth = screenWidthUnit * 100
    effectiveScreenHeight = screenHeightUnit * 100

    return (effectiveScreenWidth, effectiveScreenHeight, screenWidthUnit, screenHeightUnit)

t = turtle.Turtle()
t.shapesize(4, 5)
t.speed(7)
wn = turtle.Screen()
wn.setup(width=1.0,height=1.0)
wn.title("Turtle Presentation")

wnWidth = wn.window_width()
wnHeight = wn.window_height()
print(wnWidth, wnHeight)

# Get new dimensions that will be compatible with any user's screen.
newScreen = ResizeScreen(wnWidth, wnHeight)

# return from ResizeScreen:
#   newScreen = (effectiveWidth, effectiveHeight, widthUnit, heightUnit)
newScreenWidth = newScreen[0]
newScreenHeight = newScreen[1]

# Convert window to compatible dimensions
wn.setup(width=newScreenWidth,height=newScreenHeight)
print(newScreenWidth, newScreenHeight)
widthUnit = newScreen[2]
heightUnit = newScreen[3]
print(widthUnit, heightUnit)

# 1st slide
def write_title():
    # turtle.tracer(0, 0)
    t.up()
    t.goto(-widthUnit, -heightUnit*8)
    t.down()
    t.write("Mutability", align="center", font=("Arial", 125, "normal"))
    t.up()
    t.goto(widthUnit*30, -heightUnit*27)
    # turtle.update()
    t.onclick(explanation)
    # turtle.tracer(0, 0)
    # t.up()
    # t.goto(-20, -85)
    # t.down()
    # t.write("Mutability", align="center", font=("Arial", 125, "normal"))
    # t.up()
    # t.goto(600, -275)
    # turtle.update()
    # t.onclick(explanation)

# 2nd slide
def explanation(x, y):
    t.clear()
    t.up()
    t.goto(-widthUnit*31, heightUnit*9)
    t.down()
    t.write("Since everything in Python is an object, every variable references an object\n"
            "instance. When an object is initiated,it is assigned a unique object id.\n"
            "Its type is defined at runtime and once set can never change, however\n"
            "its state can be changed if it is mutable. Simply put, a mutable object\n"
            "can be changed after it is created, and an immutable object can’t."
            , align="left", font=("Arial", 30, "normal"))
    t.up()
    t.goto(widthUnit*30, -heightUnit*27)
    t.onclick(examples_of_mutability)
    # t.clear()
    # turtle.tracer(0, 0)
    # t.up()
    # t.goto(-610, 90)
    # t.down()
    # t.write("Since everything in Python is an object, every variable holds an object\n"
    #         "instance. When an object is initiated,it is assigned a unique object id.\n"
    #         "Its type is defined at runtime and once set can never change, however\n"
    #         "its state can be changed if it is mutable. Simply put, a mutable object\n"
    #         "can be changed after it is created, and an immutable object can’t."
    #         , align="left", font=("Arial", 30, "normal"))
    # t.up()
    # t.goto(600, -275)
    # turtle.update()
    # t.onclick(examples_of_mutability)

def examples_of_mutability(x, y):
    t.width(2)
    t.up()
    t.goto(-widthUnit*31, -heightUnit*10)
    t.down()
    t.write("Examples of mutable and immutable data types", align="left", font=("Arial", 30, "normal"))
    t.up()
    t.width(1)
    t.goto(-widthUnit*31, -heightUnit*16)
    t.down()
    t.write("Mutable: List, Dictionary", align="left", font=("Arial", 30, "normal"))
    t.up()
    t.goto(-widthUnit*31, -heightUnit*21)
    t.down()
    t.write("Immutable: String, Integers, Tuple", align="left", font=("Arial", 30, "normal"))
    t.up()
    t.goto(widthUnit*30, -heightUnit*27)
    t.onclick(how_mutability_works)
    # turtle.tracer(0, 0)
    # t.width(2)
    # t.up()
    # t.goto(-610, -100)
    # t.down()
    # t.write("Examples of mutable and immutable data types", align="left", font=("Arial", 30, "normal"))
    # t.up()
    # t.width(1)
    # t.goto(-610, -160)
    # t.down()
    # t.write("Mutable: List, Dictionary", align="left", font=("Arial", 30, "normal"))
    # t.up()
    # t.goto(-610, -210)
    # t.down()
    # t.write("Immutable: String, Integers, Tuple", align="left", font=("Arial", 30, "normal"))
    # t.up()
    # t.goto(600, -275)
    # turtle.update()
    # t.onclick(how_mutability_works)

# 3rd slide
def how_mutability_works(x, y):
    t.clear()
    # turtle.tracer(0, 0)
    t.up()
    t.goto(0, heightUnit*25)
    t.down()
    t.write("So how does mutability works?", align="center", font=("Arial", 50, "normal"))
    t.up()
    t.goto(0, -heightUnit*5)
    t.write("An easy way to understand that is if you have a look at an objects ID.\n"
            "The built-in function id() returns the identity of an object as an integer. \n"
            "This integer usually corresponds to the object’s location in memory, \n"
            "although this is specific to the Python implementation and the platform\n"
            "being used. The is operator compares the identity of two objects."
            , align="center", font=("Arial", 30, "normal"))
    t.up()
    t.goto(widthUnit*30, -heightUnit*27)
    # turtle.update()
    t.onclick(string_example)
    # t.clear()
    # turtle.tracer(0, 0)
    # t.up()
    # t.goto(0, 250)
    # t.down()
    # t.write("So how does mutability works?", align="center", font=("Arial", 50, "normal"))
    # t.up()
    # t.goto(0, -50)
    # t.write("An easy way to understand that is if you have a look at an objects ID.\n"
    #         "The built-in function id() returns the identity of an object as an integer. \n"
    #         "This integer usually corresponds to the object’s location in memory, \n"
    #         "although this is specific to the Python implementation and the platform\n"
    #         "being used. The is operator compares the identity of two objects."
    #         , align="center", font=("Arial", 30, "normal"))
    # t.up()
    # t.goto(600, -275)
    # turtle.update()
    # t.onclick(string_example)

# 4th slide
def string_example(x, y):
    t.clear()
    # turtle.tracer(0, 0)
    # Header 1
    t.up()
    t.goto(-widthUnit*31, heightUnit*27)
    t.down()
    t.write("e.g. String", align="left", font=("Arial", 35, "normal"))
    t.up()

    # Header 2
    t.goto(-widthUnit*31, heightUnit*17)
    # t.down()
    t.write("X = 10", align="left", font=("Arial", 30, "normal"))
    t.goto(t.xcor(), t.ycor() - heightUnit*5)
    t.write("X = 20", align="left", font=("Arial", 30, "normal"))
    t.goto(t.xcor(), t.ycor() + heightUnit*5)
    # t.up()

    # X's Square
    t.speed(0)
    t.goto(-widthUnit*28, heightUnit*5)
    t.down()
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(4):
        t.fd(widthUnit*3)
        t.rt(90)
    t.end_fill()
    t.up()

    # X
    t.goto(-widthUnit*27, heightUnit*0)
    t.down()
    t.color("black")
    t.write("X", align="left", font=("Arial", 30, "normal"))
    t.up()

    # Line
    t.color("blue")
    t.speed(8)
    t.goto(-widthUnit*19, heightUnit*3)
    t.down()
    t.fd(heightUnit*30)
    t.up()
    t.goto(-widthUnit*3, heightUnit*3)
    t.down()
    t.lt(160)
    t.fd(heightUnit*4)
    t.up()
    t.fd(-heightUnit*4)
    # t.goto(-widthUnit*3, heightUnit*3)
    t.down()
    t.lt(40)
    t.fd(heightUnit*4)
    t.lt(160)
    t.up()

    # 10's square
    t.pencolor("blue")
    t.width(5)
    t.goto(-widthUnit, heightUnit*10)
    t.down()
    for i in range(4):
        t.fd(heightUnit*15)
        t.rt(90)
    t.up()

    # ID 1
    t.pencolor("black")
    t.width(1)
    t.goto(widthUnit*2, heightUnit*10)
    t.down()
    t.write("ID 1", align="left", font=("Arial", 30, "normal"))
    t.up()

    # 10
    t.goto(widthUnit*2, heightUnit)
    t.down()
    t.write("10", align="left", font=("Arial", 30, "normal"))
    t.up()

    # Dotted line
    t.goto(-widthUnit*19, -heightUnit)
    t.speed(3)
    t.color("red")
    t.down()
    t.rt(30)
    for i in range(19):
        t.up()
        t.fd(heightUnit)
        t.down()
        t.fd(heightUnit)
    t.up()
    # t.goto(-widthUnit*2, -heightUnit)
    t.down()
    t.lt(160)
    t.fd(heightUnit*4)
    t.up()
    t.fd(-heightUnit*4)
    # t.goto(-widthUnit*2, -heightUnit*21)
    t.down()
    t.lt(40)
    t.fd(heightUnit*4)
    t.lt(160)
    t.lt(30)
    t.up()

    # 20's square
    t.pencolor("red")
    t.width(5)
    t.goto(-widthUnit, -heightUnit*13)
    t.down()
    for i in range(4):
        t.fd(heightUnit*15)
        t.rt(90)
    t.up()

    # ID 2
    t.pencolor("black")
    t.width(1)
    t.goto(widthUnit*2, -heightUnit*13)
    t.down()
    t.write("ID 2", align="left", font=("Arial", 30, "normal"))
    t.up()

    # 20
    t.goto(widthUnit*2, -heightUnit*23)
    t.write("20", align="left", font=("Arial", 30, "normal"))
    t.fillcolor("black")
    t.up()

    # cross old X
    t.hideturtle()
    time.sleep(1)
    t.showturtle()
    t.goto(-widthUnit*21, heightUnit*3)
    t.color("red")
    t.down()
    t.width(5)
    t.forward(heightUnit*60)
    t.up()

    # cross ID 1
    t.color("red")
    t.width(5)
    t.goto(widthUnit*2, heightUnit*12)
    t.down()
    t.forward(heightUnit*7)
    t.up()

    # thicken new X line
    t.goto(-widthUnit*19, -heightUnit)
    t.speed(4)
    t.color("black")
    t.width(3)
    t.down()
    t.rt(30)
    for i in range(19):
        t.fd(heightUnit*2)
    t.up()
    # t.goto(-widthUnit*2, -heightUnit)
    t.down()
    t.lt(160)
    t.fd(heightUnit*4)
    t.up()
    t.fd(-heightUnit*4)
    # t.goto(-widthUnit*2, -heightUnit*21)
    t.down()
    t.lt(40)
    t.fd(heightUnit*4)
    t.lt(160)
    t.lt(30)
    t.up()


    t.goto(widthUnit*30, -heightUnit*27)
    t.onclick(list_example)


# 5th slide
def list_example(x, y):
    t.clear()
    turtle.tracer(0, 0)

    # Header 1
    t.up()
    t.goto(-620, 265)
    t.write("e.g. List", align="left", font=("Ariel", 35, "normal"))

    # Header 2
    t.goto(-620, 150)
    t.write("X = [10] \nX[0] = 20", align="left", font=("Ariel", 30, "normal"))

    # X's square
    t.begin_fill()
    t.fillcolor("orange")
    t.goto(-550, 80)
    t.down()
    for i in range(4):
        t.fd(150)
        t.rt(90)
    t.end_fill()
    t.up()

    # X
    t.goto(-485, -15)
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
    t.goto(-170, 5)
    t.down()
    t.lt(160)
    t.fd(40)
    t.up()
    t.goto(-170, 5)
    t.down()
    t.lt(40)
    t.fd(40)
    t.lt(160)
    t.up()

    # Blank Square
    t.pencolor("lightgreen")
    t.width(5)
    t.goto(-125, 80)
    t.down()
    for i in range(4):
        t.fd(150)
        t.rt(90)

    # ID
    t.goto(-70, 80)
    t.pencolor("black")
    t.width(1)
    t.write("ID", align="left", font=("Ariel", 30, "normal"))
    t.up()

    # Split Line(Up)
    t.goto(50, 25)
    t.lt(30)
    t.down()
    t.fd(170)
    t.up()
    t.goto(205, 115)
    t.down()
    t.lt(160)
    t.fd(40)
    t.up()
    t.goto(205, 115)
    t.down()
    t.lt(40)
    t.fd(40)
    t.lt(160)
    t.rt(30)
    t.up()

    # 10's Square
    t.pencolor("blue")
    t.width(5)
    t.goto(220, 220)
    t.down()
    for i in range(4):
        t.fd(150)
        t.rt(90)
    t.up()

    # 10
    t.pencolor("black")
    t.width(1)
    t.goto(275, 125)
    t.write(10, align="left", font=("Ariel", 30, "normal"))
    t.up()

    # Dotted Split Line(Down)
    t.goto(50, -15)
    t.rt(30)
    t.down()
    for i in range(9):
        t.up()
        t.fd(10)
        t.down()
        t.fd(10)
    t.up()
    t.goto(210, -107)
    t.down()
    t.lt(160)
    t.fd(40)
    t.up()
    t.goto(210, -107)
    t.down()
    t.lt(40)
    t.fd(40)
    t.lt(190)
    t.up()

    # 20's Square
    t.pencolor("red")
    t.width(5)
    t.goto(220, -50)
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
    t.fillcolor("black")
    t.up()
    t.goto(600, -275)
    turtle.update()
    t.onclick(ID_function)
    # t.clear()

    # # Header 1
    # t.up()
    # t.goto(-widthUnit*31, heightUnit*27)
    # t.write("e.g. List", align="left", font=("Arial", 35, "normal"))

    # # Header 2
    # t.goto(-widthUnit*31, heightUnit*15)
    # t.write("X = [10] \nX[0] = 20", align="left", font=("Arial", 30, "normal"))

    # # X's square
    # t.begin_fill()
    # t.fillcolor("orange")
    # t.goto(-widthUnit*28, heightUnit*8)
    # t.down()
    # for i in range(4):
    #     t.fd(heightUnit*15)
    #     t.rt(90)
    # t.end_fill()
    # t.up()

    # # X
    # t.goto(-widthUnit*24, -heightUnit)
    # t.down()
    # t.write("X", align="left", font=("Arial", 30, "normal"))
    # t.up()

    # # Forward Line
    # t.lt(90)
    # t.fd(20)
    # t.rt(90)
    # t.fd(115)
    # t.down()
    # t.fd(200)
    # t.up()
    # t.goto(-170, 5)
    # t.down()
    # t.lt(160)
    # t.fd(40)
    # t.up()
    # t.goto(-170, 5)
    # t.down()
    # t.lt(40)
    # t.fd(40)
    # t.lt(160)
    # t.up()

    # # Blank Square
    # t.pencolor("lightgreen")
    # t.width(5)
    # t.goto(-125, 80)
    # t.down()
    # for i in range(4):
    #     t.fd(150)
    #     t.rt(90)

    # # ID
    # t.goto(-70, 80)
    # t.pencolor("black")
    # t.width(1)
    # t.write("ID", align="left", font=("Arial", 30, "normal"))
    # t.up()

    # # Split Line(Up)
    # t.goto(50, 25)
    # t.lt(30)
    # t.down()
    # t.fd(170)
    # t.up()
    # t.goto(205, 115)
    # t.down()
    # t.lt(160)
    # t.fd(40)
    # t.up()
    # t.goto(205, 115)
    # t.down()
    # t.lt(40)
    # t.fd(40)
    # t.lt(160)
    # t.rt(30)
    # t.up()

    # # 10's Square
    # t.pencolor("blue")
    # t.width(5)
    # t.goto(220, 220)
    # t.down()
    # for i in range(4):
    #     t.fd(150)
    #     t.rt(90)
    # t.up()

    # # 10
    # t.pencolor("black")
    # t.width(1)
    # t.goto(275, 125)
    # t.write(10, align="left", font=("Arial", 30, "normal"))
    # t.up()

    # # Dotted Split Line(Down)
    # t.goto(50, -15)
    # t.rt(30)
    # t.down()
    # for i in range(9):
    #     t.up()
    #     t.fd(10)
    #     t.down()
    #     t.fd(10)
    # t.up()
    # t.goto(210, -107)
    # t.down()
    # t.lt(160)
    # t.fd(40)
    # t.up()
    # t.goto(210, -107)
    # t.down()
    # t.lt(40)
    # t.fd(40)
    # t.lt(190)
    # t.up()

    # # 20's Square
    # t.pencolor("red")
    # t.width(5)
    # t.goto(220, -50)
    # t.down()
    # for i in range(4):
    #     t.fd(150)
    #     t.rt(90)
    # t.up()

    # # 20
    # t.pencolor("black")
    # t.width(1)
    # t.goto(275, -145)
    # t.write(20, align="left", font=("Arial", 30, "normal"))
    # t.fillcolor("black")
    # t.up()
    # t.goto(600, -275)
    # t.onclick(ID_function)


# 6th slide
def ID_function(x, y):
    t.clear()
    turtle.tracer(0, 0)
    t.up()
    t.goto(0, 250)
    t.setpos(-250.00, 150.00)
    t.down()
    t.write("The id() function is used to return \n"
            "a unique address of an object. \n"
            "Using it helps determine \n"
            "whether a data type is mutable or immutable.\n"
            "The codes below are used to check for mutable/immutable \n"
            "data types \n"
            , align="left", font=("Arial", 20, "bold"))

    t.penup()
    t.setpos(-370.00, -300.00)
    t.pencolor("red")
    t.write(">>> list=[3,6]\n"
            ">>> print(id(list)) \n"
            "4345081736 \n"
            ">>> list.append(9) \n"
            ">>> print(list) \n"
            "[3,6,9]\n"
            ">>> print(id(list))\n"
            "4345081736 \n"
            "\n"
            "It can be seen that the id (address)\n"
            "of the list did not change, \n"
            "so no new copy of the list is\n"
            "created hence the reference remains\n"
            "unchanged \n"
            , align="left", font=("Arial", 20, "italic"))

    t.setpos(-30.00, -270.00)
    t.pencolor("blue")
    t.write(">>> integer=3\n"
            ">>> print(id(integer)) \n"
            "4452056208 \n"
            ">>> integer+=1 \n"
            ">>> print(integer) \n"
            "4 \n"
            ">>> print(id(integer)) \n"
            "4452056240 \n"
            "\n"
            "It can be seen that the id(address) changes;\n"
            " A new copy of the integer is created \n"
            "which points towards the 4. \n"
            "Hence, changing its address \n"
            , align="left", font=("Arial", 20, "italic"))
    t.up()
    t.goto(600, -275)
    turtle.update()
    t.onclick(mutability_immutability)

# 7th Slide
def mutability_immutability(x, y):
    t.clear()
    turtle.tracer(0, 0)
    t.up()
    t.goto(0, -100)
    t.down()
    t.pencolor("black")
    t.write("Even though lists are mutable, \n"
            "they behave differently in different situations\n"
            , align="center", font=("Arial", 40, "normal"))

    t.up()
    t.goto(600, -275)
    turtle.update()
    t.onclick(list_eg_1)

# 8th Slide
def list_eg_1(x, y):
    t.clear()
    turtle.tracer(0, 0)
    t.up()
    t.goto(0, -100)
    t.setpos(-450.00, -100.00)
    t.down()
    t.write(" Given this code:\n "
            "\n"
            " x=[5,4]\n"
            " print(id(x))\n"
            " x*=2\n"
            " print(id(x))\n"
            "\n"
            "When this code is executed the list is updated\n"
            "without generating a new copy of x\n"
            "or changing its reference\n"
            , align="left", font=("Arial", 30, "normal"))
    
    # Animation
    t.penup()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.write("x\n", align="left", font=("Arial", 30, "normal"))
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()
    t.fillcolor("light green")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.pendown()

    # arrow
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(20)
    t.pendown()
    t.forward(50)
    t.left(160)
    t.forward(15)
    t.backward(15)
    t.left(45)
    t.forward(15)
    t.backward(15)
    t.right(205)

    # box
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.pendown()
    # 4boxes
    t.fillcolor("light grey")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    for j in range(3):
        t.forward(100)
        t.right(90)
        for i in range(3):
            t.forward(50)
            t.right(90)
    t.end_fill()
    t.penup()

    # small boxes

    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()

    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("4", align="center", font=("Arial", 30, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("5", align="center", font=("Arial", 30, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("4", align="center", font=("Arial", 30, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("5", align="center", font=("Arial", 30, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.fillcolor("black")
    t.lt(90)
    t.up()
    t.goto(600, -275)
    turtle.update()
    t.onclick(list_eg_2)


def list_eg_2(x, y):
    t.clear()
    turtle.tracer(0, 0)
    t.rt(90)
    t.up()
    t.showturtle()
    t.goto(0, -100)
    t.setpos(-200.00, 50.00)
    t.down()
    t.write("However,lists will behave differently in this situation:\n"
            "\n"
            "x=[5,4]\n"
            "print(id(x))\n"
            "x=x*2\n"
            "print(id(x))\n"
            "\n"
            "When this code is executed the: \n"
            "a new list is created which is assigned to x\n"
            "hence modifying the identifier of x"
            , align="left", font=("Arial", 25, "normal"))

    # xbox
    t.penup()
    t.forward(100)
    t.write("x\n", align="left", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()
    t.fillcolor("light green")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

    # UPPERBOX
    # arrow
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()
    t.forward(10)
    for i in range(6):
        t.pendown()
        t.forward(5)
        t.penup()
        t.forward(5)
    t.pendown()
    t.left(160)
    t.forward(10)
    t.backward(10)
    t.left(45)
    t.forward(10)
    t.backward(10)
    t.right(205)

    # box
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.pendown()

    # 2boxes
    t.fillcolor("light grey")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.forward(50)
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.pendown()

    # smallbox
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("4", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("5", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(25)

    # LOWERBOX
    # arrow
    t.right(170)
    t.pendown()
    t.forward(150)
    t.left(160)
    t.forward(15)
    t.backward(15)
    t.left(45)
    t.forward(15)
    t.backward(15)
    t.right(205)
    t.penup()

    # 2box
    t.left(80)
    t.forward(10)
    t.pendown()
    t.fillcolor("light grey")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    for j in range(3):
        t.forward(100)
        t.right(90)
        for i in range(3):
            t.forward(50)
            t.right(90)
    t.end_fill()
    t.penup()

    # small boxes
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()

    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("4", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("5", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("4", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("5", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)
    t.fillcolor("black")
    t.up()
    t.goto(600, -275)
    t.lt(90)
    turtle.update()
    t.onclick(str_eg)


def str_eg(x, y):
    t.clear()
    turtle.tracer(0, 0)
    t.rt(90)
    t.st()
    t.up()
    t.showturtle()
    t.goto(0, -100)
    t.setpos(-200.00, 150.00)
    t.down()
    t.write("For immutable objects \n"
            "x=x*2 and x*=2 behave the same way;\n"
            "the copy of x is created as well as \n"
            "its reference is updated.\n"
            "This is shown below for a string x='hello'. "
            , align="left", font=("Arial", 30, "normal"))

    t.penup()
    t.forward(150)
    t.left(90)
    t.write("x\n", align="left", font=("Arial", 20, "normal"))
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.pendown()
    t.fillcolor("light green")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.pendown()

    # UPPERBOX
    # arrow
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()
    t.forward(10)
    for i in range(6):
        t.pendown()
        t.forward(5)
        t.penup()
        t.forward(5)

    t.penup()
    t.forward(5)
    t.pendown()
    t.left(160)
    t.forward(10)
    t.backward(10)
    t.left(45)
    t.forward(10)
    t.backward(10)
    t.right(207)

    # box
    t.penup()
    t.forward(10)
    t.left(92)
    t.forward(25)
    t.right(90)
    t.pendown()
    t.fillcolor("light grey")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

    # 2nd arrow
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    # whitebox
    t.left(90)
    t.forward(25)
    t.right(90)
    for i in range(4):
        t.forward(50)
        t.right(90)

    t.penup()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.write("hello", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)

    # DOWNBOXES
    t.right(135)
    t.pendown()
    t.forward(180)
    t.right(180)
    t.forward(180)
    t.left(160)
    t.forward(15)
    t.backward(15)
    t.left(45)
    t.forward(15)
    t.backward(15)
    t.right(205)
    t.penup()
    t.left(45)

    # twoboxes
    t.forward(10)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.forward(50)
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()

    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("hello", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)
    t.pendown()
    t.forward(35)
    t.right(90)
    t.forward(25)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.forward(35)
    t.left(90)
    t.penup()
    t.forward(25)
    t.write("hello", align="center", font=("Arial", 20, "normal"))
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(55)
    t.left(90)

    t.fillcolor("black")
    t.up()
    t.goto(600, -275)
    t.lt(90)
    turtle.update()
    t.onclick(Tuple)

# 9th Slide
def Tuple(x, y):
    t.clear()
    turtle.tracer(0, 0)
    t.st()
    t.up()
    t.showturtle()
    t.goto(0, -100)

    t.setpos(-310.00, 220.00)
    t.write("Tuple \n"
            , align="left", font=("Arial", 50, "bold"))

    t.penup()
    t.setpos(-370.00, 20.00)
    t.write("A tuple is a collection of items inside a parentheses (), seperated by comma. \n"
            "\n"
            "A tuple:\n"
            "=> is similar to a list but \n"
            "unlike lists tuples are immutable.\n"
            "=> can have items of different types (integer, string etc).\n"
            "  example:  >>> Tuple = ('hi',2,(1,2,3),[6,7,8])\n"
            , align="left", font=("Arial", 20, "italic"))

    t.penup()
    t.setpos(-370.00, -50.00)
    t.write("Difference between tuple and list\n"
            , align="left", font=("Arial", 20, "bold"))

    t.penup()
    t.setpos(-370.00, -300.00)
    t.write("=> Tuple and lists are quite similar however there\n"
            "a number of differences, the most apparent is that\n"
            "=>tuples are immutable while lists are mutable.\n"
            "=>tuples do not support item assignment\n"
            "  The code below will give a TypeError:'tuple' object does not support item assignment\n"
            "  >>> Tuple = ('hi',2,3.'6')\n"
            "  >>> Tuple[0] = '4' \n"
            "=> items in tuple cannot be changed/removed\n"
            "but the tuple itself can be deleted completely\n"
            , align="left", font=("Arial", 20, "italic"))

    t.fillcolor("black")
    t.up()
    t.goto(600, -275)
    t.seth(90)
    t.rt(90)
    turtle.update()
    t.onclick(why_mutability_matters)

# 10th Slide
def why_mutability_matters(x, y):
    t.clear()
    turtle.tracer()
    t.ht()
    t.up()
    t.goto(425, 250)
    t.down()
    t.write("Why does mutability matters in coding?", align="right", font=("Arial", 40, "normal"))

    t.up()
    t.goto(0, -20)
    t.down()
    t.write('Python handles mutable and immutable objects differently. Immutable \n'
            'objects are quicker to access than mutable objects yet fundamentally \n'
            'expensive to "change", because doing so involves creating a copy, \n'
            'hence wasting much more memory creating and throwing away objects'
            , align="center", font=("Arial", 30, "normal"))
    t.up()
    t.goto(600, -275)
    turtle.update()

write_title()
turtle.done()

