import self

class Example2(self.self):
        def __init__(self):
                self.self.__init__(self)
                self.penup()
                self.setpos(-450.00,50.00)
                self.speed(20)
        def drawEx1(self):      
                self.write("Example\n"
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

                #2boxes
                self.fillcolor("light grey")
                self.begin_fill()
                for i in range(4):
                        self.forward(50)
                        self.right(90)
                self.forward(50)
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

                self.right(90)
                self.forward(45)
                self.right(90)
                self.forward(25)

                #LOWERBOX
                #arrow
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

                #2box
                self.left(80)
                self.forward(10)
                self.pendown()
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
                '''

               
                      
                      
                      
                      
                     


             
                                          

