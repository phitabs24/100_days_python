from turtle import Screen
from bariers import Barier
from  pingball import Ball
import time

from separation import Separation


separation = Separation()
# time.sleep(0.1)
ball = Ball()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Ping Pong Game")
# screen.tracer(0)
# screen.listen()
# screen.onkey(fun=ball.move(), key="space")

game_on = True

while game_on:
    screen.update()
    # time.sleep(0.1)

    ball.move()
screen.exitonclick()