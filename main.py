import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard,Over

player=Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
all_cars = CarManager()
score=Scoreboard()
over=Over()

sleep_time=0.5
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    screen.title("Ugur's Turtle Road Crossing Game")
    screen.listen()
    screen.onkey(player.move,"Up")
    all_cars.create_car()
    all_cars.car_move()
    # Car crash
    for car in all_cars.cars:
        if car.distance(player) < 25:
            game_is_on = False
            over.game_over()
            screen.listen()

            print("Crash")

    # Crossing road
    if player.ycor()>200:
        print("player.ycor() == 160", {player.ycor() == 10})
        score.clear()
        score.increase_score()
        player.go_to_starting()
        all_cars.level_up()








screen.exitonclick()