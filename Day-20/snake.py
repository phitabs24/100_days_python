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
        """Create a snake object with three segments.

        The snake object is a list of turtle objects, each of which
        represents a segment of the snake. The snake is initially
        positioned at the start of the game grid.

        The segments are added to the snake list in reverse order,
        with the head of the snake as the first element in the list.
        """
        for position in START_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        """Add a new segment to the snake.

        This method creates a new turtle object, sets its shape, color,
        and position, and adds it to the end of the snake list.

        :param position: The position of the new segment.
        :type position: tuple
        """
        new_segment = Turtle(shape='square')  # Create a new turtle object
        new_segment.pu()  # Pen up, so we don't draw lines when moving
        new_segment.color('white')  # Set the color of the new segment
        new_segment.setpos(position)  # Set the position of the new segment
        self.snake.append(new_segment)  # Add the new segment to the snake list

    def extend(self):
        """Add a new segment to the snake.

        This method adds a new segment to the snake by calling the
        add_segment method and passing the position of the last segment
        in the snake as the argument. The new segment is added to the
        end of the snake list.

        :return: None
        """
        # Add a new segment to the snake
        self.add_segment(self.snake[-1].position())

    def move(self):
        """Move the snake forward.

        This method moves the snake forward by one step size. The
        snake is moved by iterating over the segments in reverse
        order and setting the position of each segment to the
        previous segment's position. The head of the snake is moved
        forward by one step size.

        :return: None
        """
        # Iterate over the segments in reverse order
        for seg_num in range(len(self.snake) - 1, 0, -1):
            # Get the x and y coordinates of the previous segment
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()

            # Set the position of the current segment to the
            # previous segment's position
            self.snake[seg_num].setpos(new_x, new_y)

        # Move the head of the snake forward by one step size
        self.head.fd(STEP_SIZE)

    def up(self):
        """Turn the snake up.

        If the snake is currently heading down, this method does
        nothing. Otherwise, it sets the snake's heading to up.

        :return: None
        """
        if self.head.heading() != DOWN:
            # Set the snake's heading to up
            self.head.setheading(UP)

    def right(self):
        """Turn the snake right.

        If the snake is currently heading left, this method does
        nothing. Otherwise, it sets the snake's heading to right.

        :return: None
        """
        if self.head.heading() != LEFT:
            # Set the snake's heading to right
            self.head.setheading(RIGHT)

    def left(self):
        """Turn the snake left.

        If the snake is currently heading right, this method does
        nothing. Otherwise, it sets the snake's heading to left.

        :return: None
        """
        if self.head.heading() != RIGHT:
            # Set the snake's heading to left
            self.head.setheading(LEFT)

    def down(self):
        """Turn the snake down.

        If the snake is currently heading up, this method does
        nothing. Otherwise, it sets the snake's heading to down.

        :return: None
        """
        if self.head.heading() != UP:
            # Set the snake's heading to down
            self.head.setheading(DOWN)
