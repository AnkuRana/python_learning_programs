import turtle
from turtle import Turtle, Screen
import random

# color_list = ['#07051b', '#150b37', '#280b53', '#3d0965', '#510e6c',
# '#65156e', '#781c6d', '#8c2369', '#9f2a63', '#b1325a', "#7B68EE",
# '#c43c4e', '#d44842', '#e25734', '#ed6925', '#f57d15', "#FF7F50",
# '#fa9407', '#fcaa0f', '#fac228', '#f5d949', '#f1ef75', "#7FFF00"]


turtle.colormode(255)
simbha = Turtle()
simbha.pensize(1.5)
simbha.speed("fastest")
simbha.penup()
simbha.setposition(-50, 20)
simbha.pendown()

direction = [0, 90, 180, 270]

def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    my_tuple = (red, blue, green)
    return my_tuple

def draw(forward_step):
    simbha.setheading(random.choice(direction))
    simbha.forward(forward_step)

def random_moves():
    steps = random.randint(0, 50)
    simbha.pencolor(random_color())
    draw(steps)

def random_color_circle(size_of_gap):
    times = 0
    while times < int(360/size_of_gap):
        simbha.pencolor(random_color())
        simbha.circle(100)
        simbha.setheading(simbha.heading() + size_of_gap)
        times += 1

screen = Screen()


random_color_circle(10)

screen.exitonclick()