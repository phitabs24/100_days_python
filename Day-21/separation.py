from turtle import Turtle


class Separation:

    def __init__(self):
        self.t = None
        self.x_cor = 0
        self.y_cor = - (720 / 2) + 20
        self.make_separation()

    def make_separation(self):

        while self.y_cor < 340:
            self.t = Turtle("square")
            self.t.color("white")
            self.t.shapesize(stretch_wid=2, stretch_len=0.25)
            self.t.pu()
            self.t.goto(self.x_cor, self.y_cor)
            self.y_cor += 75