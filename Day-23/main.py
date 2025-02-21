# Import necessary modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off animation

# Create game objects
cars = CarManager()  # Manage cars on the screen
player = Player()  # Player's turtle object
scoreboard = Scoreboard()  # Display score and level

# Set up keyboard listener
screen.listen()
screen.onkey(player.move, "Up")  # Move player up on 'Up' key press

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(scoreboard.play_speed)  # Pause for a short duration
    screen.update()  # Update the screen
    cars.create_car()  # Create new cars
    cars.move_car()  # Move existing cars

    # Check if player reached the finish line
    if player.ycor() > 280.0:
        scoreboard.update_level()  # Increase level and speed
        player.refresh()  # Reset player position

    # Check for collisions with cars
    for car in cars.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()  # Display game over message
            game_is_on = False  # Exit game loop

# Exit on click
screen.exitonclick()