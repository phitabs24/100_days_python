
from turtle import Turtle, Screen

def snake(self):
    for _ in range(3):
        t = Turtle(shape='square')
        t.pu()
        t.color('white')
        t.setpos(self.xcor, 0)
        self.snake.append(t)
        self.xcor -= 20
    return self.snake