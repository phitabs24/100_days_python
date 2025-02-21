from turtle import Turtle

START_POSITION = [(-520, 0), (520, 0)]
UP , DOWN = 90, 270
MOVE_DISTANCE = 20

class Batons(Turtle):
    def __init__(self):
        """Initializes the batons object.

        This constructor initializes the batons object by creating the batons,
        setting their positions, and setting the variables that will be used by
        the other methods.
        """
        super().__init__()

        # The baton object
        self.baton = None

        # The x and y coordinates of the baton
        self.x_cor = None
        self.y_cor = None

        # The divider object
        self.divider = None

        # The list of batons
        self.batons = []

        # The baton objects
        self.baton1 = None
        self.baton2 = None

        # Create the batons
        self.make_batons()

        # Set the baton1 and baton2 variables
        self.baton1 = self.batons[0]
        self.baton2 = self.batons[1]

        # self.goto(position)

    def make_batons(self):
        """Creates the batons for the game.

        This method creates the batons for the game by iterating over the
        START_POSITION list and creating a new baton object for each position.
        The baton object is set up with the correct shape, color, and size,
        and is moved to the correct position.

        Returns:
            None
        """
        for position in START_POSITION:
            # self.add_segment(position)
            self.baton = Turtle(shape='square')
            self.baton.pu()
            self.baton.shapesize(stretch_wid=3, stretch_len=0.6)
            self.baton.penup()
            self.baton.color('white')
            self.baton.setpos(position)
            self.batons.append(self.baton)

    def baton1_up(self):
        self.baton1.sety(self.baton1.ycor() + MOVE_DISTANCE)


    def baton1_down(self):
        """Moves the baton1 down.

        This method moves the baton1 down by subtracting the MOVE_DISTANCE
        from the y-coordinate of the baton1.
        """
        self.baton1.sety(self.baton1.ycor() - MOVE_DISTANCE)

    def baton2_up(self):
        """Moves the baton2 up.

        This method moves the baton2 up by adding the MOVE_DISTANCE
        to the y-coordinate of the baton2.
        """
        self.baton2.sety(self.baton2.ycor() + MOVE_DISTANCE)

    def baton2_down(self):
        """Moves the baton2 down.

        This method moves the baton2 down by subtracting the MOVE_DISTANCE
        from the y-coordinate of the baton2.
        """
        self.baton2.sety(self.baton2.ycor() - MOVE_DISTANCE)

