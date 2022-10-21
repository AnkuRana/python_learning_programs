import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
car.generate_cars(scoreboard.level)
screen.listen()

screen.onkey(player.move_player, "Up")
screen.onkey(player.move_player, "w")

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check Player Collision with the cars
    if car.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    # check if player has crosses the Finish line
    if player.ycor() >= 280:
        player.reset_player()
        scoreboard.update_level()

    # To Delay generation of the cars
    if count % 6 == 0:
        car.generate_cars(scoreboard.level)
    # car.render_cars()

    car.move_car()
    count += 1

screen.exitonclick()