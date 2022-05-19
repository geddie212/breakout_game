from turtle import Turtle
import colors
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.setposition((0, -225))
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def hit(self):
        self.y_move *= -1
        self.color(random.choice(colors.color_list))

    def bounce(self):
        self.x_move *= -1

    def bounce_back(self):
        self.y_move *= -1


