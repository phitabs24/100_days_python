from turtle import Turtle


class Separation:

    def __init__(self):
        """Initializes the Separation object.

        This method sets up the separation object by initializing the turtle,
        setting the x and y coordinates, and calling the make_separation method.
        """
        self.t = None
        # Set the x coordinate to the middle of the screen
        self.x_cor = 0
        # Set the y coordinate to the bottom of the screen, offset by 20 pixels
        self.y_cor = - (720 / 2) + 20
        self.make_separation()

    def make_separation(self):
        """Creates a separation line using turtle graphics.

        This method initializes turtles as squares and places them along the
        y-axis to create a separation line. The turtles are positioned with
        specific spacing and do not draw lines when moving.
        """
        while self.y_cor < 340:
            self.t = Turtle("square")  # Create a turtle object shaped as a square
            self.t.color("white")  # Set the turtle's color to white
            self.t.shapesize(stretch_wid=2, stretch_len=0.25)  # Adjust the size of the turtle
            self.t.pu()  # Pen up: don't draw lines when moving
            self.t.speed("fastest")  # Set the turtle's speed to the fastest
            self.t.goto(self.x_cor, self.y_cor)  # Position the turtle at the current coordinates
            self.y_cor += 75  # Move to the next position along the y-axis