from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.score_l = 0
        self.score_r = 0

    def update_score(self, player):
        if player == "left":
            self.score_l += 1
        else:
            self.score_r += 1

    def print_score(self):
        self.clear()
        self.write(f"{self.score_l} : {self.score_r}", move=False, align="center", font=("Arial", 16, "normal"))
