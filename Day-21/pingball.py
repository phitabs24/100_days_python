import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """
        Initialize the Ball object.

        This method calls the Turtle class's `__init__` method,
        sets the shape to "circle", sets the color to "white",
        picks up the pen, and sets the x and y move amounts.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.setheading(random.randint(0, 360))
        self.speed("fastest")
        self.move()

    def move(self):
        self.fd(10)