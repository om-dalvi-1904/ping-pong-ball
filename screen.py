from turtle import Turtle
pos=(0,-280)
class Screen1(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(pos)
        for i in range(0,28):
            self.color("white")
            self.setheading(90)
            self.forward(20)
            self.penup()
            self.forward(10)
            self.pendown()



