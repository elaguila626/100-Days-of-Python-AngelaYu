from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red","yellow")

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_change = (r,g,b)
    return color_change

def draw_circles(angle_turtle):
    tim.circle(100)
    tim.seth(angle_turtle)

position =0

while position <= 360:
    tim.speed(50)
    tim.color(random_color())
    position += 5
    draw_circles(position)

my_screen = Screen()
my_screen.exitonclick()