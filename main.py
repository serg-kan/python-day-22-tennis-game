from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # now we handle animation manually

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

scoreboard.print_score()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # detect collisions with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        print("collision")
        ball.bounce_x()

    # reset the game
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.update_score("left")
        scoreboard.print_score()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.update_score("right")
        scoreboard.print_score()

screen.exitonclick()