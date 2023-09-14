from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, throttling):
        super().__init__()
        # self.car_list = []
        # self.hideturtle()
        self.throttling = throttling
        self.generate_car()

    def generate_car(self):
        # self = Turtle()
        select_colour = random.choice(COLORS)
        print(select_colour)
        self.color(select_colour)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        set_pos = (320, random.randint(-250, 250))
        self.goto(set_pos)
        # self.car_list.append(new_car)
        # print(f"Inside car manager: {self.car_list}")

    # def throttle(self):
    #     self.throttling += 1
    #     print(f"{self.throttling}")
    #     print(f"Throttling to : {MOVE_INCREMENT}")

    def drive(self):
        # for car in self.car_list:
        #     car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())
        self.goto(self.xcor() - (MOVE_INCREMENT+self.throttling), self.ycor())
        print(f"In drive: {MOVE_INCREMENT}")



