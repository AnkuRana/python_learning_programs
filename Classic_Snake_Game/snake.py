from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_turtle = []
        self.create_snake()
        self.snake_head = self.snake_turtle[0]

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
        self.snake_head.forward(MOVE_DISTANCE)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_turtle[0].setheading(DOWN)
