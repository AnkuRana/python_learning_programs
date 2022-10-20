from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.pad_segments = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # new_paddle.setheading(90)
        self.goto(position)
        # self.paddle_head = self.pad_segments[0]

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def move_up(self):
    #     self.paddle_head =self.pad_segments[0]
    #     self.paddle_head.setheading(UP)
    #     if self.paddle_head.ycor() < 280:
    #         for segment in range(len(self.pad_segments) - 1, 0, -1):
    #             x_cor = self.pad_segments[segment-1].xcor()
    #             y_cor = self.pad_segments[segment-1].ycor()
    #             self.pad_segments[segment].goto(x_cor, y_cor)
    #         self.paddle_head.forward(MOVE)
    #
    # def move_down(self):
    #     self.paddle_head = self.pad_segments[-1]
    #     self.paddle_head.setheading(DOWN)
    #     if self.paddle_head.ycor() > -280:
    #         for segment in range(0, 3):
    #             x_cor = self.pad_segments[segment + 1].xcor()
    #             y_cor = self.pad_segments[segment + 1].ycor()
    #             self.pad_segments[segment].goto(x_cor, y_cor)
    #         self.paddle_head.forward(MOVE)






