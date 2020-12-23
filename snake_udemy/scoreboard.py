from turtle import Turtle
import os

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.set_point()
        self.run_game()
        self.high_score = self.extract_last_high_score()
        self.high_score_msg()

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
        self.write('arrow up - start game', align='left',
                   font=('Arial', 10, 'normal'))

    def add_point(self):
        self.point += 1
        self.clear()
        self.set_point()
        self.run_game()
        if self.point > self.high_score:
            self.high_score = self.point
            with open('..\\ejercicios\\udemy_projects\\snake_udemy\\data.txt', 'w') as file_point:
                file_point.write(str(self.high_score))

    def high_score_msg(self):
        self.goto(130, -240)
        self.write(f'HIGH SCORE: {self.high_score}', align='center',
                   font=('Arial', 19, 'normal'))

    def extract_last_high_score(self):
        with open('..\\ejercicios\\udemy_projects\\snake_udemy\\data.txt') as file_point:
            file_high = file_point.read()
            return int(file_high)           
