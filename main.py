from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=900, height=600)
screen.title("PONG-GAME")
screen.bgcolor("black")
screen.tracer(0)


screen.listen()
screen.onkey(left_up, "Up")
screen.onkey(left_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()
