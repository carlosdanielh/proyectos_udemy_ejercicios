#! python 5
'''
w = foward
s = backward
a = counter-clockwise
d = clockwise
c = clear drawing
'''
from turtle import Turtle


def foward():
    tim.forward(5)


def backward():
    tim.backward(5)


def counter_clock():
    tim.left(5)


def clock():
    tim.right(5)


def clear():
    tim.screen.resetscreen()


tim = Turtle()
tim.screen.listen()
tim.screen.onkeypress(foward, 'w')
tim.screen.onkeypress(backward, 's')
tim.screen.onkeypress(counter_clock, 'a')
tim.screen.onkeypress(clock, 'd')
tim.screen.onkeypress(clear, 'c')
tim.screen.listen()

tim.screen.exitonclick()





