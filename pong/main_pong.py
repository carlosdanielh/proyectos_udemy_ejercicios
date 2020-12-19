from turtle import Screen
from table_pong import Table
from time import sleep
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
sleep(0.001)
screen.tracer(1)

screen.listen()
screen.onkeypress(table_right.up, 'Up')
screen.onkeypress(table_right.down, 'Down')

screen.onkeypress(table_left.up, 'w')
screen.onkeypress(table_left.down, 's')
screen.update()
screen.mainloop()
