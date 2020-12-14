from turtle import Turtle, Screen
import random


list_color = ['red', 'blue', 'orange', 'grey', 'pink', 'yellow', 'green',
              'violet']

orientation_list = [0, 90, 180, 270]

tim = Turtle()
last_orientation = 0
change_orientation = False
for movement in range(100):

    color = random.choice(list_color)
    tim.pen(pencolor=color, pensize=10, speed=1)
    current_orientation = random.choice(orientation_list)

    while not change_orientation:
        if current_orientation != last_orientation:
            last_orientation = current_orientation
            change_orientation = True
        else:
            current_orientation = random.choice(orientation_list)

    print(last_orientation)
    change_orientation = False
    tim.setheading(current_orientation)
    tim.forward(20)

screen = Screen()
screen.exitonclick()
