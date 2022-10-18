from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.title("------- SNAKE GAME -----")
screen.exitonclick()
