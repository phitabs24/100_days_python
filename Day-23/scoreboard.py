from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-260, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(LEVEL_POSITION)
        self.level = 1
        self.play_speed = 0.5
        self.write(f"Level: {self.level}", False, font=FONT)


    def update_level(self):
        self.level += 1
        self.play_speed /= self.level
        self.clear()

    def game_over(self):
        message = "Game Over"
        self.home()
        self.write(message, False, 'center', font=FONT)


