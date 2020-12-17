from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('red')
        self.shapesize(1.0, 1.0)
        self.random_move()

    def random_move(self):
        x = randint(-230, 230) 
        y = randint(-230, 230)
        self.goto(x, y)

    
