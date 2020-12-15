from turtle import Turtle
import random

# ##################################FUNCTIONS##################################
def start_point(START_Y_POSITION):
    tim.speed(0)    
    tim.setpos(-300, START_Y_POSITION)


def leave_a_dot():
    tim.screen.colormode(255)
    tim.dot(20, random.choice(list_color))


def move_foward():    
    tim.forward(50)
# ##############################END FUNCTIONS##################################


list_color = [(46, 33, 27), (208, 170, 115), (235, 202, 218), (177, 96, 48),
              (223, 231, 226)]

START_Y_POSITION = -250
UP_Y_POSITION = 50
tim = Turtle()
tim.up()

start_point(START_Y_POSITION)
leave_a_dot()

for y in range(10):    
    for x in range(9):
        leave_a_dot()
        move_foward()
    START_Y_POSITION += UP_Y_POSITION
    start_point(START_Y_POSITION)

tim.hideturtle()
tim.screen.exitonclick()
