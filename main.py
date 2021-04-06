from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=900, height=600)
screen.title("PONG-GAME")
screen.bgcolor("black")
screen.tracer(0)

R_POSITIONS = (420, 0)
L_POSITIONS = (-430, 0)


r_paddle = Paddle(R_POSITIONS)
l_paddle = Paddle(L_POSITIONS)

ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detecting collision with wall bouns
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

        # Detect ball touch with R-Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
screen.exitonclick()
