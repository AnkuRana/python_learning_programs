from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ROAD_NORTH_END = 280
ROAD_SOUTH_END = -280
STARTING_X_COR = 260
UPPER_LIMIT_Y = 260
LOWER_LIMIT_Y = -250
# ROAD_LANES =[(260,-240 ), (260,-200 ), (260,-160 ), (260,-120 ), (260,-80 ), (260,-40 ), (260,0 ), (260,40 ),
#              (260,80 ), (260,120 ), (260,160 ), (260,200 ), (260,-240 )]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        # self.render_cars()

    def generate_cars(self, no_of_cars):
        for car in range(0, no_of_cars):
            new_car = Turtle()
            random_ycor = random.randint(LOWER_LIMIT_Y, UPPER_LIMIT_Y)
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(STARTING_X_COR, random_ycor)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            random_move = random.randint(1, 10)
            car.forward(random_move)

    # def create_car(self, position):
    #     self.color(random.choice(COLORS))
    #     self.shape("square")
    #     self.setheading(180)
    #     self.shapesize(stretch_wid=1, stretch_len=2)
    #     self.penup()
    #     self.goto(position)

    # def render_cars(self):
    #     for i in range(0, 13):
    #         self.cars[i].goto(ROAD_LANES[i])

    def detect_collision(self, player):
        is_collision = False
        for car in self.cars:
            if player.distance(car) < 26:
                return True






