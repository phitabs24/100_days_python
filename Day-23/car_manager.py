from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    """
    Manage the creation and movement of cars in the game.
    """

    def __init__(self):
        """
        Initialize the CarManager object.

        This method creates a hidden turtle and initializes the car speed
        and turtle speed. It also creates the first car and moves it.
        """
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.turtle_speed = MOVE_INCREMENT
        self.create_car()
        self.move_car()


    def create_car(self):
        """
        Create a new car with a random chance and add it to the list of cars.

        This method generates a new car with a 1 in 6 chance each time it's called.
        The car is a turtle object with a random color and position.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Create a new turtle object shaped like a square
            new_car = Turtle("square")
            # Set the size of the car
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # Assign a random color to the car
            new_car.color(random.choice(COLORS))
            # Lift the pen to avoid drawing
            new_car.penup()
            # Set a random y-coordinate for the car's starting position
            random_y = random.randint(-250, 250)
            # Position the car at the right edge of the screen
            new_car.goto(300, random_y)
            # Add the new car to the list of all cars
            self.all_cars.append(new_car)

    def move_car(self):
        for a in self.all_cars:
            a.backward(self.car_speed)
            if a.xcor() < -300:
                self.all_cars.remove(a)

    def level_up(self):
        """
        Increase the speed of all cars.

        This method adds the value of the turtle speed to the current car speed.
        """
        self.car_speed += self.turtle_speed
