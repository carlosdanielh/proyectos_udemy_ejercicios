from turtle import Turtle
import random


colors = ['red', 'violet', 'brown', 'blue', 'orange', 'green', 'black',
          'brown', 'purple', 'fuchsia', 'navy']

MAX_CAR = 30
STEPS = 5


class Cars():
    def __init__(self):
        self.list_car = []
        for _ in range(MAX_CAR):
            new_car = Turtle()
            new_car.setheading(180)
            new_car.color(random.choice(colors))
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(self.new_x(), self.new_y())
            self.list_car.append(new_car)
        self.speed_move = STEPS
        self.move()

    def new_y(self):
        new_y = random.randint(-240, 240)
        return new_y

    def new_x(self):
        new_x = random.randint(-320, 400)
        return new_x

    def over_pass_left_screen(self):
        for car in self.list_car:
            if car.xcor() < -310:
                self.start_new_position_right(car)

    def start_new_position_right(self, car):
        car.screen.tracer(0)
        x = random.randint(320, 340)
        car.goto(x, self.new_y())

    def move(self):
        for car in self.list_car:
            car.forward(self.speed_move)

    def level_up_speed(self):
        self.speed_move += STEPS

    def run_into(self, turtle):
        for car in self.list_car:
            if turtle.distance(car) <= 27:
                return True
        return False
