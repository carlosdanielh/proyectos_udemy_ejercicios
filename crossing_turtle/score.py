from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.level_msg()


    def level_msg(self):
        self.goto(-250, 270)
        self.write(f'Level: {self.level}', align='center', font=('Arial', 14, 'normal'))

    def game_over_msg(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 14, 'normal'))

    def set_point(self):
        self.level += 1
