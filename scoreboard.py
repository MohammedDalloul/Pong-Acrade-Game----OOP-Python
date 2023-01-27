from turtle import Turtle

# positions = [(75, 260), (-75, 260)]

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.goto(75, 260)
        self.write(self.r_score, align="center", font=("Calibri", 60, "normal"))
        self.goto(-75, 260)
        self.write(self.l_score, align="center", font=("Calibri", 60, "normal"))

    def update_score_r(self):
        self.r_score += 1
        self.update_score()

    def update_score_l(self):
        self.l_score += 1
        self.update_score()




