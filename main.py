from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
from screen import Screen1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
mid = Screen1()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.refresh_y()

    #detect collision with the paddle
    if ball.distance(r_paddle) < 50 and r_paddle.xcor() > 330 or ball.distance(l_paddle) < 50 and l_paddle.xcor() < -330:
        ball.refresh_x()

    if ball.xcor() > 330:
        # time.sleep(0.1)
        ball.restart()
        score.inc_left()

    if ball.xcor()< -330:
        # time.sleep(0.1)
        ball.restart()
        score.inc_right()
    if score.r_score > 3:
        game_on = False
        mid.write("Right player has won the game.",align="center", font=("Arial", 8, "normal"))
    if score.l_score > 3:
        game_on = False
        mid.write("Left player has won the game.",align="center", font=("Arial", 8, "normal"))


screen.exitonclick()