from turtle import Turtle
import colors

class Bricks():

    def __init__(self):
        self.bricks = []

    def lay_bricks(self, layers):
        x_pos = -320
        y_pos = 200
        x_position_list = []
        y_position_list = []
        position_list = []
        for ix, i in enumerate(range(1, layers)):
            for idx, j in enumerate(range(1, 9)):
                position_list.append([x_pos, y_pos])
                brick = Turtle()
                brick.shape('square')
                brick.color(colors.color_list[idx])
                brick.penup()
                brick.shapesize(1, 4, 0)
                brick.setposition(x_pos, y_pos)
                self.bricks.append(brick)
                x_pos += 90
            x_pos = -320
            y_pos -= 30
        return position_list