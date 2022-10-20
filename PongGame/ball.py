from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 2
        self.y_move = 2
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        print("bounce_y")

    def bounce_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()

    def update_speed(self, speed):
        self.x_move = speed
        self.y_move = speed

