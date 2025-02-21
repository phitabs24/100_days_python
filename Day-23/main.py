import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(scoreboard.play_speed)
    screen.update()
    cars.create_car()
    cars.move_car()
    if player.ycor() > 280.0:
        scoreboard.update_level()
        player.refresh()

    for a in cars.all_cars:
        if player.distance(a) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
