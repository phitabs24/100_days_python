import random

import colorgram as cg

from turtle import Turtle, Screen, colormode

t = Turtle()

# colors = cg.extract('image.jpg', 25)

rgb_colors = [(237, 233, 228), (241, 146, 64), (24, 113, 164), (168, 7, 34), (104, 176, 211), (236, 83, 40),
              (190, 175, 9), (165, 49, 93), (242, 226, 236), (205, 227, 238), (8, 172, 213), (42, 23, 16),
              (23, 133, 65), (64, 14, 31), (234, 244, 239), (223, 204, 103), (193, 63, 31), (22, 33, 71),
              (212, 56, 116), (1, 114, 86), (8, 50, 34), (61, 166, 92), (130, 215, 231), (101, 185, 146),
              (207, 124, 174)]

t.speed(100)
colormode(255)

# for coloring in colors:
#
#     r = coloring.rgb.r
#     g = coloring.rgb.g
#     b = coloring.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

t.pu()
t.setpos(-225, -225)

def paint():
    t.dot(20)
    t.fd(50)
# print(rgb_colors)
for _ in range(100):
    t.color(random.choice(rgb_colors))
    if t.xcor() > 255:
        t.setx(-225)
        t.sety(t.ycor() + 50)
    paint()

screen = Screen()
screen.exitonclick()
