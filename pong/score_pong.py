from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.point_a = 0
        self.point_b = 0

    def points_message(self):
        self.goto(-200, 260)        
        self.write(f'POINT A: {self.point_a}', align='center',
                   font=('Arial', 20, 'normal'))
        self.goto(200, 260)
        self.write(f'POINT B: {self.point_b}', align='center',
                   font=('Arial', 20, 'normal'))

    def set_points(self, gamer):
        self.clear()
        if gamer == 'a':
            self.point_a += 1
        else:
            self.point_b += 1
        self.points_message()



