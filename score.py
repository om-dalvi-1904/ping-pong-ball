from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-50, 190)
        self.write(self.l_score, align="center", font=("arial", 80, "normal"))
        self.goto(50, 190)
        self.write(self.r_score, align="center", font=("arial", 80, "normal"))

    def inc_right(self):
        self.r_score += 1
        self.update()
    def inc_left(self):
        self.l_score += 1
        self.update()

