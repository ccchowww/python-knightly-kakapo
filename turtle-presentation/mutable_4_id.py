import turtle

class Example1(turtle.Turtle):
        def __init__(self):
                turtle.Turtle.__init__(self)
                self.penup()
                self.setup(width = 800,height=800,startx = None, starty=None)
                self.speed(20)


        def drawEx4_id(self):
            self.setpos(-300.00,200.00)
            self.write("Function: id() \n"
                        ,align="left",font=("Ariel",50,"bold"))

            self.setpos(-250.00,50.00)
            self.write("This function is used to return \n"
                        "a unique address of an object. \n"
                        "Using the id() function helps determine \n"
                        "whether a data type is mutable or immutable.\n"
                        "The codes below are used to check for mutable/immutable \n"
                        "data types \n"
                        ,align="left",font=("Ariel",20,"bold"))


            self.penup()
            self.setpos(-370.00,-350.00)
            self.pencolor("red")
            self.write(">>> list=[3,6]\n"
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
                        

            self.setpos(-30.00,-320.00)
            self.pencolor("blue")
            self.write(">>> integer=3\n"
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
                        
                        
                    
                        
