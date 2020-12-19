from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.set_point()
        self.run_game()

    def set_point(self):
        self.goto(0, 220)
        self.write(f'POINT OF SNAKE: {self.point}', align='center',
                   font=('Arial', 19, 'normal'))

    def game_over_message(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=('Arial', 19, 'normal'))

    def run_game(self):
        self.goto(-230, -190)
        self.write('space - pause', align='left', font=('Arial', 10, 'normal'))
        self.goto(-230, -210)
        self.write('c - continue', align='left', font=('Arial', 10, 'normal'))
        self.goto(-230, -230)
        self.write('arrow up - start game', align='left', font=('Arial', 10, 'normal'))

    def add_point(self):
        self.point += 1
        self.clear()
        self.set_point()
        self.run_game()
