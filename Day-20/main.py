# Import necessary modules
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.bgcolor('black')  # Set background color
screen.title('Ultimate Snake Game')  # Set window title
screen.tracer(0)  # Turn off animation

# Create game objects
snake = Snake()  # Create a new snake object
food = Food()  # Create a new food object
scoreboard = ScoreBoard()  # Create a new scoreboard object

# Set up keyboard controls
screen.listen()  # Start listening for keyboard events
screen.onkey(fun=snake.up, key='Up')  # Bind up arrow key to snake.up method
screen.onkey(fun=snake.down, key='Down')  # Bind down arrow key to snake.down method
screen.onkey(fun=snake.left, key='Left')  # Bind left arrow key to snake.left method
screen.onkey(fun=snake.right, key='Right')  # Bind right arrow key to snake.right method

# Main game loop
game_is_on = True  # Flag to indicate whether game is running
while game_is_on:
    # Update screen
    screen.update()

    # Pause for a short time to control game speed
    time.sleep(0.2)

    # Move the snake
    snake.move()

    # Check for collision with food
    if snake.head.distance(food) < 15:
        # Refresh food position
        food.refresh()
        # Increment score
        scoreboard.score += 1
        # Update scoreboard
        scoreboard.update_score()
        # Extend snake length
        snake.extend()

    # Check for collision with walls
    if (snake.head.xcor() > 280 or
        snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or
        snake.head.ycor() < -280):
        # Game over
        # game_is_on = False
        # Display game over message
        scoreboard.reset()
        snake.reset()

    # Check for collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            # Game over
            # game_is_on = False
            # Display game over message
            scoreboard.reset()
            snake.reset()

# Exit game loop
screen.exitonclick()