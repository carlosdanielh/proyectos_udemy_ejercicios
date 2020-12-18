from turtle import Screen
from time import sleep
from snake_class import Snake
from Food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)
screen.bgcolor('black')

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.pause, 'space')
screen.onkeypress(snake.continue_, 'c')


game_over = False
while not game_over:
    screen.update()
    sleep(0.1)

    if snake.activate:
        snake.move()

    if snake.collide(food):
        food.random_move()
        score.add_point()
        snake.grow()

    if snake.touch_border():
        score.game_over_message()
        game_over = True


screen.mainloop()
