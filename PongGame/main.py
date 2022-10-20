import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, ALIGNMENT, FONT

STARTING_POSITIONS_PAD_1 = (-370, 0)
STARTING_POSITIONS_PAD_2 = (370, 0)
WINING_SCORE = 10
DEFAULT_SPEED = 2


screen = Screen()
screen.tracer(0)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()

left_paddle = Paddle(STARTING_POSITIONS_PAD_1)
right_paddle = Paddle(STARTING_POSITIONS_PAD_2)

winner = Turtle()
winner.hideturtle()
winner.penup()
winner.color("white")

ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

is_game_on = True
count = 1
speed = 2
while is_game_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    var = ball.ycor()

    # detect collision with walls up and down
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with left and right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or \
            ball.distance(left_paddle) < 50 and ball.xcor() <= -340:
        ball.bounce_x()
        count += 1

    # if right paddle misses the ball
    if ball.xcor() > 370:
        scoreboard.l_point()
        ball.ball_reset()
        speed = DEFAULT_SPEED
        ball.update_speed(speed)

    # if left paddle misses the ball
    if ball.xcor() < -370:
        scoreboard.r_point()
        ball.ball_reset()
        speed = DEFAULT_SPEED
        ball.update_speed(speed)

    if scoreboard.l_score == 10:
        winner.goto(0, 0)
        winner.write("LEFT SIDE WINS ! GAME OVER", True, align=ALIGNMENT, font=FONT)
        is_game_on = False

    if scoreboard.r_score == 10:
        winner.goto(0, 0)
        winner.write("RIGHT SIDE WINS ! GAME OVER", True, align=ALIGNMENT, font=FONT)
        is_game_on = False

    # After every 5 times increase speed
    if count % 5 == 0:
        speed += 1
        ball.update_speed(speed)
        count = 1


screen.exitonclick()
