from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
# with open("data.txt") as file:
#     highest_score = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        #self.point()


    def update_data(self):
        with open("data.txt",mode = "w") as highest_score:
            highest_score.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_data()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)




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









