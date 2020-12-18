from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0 
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 220)
        self.set_point()

    def set_point(self):
        self.write(f'POINT OF SNAKE: {self.point}', align='center',
                   font=('Arial', 19, 'normal'))

    def game_over_message(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=('Arial', 19, 'normal'))

    def add_point(self):
        self.point += 1
        self.clear()
        self.set_point()
