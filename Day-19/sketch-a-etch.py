import turtle
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()


def turn_left():
    t.setheading(t.heading() + 10)


def turn_right():
    t.setheading(t.heading() - 10)


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def clear_screen():
    t.clear()
    t.pu()
    t.home()
    t.pd()


screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
