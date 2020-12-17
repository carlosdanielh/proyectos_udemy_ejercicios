from turtle import Screen
from time import sleep
from snake_class import Snake


screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)
screen.bgcolor('black')

snake = Snake()
# snake.move('right')

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')

game_over = False
while not game_over:
    screen.update()
    sleep(0.1)
    snake.move()

screen.mainloop()
