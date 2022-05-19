from turtle import Turtle

class Walls():

    def __init__(self, ceiling_width, wall_height):
        self.ceiling_width = ceiling_width
        self.wall_height = wall_height
        self.left_wall = Turtle()
        self.right_wall = Turtle()
        self.ceiling = Turtle()

        self.wall_maker(self.left_wall, 'left')
        self.wall_maker(self.right_wall, 'right')
        self.wall_maker(self.ceiling, 'top')

    def wall_maker(self, turtle, position):
        turtle.shape('square')
        turtle.color('#887d82')
        turtle.penup()
        if position == 'left':
            turtle.shapesize(self.wall_height / 10, 1, 0)
            turtle.setposition(0-(self.ceiling_width / 2), 0)
        elif position == 'right':
            turtle.shapesize(self.wall_height / 10, 1, 0)
            turtle.setposition(0 + (self.ceiling_width / 2) - 7, 0)
        elif position == 'top':
            turtle.shapesize(0.5, self.ceiling_width / 10, 0)
            turtle.setposition(0, 0 + (self.wall_height / 2) - 100)

