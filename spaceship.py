from turtle import Turtle

MOVE_INCREMENT = 40

class SpaceShip(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('#887d82')
        self.penup()
        self.shapesize(1, 5, 0)
        self.setposition((0, -250))

    def move_left(self):
        self.setposition(self.xcor() - MOVE_INCREMENT, self.ycor())

    def move_right(self):
        self.setposition(self.xcor() + MOVE_INCREMENT, self.ycor())
