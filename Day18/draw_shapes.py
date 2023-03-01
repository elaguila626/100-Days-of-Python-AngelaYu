from turtle import Turtle, Screen
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red","yellow")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 10):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)

my_screen = Screen()
my_screen.exitonclick()
