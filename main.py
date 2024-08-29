from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right = Paddle((370, 0))
left = Paddle((-380, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right.up, "Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(
            left) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    #Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
