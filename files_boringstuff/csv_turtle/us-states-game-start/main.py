import os
from pathlib import Path
from turtle import Screen, Turtle

from state import State

os.system('cls')
windows = Screen()
windows.tracer(0)
windows.setup(740, 540)
turtle = Turtle()
windows.title = ('U.S State')
image = str(Path.cwd() / 'udemy_projects' / 'files_boringstuff' /
            'csv_turtle' / 'us-states-game-start' /
            'blank_states_img.gif'
            )
windows.addshape(image)
turtle.shape(image)
windows.update()
state = State()
want_to_exit = False
while not want_to_exit:
    answer_state = windows.textinput(title=state.guess_message(),
                                     prompt='Whats the other state\'s name '
                                     '(blank input to exit)'
                                     )

    if len(answer_state) == 0:
        want_to_exit = True
    elif state.check_state(answer_state):
        state.move_state_to_map(answer_state)

windows.bye()
windows.mainloop()
