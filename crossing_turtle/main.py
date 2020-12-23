from turtle import Screen
from player import Player
from score import Score
from time import sleep
from car_manager import Cars


screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
cars = Cars()
score = Score()
turtle = Player()
screen.update()

screen.listen()
screen.onkeypress(turtle.up, 'Up')
screen.onkeypress(turtle.down, 'Down')

game_over = False
while not game_over:
    cars.move()
    screen.update()

    if turtle.over_pass_top_screen():
        score.set_point()
        turtle.start_position()
        cars.level_up_speed()
    elif cars.run_into(turtle):
        score.game_over_msg()
        game_over = True

    if cars.over_pass_left_screen():
        cars.start_new_position_right()

    sleep(0.1)
screen.mainloop()
