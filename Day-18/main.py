import random
from turtle import Turtle, Screen

t = Turtle()
# t.pu()
# t.setpos(-100, 350)
# t.pd()
n = 1000

color_list = ["CadetBlue",
"CadetBlue1",
"CadetBlue2",
"CadetBlue3",
"CadetBlue4",
"chartreuse",
"chartreuse1",
"chartreuse2",
"chartreuse3",
"chartreuse4",
"chocolate",
"chocolate1",
"chocolate2", "NavajoWhite4",
"navy",
"NavyBlue",
"OldLace",
"OliveDrab",
"OliveDrab1",
"OliveDrab2",
"OliveDrab3",
"OliveDrab4",
"orange",
"orange1",
"orange2",
"orange3",
"orange4",
"OrangeRed",
"OrangeRed1",
"OrangeRed2",
"OrangeRed3",
"OrangeRed4",
"orchid"]

# while n < len(color_list):
#     color = random.choice(color_list)
#     t.color(color)
#     angle = 360 / n
#     for _ in range(n):
#         t.forward(100)
#         t.rt(angle)
#     n += 1

def west():
    t.setheading(180)

def east():
    t.setheading(0)

def north():
    t.setheading(90)

def south():
    t.setheading(270)

directions = [0, 90, 270, 180]
t.speed(10)
t.pensize(20)

for _ in range(n):
    t.pencolor(random.choice(color_list))
    t.setheading(random.choice(directions))
    t.forward(25)








my_screen = Screen()
my_screen.exitonclick()