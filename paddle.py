from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")

        self.goto(x_pos, y_pos)

    def move_up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -300:
            self.goto(self.xcor(), self.ycor() - 20)



