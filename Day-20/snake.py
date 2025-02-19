from turtle import Turtle

RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

START_POSITION = [(0,0), (-20,0), (-40,0)]

TURTLE_SIZE = 20
STEP_SIZE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.make_snake()
        self.head = self.snake[0]

    def make_snake(self):
        for position in START_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.pu()
        new_segment.color('white')
        new_segment.setpos(position)
        self.snake.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].setpos(new_x, new_y)
        self.head.fd(STEP_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
