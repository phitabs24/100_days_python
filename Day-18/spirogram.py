import random

from turtle import Turtle, Screen, colormode

t = Turtle()
colormode(255)
# t.pu()
# t.setpos(-100, 350)
# t.pd()
# n = 1000

# color_list = ["CadetBlue",
# "CadetBlue1",
# "CadetBlue2",
# "CadetBlue3",
# "CadetBlue4",
# "chartreuse",
# "chartreuse1",
# "chartreuse2",
# "chartreuse3",
# "chartreuse4",
# "chocolate",
# "chocolate1",
# "chocolate2",
# "NavajoWhite4",
# "navy",
# "NavyBlue",
# "OldLace",
# "OliveDrab",
# "OliveDrab1",
# "OliveDrab2",
# "OliveDrab3",
# "OliveDrab4",
# "orange",
# "orange1",
# "orange2",
# "orange3",
# "orange4",
# "OrangeRed",
# "OrangeRed1",
# "OrangeRed2",
# "OrangeRed3",
# "OrangeRed4",
# "orchid"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# while n < len(color_list):
#     color = random.choice(color_list)
#     t.color(color)
#     angle = 360 / n
#     for _ in range(n):
#         t.forward(100)
#         t.rt(angle)
#     n += 1


directions = [0, 90, 270, 180]
t.speed(10)
# t.pensize(20)

# for _ in range(n):
#     t.pencolor(random_color())
#     t.setheading(random.choice(directions))
#     t.forward(30)

n = 0
for _ in range(36):
    t.pencolor(random_color())
    t.setheading(n)
    t.circle(120)
    n += 10





my_screen = Screen()
my_screen.exitonclick()