from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red","yellow")

# intermittent blank spaces
for move in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()