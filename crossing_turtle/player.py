from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape('turtle')
        self.color('yellow')
        self.penup()
        self.goto(0, -280)

    def up(self):
        y = self.ycor() + 10
        self.goto(0, y)

    def down(self):
        y = self.ycor() - 10
        self.goto(0, y)

    def over_pass_top_screen(self):
        if self.ycor() > 300:
            return True

    def start_position(self):
        self.screen.tracer(0) 
        self.goto(0, -280)
        self.screen.update()
