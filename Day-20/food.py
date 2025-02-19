from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Initializes a new instance of the Food class.

        The Food class is responsible for creating and managing the food
        that the snake is supposed to eat. The food is represented by a
        circle shape and is colored blue. The food is initially placed at
        a random location on the screen.
        """
        super().__init__()

        # Set the shape of the food to a circle
        self.food_y = None
        self.food_x = None
        self.shape('circle')

        # Make sure the food is not drawn on the screen
        self.pu()

        # Make the food smaller
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Set the color of the food to blue
        self.color("blue")

        # Make sure the food moves quickly
        self.speed("fastest")

        # Place the food at a random location on the screen
        self.refresh()


    def refresh(self):
        """Places the food at a new random location on the screen.

        The food is placed at a random location within the screen
        boundaries. The x and y coordinates are randomly selected
        within the range of -280 to 280.
        """
        # Generate a new random x and y coordinate within the screen boundaries
        self.food_x = random.randint(-280, 280)
        self.food_y = random.randint(-280, 280)

        # Move the food to the new location
        self.goto(self.food_x, self.food_y)