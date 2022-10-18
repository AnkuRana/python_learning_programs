from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_turtle = []
        self.create_snake()

    def create_snake(self):
        pos = 0
        for i in range(3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=pos, y=0)
            self.snake_turtle.append(new_turtle)
            pos -= 20

    def move(self):
        for snake in range(len(self.snake_turtle) - 1, 0, -1):
            new_x = self.snake_turtle[snake - 1].xcor()
            new_y = self.snake_turtle[snake - 1].ycor()
            self.snake_turtle[snake].goto(new_x, new_y)
        self.snake_turtle[0].forward(MOVE_DISTANCE)

    def left(self):
        self.snake_turtle[0].setheading(180)

    def right(self):
        self.snake_turtle[0].setheading(0)

    def up(self):
        self.snake_turtle[0].setheading(90)

    def down(self):
        self.snake_turtle[0].setheading(270)
