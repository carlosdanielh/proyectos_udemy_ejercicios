from turtle import Turtle

START_BODY_POSITION = [[0, 0], [-20, 0], [-40, 0]]
STEPS = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.snake_body = []
        self.activate = False
        for position in START_BODY_POSITION:
            body = Turtle('square')
            body.color('white')
            body.penup()
            body.goto(position)
            self.snake_body.append(body)

    def move(self):
        for number_of_body in range(len(self.snake_body) - 1, 0, - 1):
            new_x = self.snake_body[number_of_body - 1].xcor()
            new_y = self.snake_body[number_of_body - 1].ycor()
            self.snake_body[number_of_body].goto(new_x, new_y)

        self.snake_body[0].forward(STEPS)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)
            self.activate = True

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def pause(self):
        self.activate = False

    def continue_(self):
        self.activate = True

    def collide(self, food):
        if self.snake_body[0].distance(food) < 15:
            return True

    def grow(self, grow):

        self.snake_body[0].append()

