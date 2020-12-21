from turtle import Screen
from table_pong import Table
from time import sleep
from ball import Ball
from score_pong import Score
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

score = Score()
score.points_message()

paint_circle = Score()
paint_circle.pendown()
paint_circle.shape('circle')
paint_circle.color('red')
paint_circle.shapesize(3, 3)

paint_line = Score()
paint_line.pendown()
paint_line.color('red')
paint_line.goto(0, -300)
paint_line.setheading(90)
paint_line.forward(700)

screen.update()
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
    screen.update()
    sleep(0.01)
    ball.move()

    if ball.collide(screen):
        ball.bounce_walls()

    if ball.collide(table_right) or ball.collide(table_left):
        ball.bounce_tables()

    if ball.touch_empty_space():
        screen.tracer(0)

        if ball.xcor() >= 380:
            score.set_points('a')
        elif ball.xcor() <= -380:
            score.set_points('b')
        ball.start_game_again()

        screen.update()
screen.mainloop()
