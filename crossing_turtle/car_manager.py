from turtle import Turtle
import random


colors = ['red', 'violet', 'brown', 'blue', 'orange', 'green', 'yellow',
          'pink', 'purple', 'fuchsia', 'navy']


class Cars:
    def __init__(self):
        self.list_car = []
        # for _ in range(60):
        self.new_car = Turtle()
        self.new_car.setheading(180)
        self.new_car.color(random.choice(colors))
        self.new_car.shape('square')
        self.new_car.shapesize(1, 2)
        self.new_car.penup()
        self.new_car.goto(self.new_y(), self.new_x())
        self.move()

    def new_y(self):
        new_y = random.randint(-280, 280)
        return new_y

    def new_x(self):
        new_x = random.randint(-320, 400)
        return new_x

    def over_pass_left_screen(self):
        if self.new_car.xcor() > -300:
            self.start_new_position()

    def start_new_position_right(self):
        x = random.randint(320, 340)
        self.goto(x, self.new_y())

    def move(self):
        self.new_car.goto(self.new_car.xcor() - 5, self.new_car.ycor())

    def run_into(self, turtle):
        if self.new_car.distance(turtle) < 35:
            return True
        return False
