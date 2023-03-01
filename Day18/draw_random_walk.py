from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.colormode(255)

shift_list = [0,25,-25]
angle_move = [0, 90, 180, 270, 360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_change = (r,g,b)
    return color_change

def sporadic(shift,angle):
    tim.forward(random.choice(shift))
    tim.seth(random.choice(angle))
    tim.backward(random.choice(shift))
    tim.seth(random.choice(angle))

for move in range(100):
    tim.speed(10)
    tim.pensize(8)
    tim.color(random_color())
    sporadic(shift_list,angle_move)

my_screen = Screen()
my_screen.exitonclick()