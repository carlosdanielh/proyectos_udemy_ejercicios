from turtle import Turtle, Screen
import random


def pen_all_turtle_down(list_turtles):
    for turtle in list_turtles:
        turtle.up()


def move_all_turtle_to_the_start_point(start_point_y, list_turtles):
    index = 0
    for turtle in list_turtles:  
        turtle.color(ranbow_colors[index])
        turtle.goto(-390, start_point_y)
        start_point_y += 66
        index += 1


ranbow_colors = ['yellow', 'red', 'orange', 'violet', 'blue', 'pink']


screen = Screen()
screen.setup(800, 400)


tim = Turtle('turtle')
jason = Turtle('turtle')
marly = Turtle('turtle')
pluton = Turtle('turtle')
wasock = Turtle('turtle')
pepe = Turtle('turtle')

list_turtles = [tim, jason, marly, pluton, wasock, pepe]


pen_all_turtle_down(list_turtles)
start_point_y = -160
move_all_turtle_to_the_start_point(start_point_y, list_turtles)
screen.mainloop()