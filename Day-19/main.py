import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
n = 0

for color in colors:
    t = Turtle(shape='turtle')
    t.color(colors[n])
    turtles.append(t)
    n += 1

startx = -235
starty = -146

for turtle in turtles:
    turtle.pu()
    turtle.goto(x=startx, y=starty)
    starty += 60

def check_winner():
    if turtle.xcor() > 240:
        winner = turtle.fillcolor()
        if winner == user_bet.lower():
            return f"You win! The winner is {winner}"
        else:
            return f"You lose! The winner is {winner}"

def game_on():
    if turtle.xcor() > 240:
        return False
    else:
        return True

is_game_on = True

while is_game_on:
    for turtle in turtles:
        turtle.speed("fast")
        turtle.forward(random.randint(1, 10))
        is_game_on = game_on()
        if not is_game_on:
            print(check_winner())
            break

screen.exitonclick()
