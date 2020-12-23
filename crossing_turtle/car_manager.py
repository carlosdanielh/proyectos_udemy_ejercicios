from turtle import Turtle
import random


colors = ['red', 'violet', 'brown', 'blue', 'orange', 'green', 'black',
          'brown', 'purple', 'fuchsia', 'navy']

MAX_CAR = 30


class Cars():
    def __init__(self):
        self.list_car = []
        for _ in range(MAX_CAR):
            self.new_car = Turtle()
            self.new_car.setheading(180)
            self.new_car.color(random.choice(colors))
            self.new_car.shape('square')
            self.new_car.shapesize(1, 2)
            self.new_car.penup()
            self.new_car.goto(self.new_x(), self.new_y())
            self.list_car.append(self.new_car)
        self.speed_move = 5
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
        self.speed_move += 5

    def run_into(self, turtle):
        for car in self.list_car:
            if turtle.distance(car) <= 27:
                print(turtle.distance(car))
                print(car.ycor())
                print(car.color())
                return True
        return False
