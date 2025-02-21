from turtle import Screen
from batons import Batons
from pingball import Ball
from scoreboard import ScoreBoard
import time

from separation import Separation

screen = Screen()
screen.setup(width=1080, height=720)
screen.bgcolor('black')
screen.title("Ping Pong Game")
screen.tracer(0)
time.sleep(0.05)

separation = Separation()
scoreboard = ScoreBoard()
batons = Batons()
ball = Ball()

screen.listen()
screen.onkey(fun=batons.baton1_up, key="w")
screen.onkey(fun=batons.baton1_down, key="s")
screen.onkey(fun=batons.baton2_up, key="Up")
screen.onkey(fun=batons.baton2_down, key="Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.speed("fastest")
    ball.move()

    if ball.xcor() > 535 or ball.xcor() < -535:

        if ball.xcor() > 520:
            scoreboard.score1 += 1
        elif ball.xcor() < -520:
            scoreboard.score2 += 1
        scoreboard.update_score()
        ball.refresh()
    elif ball.ycor() > 340 or ball.ycor() < -340:
        ball.setheading(ball.heading() * -1)
    elif ball.distance(batons.baton1) < 20 or ball.distance(batons.baton2) < 20:
        ball.setheading(ball.heading() + 90)

screen.exitonclick()
