from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, initial_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(initial_position)
        self.setheading(90)



        # self.segments = []
        # self.create_paddle()
    #     self.initial_position = initial_position
    #
    #
    # def create_paddle(self):
    #     self = Turtle("square")
    #     self.color("white")
    #     self.shapesize(stretch_wid=1, stretch_len=5)
    #     self.penup()
    #     self.goto(x=self.initial_position, y=0)
    #     self.setheading(90)
    #     self.segments.append(segment)

    def up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
