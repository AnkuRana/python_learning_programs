import random
import turtle

import colorgram
from turtle import Turtle, Screen

color_list = []
turtle.colormode(255)

# def extract_colors():
#     """extract colors from image using colorgram module"""
#     colors = colorgram.extract("damien_hirst.jpg", 30)
#     for color in colors:
#         red  = color.rgb.r
#         green = color.rgb.g
#         blue = color.rgb.b
#         color_tuple =  (red, green, blue)
#         color_list.append(color_tuple)


# extracted colors from above than copy them in the list
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

simbha = Turtle()
simbha.speed("normal")
# extract_colors()
simbha.penup()
simbha.hideturtle()
# x,y are those values as i wanted  turtle to start in middle and end of screen
simbha.setposition(-235, -235)


def make_damin_hirst():
    x = -235
    y = -235
    for i in range(10):
        for j in range(10):
            simbha.pencolor(random.choice(color_list))
            simbha.dot(20)
            x += 50
            simbha.goto(x, y)
        x = -235
        y += 50
        simbha.goto(x, y)


screen = Screen()
make_damin_hirst()
screen.exitonclick()
