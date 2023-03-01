from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red","yellow")

#create a square
for _ in range(4):
    tim.right(90)
    tim.forward(100)

my_screen = Screen()
my_screen.exitonclick()