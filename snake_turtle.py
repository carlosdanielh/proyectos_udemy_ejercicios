from turtle import Turtle, Screen
from time import sleep

def move(key_pressed):
    global move_x
    global move_y
    game_over = False
    # screen.tracer(1, 20)
    while not game_over:
        
        while True:           

            if key_pressed == 'right':
                move_x += 20
                move_y = 0
            elif key_pressed == 'up':
                move_x = 0
                move_y += 20
            elif key_pressed == 'left':
                move_y = 0
                move_x -= 20
            elif key_pressed == 'down':
                move_x = 0
                move_y -= 20

            screen.tracer(1)
            for index, body in enumerate((body_snake)):
                x = list_position[index][0] + move_x
                y = list_position[index][1] + move_y
                print(f' x {x}')
                print(f' y {y}')
                body.goto(x, y)
            print('-----------')
            # import pdb; pdb.set_trace()
            screen.update()
            move_y = 0
            move_x = 0
            sleep(1)
            


def right():
    move('right')


def up():
    move('up')


def down():
    move('down')


def left():
    move('left')


move_x = 0
move_y = 0
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
list_position = [(20, 0), (40, 0), (60, 0)]
body_snake = []
screen.tracer(0)
for position in list_position:

    snake = Turtle()

    snake.up()
    snake.shape('square')
    snake.color('white')
    snake.goto(position)
    body_snake.append(snake)

screen.update()
screen.tracer(1, 20)
screen.listen()
screen.onkeypress(up, 'Up')
screen.onkeypress(down, 'Down')
screen.onkeypress(right, 'Right')
screen.onkeypress(left, 'Left')

screen.mainloop()
