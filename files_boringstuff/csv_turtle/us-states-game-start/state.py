import pandas
from pathlib import Path
from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        the_path = str(Path.cwd() / 'data' / '50_states.csv')
        self.data_states = pandas.read_csv(the_path)
        self.guess = 0
        self.guess_state_list = []
        self.hideturtle()
        self.penup()

    def check_state(self, user_answer):
        user_answer = self.format_answer(user_answer)
        if len(self.data_states[self.data_states.state == user_answer]) == 1\
                and user_answer not in self.guess_state_list:
            self.guess_state_list.append(user_answer)
            self.guess += 1
            return True
        return False

    def get_coordinate(self, user_answer):
        x = self.data_states[self.data_states.state == user_answer].x
        y = self.data_states[self.data_states.state == user_answer].y
        return [x.to_list(), y.to_list()]

    def guess_message(self):
        if self.guess == 0:
            message = 'U.S STATE GAME'
        else:
            message = f'GUESSED {self.guess}/50 U.S STATE GAME'
        return message

    def format_answer(self, answer):
        return answer.lower().title()

    def move_state_to_map(self, answer):
        answer = self.format_answer(answer)
        position = self.get_coordinate(answer)
        x_pos = position[0][0]
        y_pos = position[1][0]
        self.goto(x_pos, y_pos)
        self.write(answer, font=('Arial', 7, 'normal'))     
