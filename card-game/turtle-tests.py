import turtle

turtle.setup(900, 900)

s = turtle.Screen()

s.title("game window")

t = turtle.Turtle()

t.speed(1)

t.pencolor("green")

# userInput = int(s.textinput("butt", "enter forward"))
userInput = int(input("enter forward amount"))

t.forward(userInput)

s.exitonclick()