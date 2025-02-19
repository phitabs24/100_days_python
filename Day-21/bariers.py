from turtle import Turtle

START_POSITION = [(-280, 0), (280, 0)]
class Barier(Turtle):
    def __init__(self):
        super().__init__()

        self.barriers = []
        self.right_barrier = []
        self.penup()
        self.make_barriers()
        self.make_separations()
        # self.goto(position)

    def make_barriers(self):
        for position in START_POSITION:
            # self.add_segment(position)
            self.barrier = Turtle(shape='square')
            self.barrier.pu()
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()

            barrier.color('white')
            barrier.setpos(position)
            self.barriers.append(barrier)

    def make_separations(self):
        while self.y_cor < 340:
            self.divider = Turtle()
            self.divider.color("white")
            self.divider.shapesize(stretch_wid=10, stretch_len=30)
            self.divider.pu()
            self.divider.goto(self.x_cor, self.y_cor)
            self.y_cor += 30



