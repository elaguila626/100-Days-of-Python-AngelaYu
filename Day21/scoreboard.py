from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        #self.point()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




    # def point(self):
    #     SCORE[0] += 1
    #     #print(SCORE[0])

#This is what I originally wrote w/ SCORE outside of the class.
    # def score(self):
    #     self.hideturtle()
    #     self.color("white")
    #     self.penup()
    #     self.setposition(-20, 280)
    #     self.write(f"Score: {SCORE[0]}", font=('Arial', 14, 'normal'))









