from turtle import Turtle, Screen
import random
tortu = Turtle()
tortu.color('blue4')
list_color = ['red', 'blue', 'orange', 'grey', 'pink', 'yellow', 'green',
              'violet']
geometry = {
    'triangle': {'degree': 120, 'sides': 3},
    'squeare':  {'degree': 90, 'sides': 4},
    'pentagon': {'degree': 72, 'sides': 5},
    'hexagon':  {'degree': 60, 'sides': 6},
    'heptagon': {'degree': 51.62, 'sides': 7},
    'octagon':  {'degree': 45, 'sides': 8},
    'nonagon':  {'degree': 40, 'sides': 9},
    'decagon':  {'degree': 36, 'sides': 10}
    }

for shape in geometry:
    tortu.color(random.choice(list_color))
    for sides in range(geometry[shape]['sides']):
        tortu.backward(80)
        tortu.left(geometry[shape]['degree'])

screen = Screen()
screen.exitonclick()    
