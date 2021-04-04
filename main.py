from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=900, height=600)
screen.title("PONG-GAME")
screen.bgcolor("black")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(-430, 0)


def left_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def left_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(left_up, "Up")
screen.onkey(left_down, "Down")
