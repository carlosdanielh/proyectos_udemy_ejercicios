from turtle import Screen
from time import sleep
from snake_class import Snake
from Food import Food

screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)
screen.bgcolor('black')

snake = Snake()
food = Food()
# snake.move('right')

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
    print(snake.snake_body[0].distance(food))

    if snake.collide(food):
        food.random_move()



screen.mainloop()
