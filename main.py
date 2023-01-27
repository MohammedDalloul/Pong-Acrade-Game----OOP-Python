from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((425, 0))
l_paddle = Paddle((-425, 0))
ball = Ball()
score = Score()

screen.update()

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 440:
        ball.goto(0, 0)
        ball.move_speed = 0.09
        ball.bounce_x()
        score.clear()
        score.update_score_l()

    if ball.xcor() < -440:
        ball.goto(0, 0)
        ball.bounce_x()
        score.clear()
        score.update_score_r()


    # if ball.xcor() > 440:
    #     score2.update_score()
    #
    # elif ball.xcor() < -440:
    #     score1.update_score()

screen.exitonclick()



# from turtle import Turtle
# POSITIONS = [(435, -30), (435, 0), (435, 30)]
#
# class Paddle1(Turtle):
#

#
#     def up(self):
#         self.pad_list[-1].setheading(90)
#         self.pad_list[-1].fd(30)
#         self.move_paddle1_up()
#
#     def down(self):
#         self.pad_list[0].setheading(270)
#         self.pad_list[0].fd(30)
#         self.move_paddle1_down()
#
#     def move_paddle1_up(self):
#         for seg in range(0, 3):
#             self.pad_list[seg].goto(self.pad_list[seg + 1].position())
#
#     def move_paddle1_down(self):
#         for seg in range(0, 3):
#             self.pad_list[seg].goto(self.pad_list[seg - 1].position())
#

#
# self.color("white")
# self.penup()
# self.hideturtle()
# self.r_score = 0
# self.l_score = 0
# self.goto(85, 330)
# self.write(arg=f"{self.r_score}", align="center", font=("Calibri", 60, "normal"))
# self.goto(-85, 330)
# self.write(arg=f"{self.r_score}", align="center", font=("Calibri", 60, "normal"))
