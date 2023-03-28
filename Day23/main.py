import time
from turtle import Screen
from player import Player
from cars import Car
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = Car()

screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # move_car()
    car.create_car()
    car.move_car()

    #collision with car
    for cars in car.car_garage:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            screen.exitonclick()

    #turtle crosses finish line
    if player.ycor() > player.finish_line:
        player.reset()
        car.level_up()
        scoreboard.update_scoreboard()


