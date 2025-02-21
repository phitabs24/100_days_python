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
        # Set the shape of the turtle to a circle
        self.shape("circle")

        # Set the color of the turtle to white
        self.color("white")

        # Pen up to avoid drawing lines
        self.penup()

        # Set the speed of the turtle to fastest
        self.speed("fastest")

        # Initialize the x and y move amounts
        # self.x_move = 10
        # self.y_move = 10

        # Refresh the ball's position and move it
        self.refresh()
        self.move()

    def refresh(self):
        """
        Resets the ball's position to the center and sets a random heading.

        This method moves the ball to the home position (center of the screen)
        and sets its heading to a random angle between 0 and 360 degrees.
        """
        # Move the ball to the home position (center of the screen)
        self.home()

        # Set the ball's heading to a random angle between 0 and 360 degrees
        self.setheading(random.randint(0, 360))

    def move(self):
        """
        Moves the ball forward.

        This method moves the ball forward by a fixed distance.
        """
        # Move the ball forward by 10 units
        self.fd(10)