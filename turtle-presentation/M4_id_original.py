import turtle
turtle.setup(width = 800,height=800,startx = None, starty=None)
turtle.penup()
turtle.speed(20)

turtle.setpos(-250.00,150.00)
turtle.write("This function is used to return \n"
             "a unique address of an object. \n"
             "Using the id() function helps determine \n"
             "whether a data type is mutable or immutable.\n"
             "The codes below are used to check for mutable/immutable \n"
             "data types \n"
             ,align="left",font=("Ariel",20,"bold"))


turtle.penup()
turtle.setpos(-370.00,-300.00)
turtle.pencolor("red")
turtle.write(">>> list=[3,6]\n"
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
             ,align="left",font=("Ariel",20,"italic"))
             

turtle.setpos(-30.00,-270.00)
turtle.pencolor("blue")
turtle.write(">>> integer=3\n"
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
             ,align="left",font=("Ariel",20,"italic"))
             
            
        
             
