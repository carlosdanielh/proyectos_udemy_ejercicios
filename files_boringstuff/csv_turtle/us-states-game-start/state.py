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
        self.x = 0
        self.y = 0
        self.hideturtle()

    def check_state(self, user_answer):
        user_answer = user_answer.lower().title()

        if len(self.data_states[self.data_states.state == user_answer]) == 1\
                and user_answer not in self.guess_state_list:
            self.guess_state_list.append(user_answer)
            self.guess += 1
            return True
        return False

    def get_coordinate(self, user_answer):
        # import pdb; pdb.set_trace()
        self.x = self.data_states[self.data_states.state == user_answer].x
        self.y = self.data_states[self.data_states.state == user_answer].y
        return [self.x.to_list(), self.y.to_list()]

    def guess_message(self):
        if self.guess == 0:
            message = 'U.S STATE GAME'
        else:
            message = f'GUESSED {self.guess}/50 U.S STATE GAME'
        return message

    def move_state_to_coordinate(self, answer):
        
        position = self.get_coordinate(answer.lower().title())
        new_x = position[0][0]
        new_y = position[1][0]
        self.goto(new_x, new_y)
        # import pdb; pdb.set_trace()
        print(new_x)
        print(new_y)
        self.clear()
        self.write(answer.lower().title(), font=('Arial', 5, 'normal'))
        
