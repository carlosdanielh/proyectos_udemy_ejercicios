from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x, y)

    def collide(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            return True
