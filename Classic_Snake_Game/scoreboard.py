from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Showcard Gothic', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", True, align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT,
                   font=FONT)

    def score_up(self):
        self.clear()
        self.goto(0, 280)
        self.score += 1
        self.update_score()
