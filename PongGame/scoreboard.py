from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Showcard Gothic', 30, 'normal')
R_SCORE_LOC = (40, 250)
L_SCORE_LOC = (-40, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(L_SCORE_LOC)
        self.write(f"{self.l_score}", True, align=ALIGNMENT, font=FONT)
        self.goto(R_SCORE_LOC)
        self.write(f"{self.r_score}", True, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.update_board()
