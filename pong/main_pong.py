from turtle import Screen
from table_pong import Table
from time import sleep
from ball import Ball
WIDTH = 800
HEIGHT = 600


screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title('pong game')

table_right = Table()
table_right.draw_paddle_right()

table_left = Table()
table_left.draw_paddle_left()

screen.update()
# sleep(0.01)
screen.tracer(1)

screen.listen()
screen.onkeypress(table_right.up, 'Up')
screen.onkeypress(table_right.down, 'Down')
screen.onkeypress(table_left.up, 'w')
screen.onkeypress(table_left.down, 's')
screen.update()

ball = Ball()
game_over = False
while not game_over:
    sleep(0.01)
    ball.move()

    if ball.collide():
        print('touch top')
        game_over = True

screen.mainloop()
