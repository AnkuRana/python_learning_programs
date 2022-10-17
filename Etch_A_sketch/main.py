from turtle import Turtle, Screen

simbha = Turtle()
screen = Screen()
angle = 0


def clear_screen():
    simbha.clear()
    simbha.penup()
    simbha.home()
    simbha.pendown()


def move_forward():
    simbha.forward(10)


def move_backward():
    simbha.backward(10)


def turn_antilclockwise():
    simbha.left(5)

def turn_clockwise():
    simbha.right(5)

screen.listen()
# simbha.degrees(30)
screen.onkeypress(key = "w", fun = move_forward)
screen.onkeypress(key = "s", fun = move_backward)
screen.onkeypress(key = "a", fun = turn_antilclockwise)
screen.onkeypress(key = "d", fun = turn_clockwise)

screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()