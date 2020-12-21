from turtle import Screen
from player import Player
from score import Score


screen = Screen()
screen.tracer(0)
screen.setup(600, 600)

score = Score()
screen.update()

screen.tracer(1)
turtle = Player()
screen.listen()
screen.onkeypress(turtle.up, 'Up')
screen.onkeypress(turtle.down, 'Down')

if turtle.over_pass_top_screen:
    print('entro')
    score.set_point()
    turtle.start_position()

screen.update()

# game_over = False
# while not game_over:

screen.mainloop()
