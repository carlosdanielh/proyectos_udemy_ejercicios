import pandas
from pathlib import Path
from turtle import Turtle

PATH_OF_50_STATES_CSV = str(Path.cwd() / 'data' / '50_states.csv')
PATH_OF_NO_GUESSED_STATE = str(Path.cwd() / 'data' / 'no_guessed_states.csv')
FONT_COUNT=('Arial', 20, 'normal')


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.data_states = pandas.read_csv(PATH_OF_50_STATES_CSV)
        self.guess_state_list = []
        self.hideturtle()
        self.penup()

    def check_state(self, user_answer):
        user_answer = self.format_answer(user_answer)
        if len(self.data_states[self.data_states.state == user_answer]) == 1\
                and user_answer not in self.guess_state_list:
            self.guess_state_list.append(user_answer)
            return True
        return False

    def count_message(self):
        self.goto(158, 260)
        guess = len(self.guess_state_list)
        message = f'SCORE {guess}/50'
        self.write(message, font=FONT_COUNT)

    def format_answer(self, answer):
        return answer.title()

    def move_state_to_map(self, answer):
        answer = self.format_answer(answer)
        x = int(self.data_states[self.data_states.state == answer].x)
        y = int(self.data_states[self.data_states.state == answer].y)
        self.goto(x, y)
        self.write(answer, font=('Arial', 7, 'normal'))

    def saved_to_csv_all_state_no_guessed(self):
        state_no_guessed_list = []
        all_state_list = self.data_states.state.to_list()

        for state in all_state_list:
            if state not in self.guess_state_list:
                state_no_guessed_list.append(state)
        no_guessed_state_csv = pandas.DataFrame(state_no_guessed_list)
        no_guessed_state_csv.to_csv(PATH_OF_NO_GUESSED_STATE)

