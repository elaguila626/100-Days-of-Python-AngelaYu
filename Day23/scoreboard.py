from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-220, 230)
        self.write(f"Level: {self.level}", align = "center", font = ("Courier", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 230)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


