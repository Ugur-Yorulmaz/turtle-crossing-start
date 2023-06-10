from turtle import Turtle
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        select = randint(1,2)
        if select == 2:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(200, randint(-150,150))
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.goto(car.xcor()-self.speed, car.ycor())

    def level_up(self):
        self.speed+=MOVE_INCREMENT
        self.car_move()



