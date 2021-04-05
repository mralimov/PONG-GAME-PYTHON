from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=900, height=600)
screen.title("PONG-GAME")
screen.bgcolor("black")
screen.tracer(0)

R_POSITIONS = (420, 0)
L_POSITIONS = (-430, 0)


r_paddle = Paddle(R_POSITIONS)
l_paddle = Paddle(L_POSITIONS)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()
