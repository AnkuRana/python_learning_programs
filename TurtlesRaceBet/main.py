from turtle import Turtle, Screen
import random

colors = ["red", "yellow", "blue" ,"orange", "purple", "green"]
is_race_on = False


def create_turtle():
    pos = -170
    turtle_list = []
    for i in range(6):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(colors[i])
        new_turtle.goto(x=-250, y=pos)
        turtle_list.append(new_turtle)
        pos += 60
    return turtle_list


screen = Screen()
screen.setup(height=500, width=600)
all_turtles = create_turtle()
user_bet = screen.textinput(title="Enter your bet", prompt="Choose your turtle. enter color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_no in all_turtles:
        if turtle_no.xcor() > 280:
            wining_turtle = turtle_no.pencolor()
            if wining_turtle == user_bet:
                print(f"You have won! The {wining_turtle} is the wining turtle")
            else:
                is_race_on = False
                print(f"You have lost! The {wining_turtle} is the wining turtle")
        turtle_no.forward(random.randint(0, 10))

screen.exitonclick()
