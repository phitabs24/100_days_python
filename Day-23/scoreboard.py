# Import necessary modules
from turtle import Turtle

# Define constants
FONT = ("Courier", 24, "normal")  # Font for scoreboard text
LEVEL_POSITION = (-260, 260)  # Position for level display

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle object
        self.pu()  # Pen up
        self.goto(LEVEL_POSITION)  # Move to level display position
        self.level = 1  # Initialize level to 1
        self.play_speed = 0.5  # Initialize play speed to 0.5
        self.write(f"Level: {self.level}", False, font=FONT)  # Display initial level

    def update_level(self):
        """Increase level and speed"""
        self.level += 1
        self.play_speed /= self.level
        self.clear()  # Clear previous level display
        self.write(f"Level: {self.level}", False, font=FONT)  # Display updated level

    def game_over(self):
        """Display game over message"""
        message = "Game Over"
        self.home()  # Move to home position
        self.write(message, False, 'center', font=FONT)  # Display game over message