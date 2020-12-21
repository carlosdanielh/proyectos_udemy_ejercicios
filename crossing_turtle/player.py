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
        self.y = self.ycor() + 10
        self.goto(0, self.y)

    def down(self):
        self.y = self.ycor() - 5
        self.goto(0, self.y)

    def over_pass_top_screen(self):
        if self.ycor() > 300:
            return True

    def start_position(self):
        self.goto(0, -280)