# Part 2(Intro to Mutability)

import turtle
t = turtle.Turtle()
t.ht()
t.speed(10)

# Header
t.up()
t.goto(-610, 90)
t.down()
t.write("Since everything in Python is an Object, every variable holds an object\n"
        "instance. When an object is initiated,it is assigned a unique object id.\n"
        "Its type is defined at runtime and once set can never change, however\n"
        "its state can be changed if it is mutable. Simply put, a mutable object\n"
        "can be changed after it is created, and an immutable object can’t."
        , align="left", font=("Ariel", 30, "normal"))


# Part 3(Examples of Mutability)
t.width(2)
t.up()
t.goto(-610,-100)
t.down()
t.write("Examples of mutable and immutable data types", align="left", font=("Ariel", 30, "normal"))
t.up()
t.width(1)
t.goto(-610,-160)
t.down()
t.write("Mutable: List, Dictionary", align="left", font=("Ariel", 30, "normal"))
t.up()
t.goto(-610,-210)
t.down()
t.write("Immutable: String, Integers, Tuple", align="left", font=("Ariel", 30, "normal"))

turtle.done()
