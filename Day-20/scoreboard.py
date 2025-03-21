from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        """Initializes a new ScoreBoard instance.

        This constructor sets up the scoreboard by initializing the score
        to zero, positioning the turtle, and updating the score display.
        """
        super().__init__()  # Call the parent class (Turtle) constructor
        self.pu()  # Pen up; do not draw lines when moving
        self.hideturtle()  # Hide the turtle shape
        self.color("white")  # Set the text color to white
        self.sety(260)  # Position the scoreboard near the top of the screen
        self.score = 0  # Initialize the score to zero
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())  # Read the high score from a file
        self.update_score()  # Display the initial score

    # def game_over(self):
    #     """Displays the game over message on the scoreboard.
    #
    #     This method moves the scoreboard to the home position (center of the
    #     screen) and writes the game over message. The message is written in the
    #     middle of the screen with the font Arial, size 16, in normal style.
    #     """
    #     # Move the scoreboard to the home position (center of the screen)
    #     self.home()
    #     # Write the game over message
    #     self.write("GAME OVER.", move=False, align=ALIGNMENT, font=FONT)


    def reset(self):
        """Checks for new high score and Resets the score to zero and updates the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        """Updates the scoreboard with the current score and high score.

        This method clears the previous scoreboard and writes the current
        score and high score to the scoreboard. The score is formatted as "Score: <current
        score>" and is written in the middle of the screen with the font
        Arial, size 16, in normal style.
        """
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)



