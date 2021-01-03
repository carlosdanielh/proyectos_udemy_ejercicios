from turtle import Turtle


FONT_COUNT = ('Arial', 20, 'normal')


class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.list_rectangle_sides = [[180, 40]]
        self.list_rectangle_sides.extend(self.list_rectangle_sides.copy())
        self.penup()
        self.goto(144, 300)
        self.hideturtle()
        self.pendown()
        self.pensize(4)
        self.draw_rectangle()

    def draw_rectangle(self):
        for pos in range(2):
            self.forward(self.list_rectangle_sides[pos][0])
            self.right(90)
            self.forward(self.list_rectangle_sides[pos][1])
            self.right(90)

    def point(self, list_guessed_state):
        self.goto(158, 260)
        guess = len(list_guessed_state)
        message = f'SCORE {guess}/50'
        self.clear()
        self.write(message, font=FONT_COUNT)
