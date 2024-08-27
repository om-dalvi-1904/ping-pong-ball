from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=20, stretch_len=20)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def refresh_y(self):
        self.y_move *= -1

    def refresh_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.refresh_x()
        self.move_speed = 0.1
        self.goto(0,0)

