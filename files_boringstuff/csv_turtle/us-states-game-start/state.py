import pandas
from pathlib import Path
from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        the_path = str(Path.cwd() / 'data' / '50_states.csv')
        self.data_states = pandas.read_csv(the_path)
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
        guess = len(self.guess_state_list)
        if guess == 0:
            message = 'U.S STATE GAME'
        else:
            message = f'GUESSED {guess}/50 U.S STATE GAME'
        return message

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
        the_path = str(Path.cwd() / 'data' / 'no_guessed_states.csv')

        for state in all_state_list:
            if state not in self.guess_state_list:
                state_no_guessed_list.append(state)
        no_guessed_state_csv = pandas.DataFrame(state_no_guessed_list)
        no_guessed_state_csv.to_csv(the_path)