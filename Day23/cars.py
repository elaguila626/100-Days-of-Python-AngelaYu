from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_garage = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        randomization = random.randint(0,6)
        if randomization == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230,230)
            new_car.goto(280,random_y)
            self.car_garage.append(new_car)

    def move_car(self):
        for cars in self.car_garage:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT










