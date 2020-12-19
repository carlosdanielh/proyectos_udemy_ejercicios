from turtle import Turtle


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(7, 1)
        self.penup()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def draw_paddle_right(self):
        self.goto(350, 0)

    def draw_paddle_left(self):
        self.goto(-350, 0)
