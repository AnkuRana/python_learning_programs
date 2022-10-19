from snake import Snake
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with the food of snake
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scorecard.score_up()
        snake.extend_snake()

    # Detect collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 \
            or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        is_game_on = False
        scorecard.game_over()

    # Detect collision with its own body or tail
    # passing the time when turtle is snake head used slicing
    for turtle in snake.snake_turtle[1:]:
        if snake.snake_head.distance(turtle) < 10:
            is_game_on = False
            scorecard.game_over()


screen.title("------- SNAKE GAME -----")
screen.exitonclick()
