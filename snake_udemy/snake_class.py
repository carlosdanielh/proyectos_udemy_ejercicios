from turtle import Turtle

START_BODY_POSITION = [[0, 0], [-20, 0], [-40, 0]]
STEPS = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
RIGHT_WALL = 250
LEFT_WALL = -250
UP_WALL = 250
DOWN_WALL = -250


class Snake():

    def __init__(self):
        self.snake_body = []
        self.activate = False
        for position in START_BODY_POSITION:
            self.add_part_of_body(position)

    def add_part_of_body(self, position):
        body = Turtle('square')
        body.color('white')
        body.penup()
        body.goto(position)
        self.snake_body.append(body)

    def grow(self):
        self.add_part_of_body(self.snake_body[-1].position())

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

    def collide(self, something):
        if type(something) != list:
            if self.snake_body[0].distance(something) < 15:
                return True
        else:            
            for index in range(len(something)):
                if index < len(something)-1:
                    if self.snake_body[0].position() == something[index + 1].position():
                        print('perdiste')
                        return True

    def touch_border(self):
        if self.snake_body[0].xcor() >= RIGHT_WALL or\
               self.snake_body[0].xcor() <= LEFT_WALL or\
               self.snake_body[0].ycor() >= UP_WALL or\
               self.snake_body[0].ycor() <= DOWN_WALL:
            return True
        return False

    
    

