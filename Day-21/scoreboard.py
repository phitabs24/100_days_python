from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        """Initializes a new ScoreBoard instance.

        This constructor sets up the scoreboard by initializing the scores
        for both players to zero, positioning the turtle for display, and
        updating the score display on the screen.
        """
        super().__init__()  # Call the parent class (Turtle) constructor
        self.pu()  # Pen up; the turtle will not draw lines while moving
        self.hideturtle()  # Hide the turtle shape to focus on text display
        self.color("white")  # Set the text color to white for visibility
        self.sety(320)  # Position the scoreboard near the top of the screen
        self.score1 = 0  # Initialize the score of player 1 to zero
        self.score2 = 0  # Initialize the score of player 2 to zero
        self.update_score()  # Display the initial score on the screen

    def game_over(self):
        """Displays the game over message on the scoreboard.

        This method moves the scoreboard to the home position (center of the
        screen) and writes the game over message. The message is written in the
        middle of the screen with the font Arial, size 16, in normal style.
        """
        # Move the scoreboard to the home position (center of the screen)
        self.home()

        # Write the game over message
        message = "GAME OVER."
        self.write(message, move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        """Updates the scoreboard with the current scores of both players.

        This method clears the previous scoreboard display and writes the
        updated scores for player 1 and player 2. The scores are displayed
        in the format "<score1>      <score2>", centered on the screen using
        the specified font settings.
        """
        # Clear the previous score display from the screen
        self.clear()

        # Write the current scores of both players on the screen
        # The scores are centered using the ALIGNMENT and displayed with the FONT
        self.write(f"{self.score1}      {self.score2}", move=False, align=ALIGNMENT, font=FONT)



