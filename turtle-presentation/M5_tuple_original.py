import turtle
turtle.setup(width = 800,height=800,startx = None, starty=None)
turtle.penup()
turtle.speed(20)

turtle.setpos(-300.00,200.00)

turtle.setpos(-310.00,220.00)
turtle.write("Tuple \n"
             ,align="left",font=("Ariel",50,"bold"))


turtle.penup()
turtle.setpos(-370.00,20.00)
turtle.write("A tuple is a collection of items inside a parentheses (), seperated by comma. \n"
             "\n"
             "A tuple:\n"
             "=> is similar to a list but \n"
             "unlike lists tuples are immutable.\n"
             "=> can have items of different types (integer, string etc).\n"
             "  example:  >>> Tuple = ('hi',2,(1,2,3),[6,7,8])\n"
             ,align="left",font=("Ariel",20,"italic"))
turtle.penup()
turtle.setpos(-370.00,-50.00)
turtle.write("Difference between tuple and list\n"
             ,align="left",font=("Ariel",20,"bold"))
turtle.penup()
turtle.setpos(-370.00,-300.00)
turtle.write("=> Tuple and lists are quite similar however there\n"
             "a number of differences, the most apparent is that\n"
             "=>tuples are immutable while lists are mutable.\n"
             "=>tuples do not support item assignment\n"
             "  The code below will give a TypeError:'tuple' object does not support item assignment\n"
             "  >>> Tuple = ('hi',2,3.'6')\n"
             "  >>> Tuple[0] = '4' \n"
             "=> items in tuple cannot be changed/removed\n"
             "but the tuple itself can be deleted completely\n"
             ,align="left",font=("Ariel",20,"italic"))
