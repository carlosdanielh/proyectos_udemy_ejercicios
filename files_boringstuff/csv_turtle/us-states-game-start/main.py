import os
from pathlib import Path
from turtle import Screen, Turtle
from state import State

FONT_YOU_WON = ('Arial', 24, 'normal', 'bold')
PATH_OF_IMAGE = str(Path.cwd() / 'udemy_projects' / 'files_boringstuff' /
                    'csv_turtle' / 'us-states-game-start' /
                    'blank_states_img.gif'
                    )

os.system('cls')
windows = Screen()
windows.title('USA STATE')
windows.tracer(0)
windows.setup(740, 540)
turtle = Turtle()
windows.addshape(PATH_OF_IMAGE)
turtle.shape(PATH_OF_IMAGE)
windows.update()
state = State()

want_to_exit = False
while not want_to_exit:
    answer_state = windows.textinput(title=state.count_message(),
                                     prompt='Whats the other state\'s name '
                                     '(type nothing to exit)'
                                     )

    if len(answer_state) == 0:
        want_to_exit = True
        state.saved_to_csv_all_state_no_guessed()
    elif state.check_state(answer_state):
        state.move_state_to_map(answer_state)

    if len(state.guess_state_list) == 50:
        turtle.goto(-100, 0)
        turtle.color('red')
        turtle.write('YOU WON!! THANK YOU FOR GAME', FONT_YOU_WON)


windows.mainloop()
