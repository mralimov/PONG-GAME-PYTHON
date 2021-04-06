
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movement_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.x_move
        new_x = self.xcor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.movement_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.movement_speed = 0.1
        self.bounce_x()
