import colorgram
from turtle import Turtle, Screen
tim = Turtle()
import random

# colors = colorgram.extract ('image.jpg',20)
# def rgb_extraction(colors_number):
#     color_list = []
#     for item in range(0, colors_number):
#         add_color = colors[item]
#         rgb = add_color.rgb
#         r = rgb.r
#         g = rgb.g
#         b = rgb.b
#         color_tuple = (r,g,b)
#         color_list.append(color_tuple)
#     return color_list
#
# print(rgb_extraction(20))

my_screen = Screen()
my_screen.colormode(255)
color_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46)]
tim.hideturtle()
tim.speed(10)
y = 0

def move_dot():
    tim.setheading(225)
    tim.penup()
    tim.forward(290)
    tim.pendown()
    tim.setheading(0)
    for item in range(10):
        tim.dot(20,(random.choice(color_list)))
        tim.penup()
        tim.forward(50)
        tim.pendown()

for movement in range(10):
    move_dot()
    y += 50
    tim.penup()
    tim.goto(0,y)
    tim.pendown()

my_screen.exitonclick()


