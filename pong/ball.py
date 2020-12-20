from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def collide(self, something):
        try:
            top_window = (something.window_height() - 20) / 2
            bottom_window = (something.window_height() - 20) / - 2

            if self.ycor() >= top_window or self.ycor() <= bottom_window:
                return True
        except AttributeError:
            if something.xcor() == 350:
                if self.distance(something) < 20 or\
                   self.distance(something) < 80 and\
                   self.xcor() >= something.xcor() - 20:
                    return True
            if something.xcor() == -350:
                if self.distance(something) < 20 or\
                   self.distance(something) < 80 and\
                   self.xcor() <= something.xcor() + 20:
                    return True

    def bounce_walls(self):
        self.y *= -1

    def bounce_tables(self):
        self.x *= -1

    def touch_empty_space(self):
        if self.xcor() >= 390 or self.xcor() <= -390:
            return True

    def start_game_again(self):
        self.goto(0, 0)
        self.bounce_tables()
