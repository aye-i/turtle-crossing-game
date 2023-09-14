import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Gainsboro")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")

game_is_on = True
count = 0
cars = []
car_throttle = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count == 5:
        cars.append(CarManager(throttling=car_throttle))
        count = 0
        print(f"outside in main: {cars}")
    for car in cars:
        car.drive()
    count += 1

    for car in cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # next stage
    next_lvl = player.go_back()
    if next_lvl:
        scoreboard.next_stage()
        for car in cars:
            car_throttle += 0.25
            car.throttling = car_throttle



screen.exitonclick()
