from turtle import Turtle
import colors
import random

POSITION = (0, 0)
ALIGNMENT = 'center'
FONT = ('Arial', 100, 'bold')

class LossTimer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('#fa6ee8')
        self.hideturtle()
        self.speed('fastest')
        self.goto(POSITION)

    def update(self, time):
        self.clearer()
        self.write(f'{time}', False, align=ALIGNMENT, font=FONT)

    def update_color(self, index):
        self.clearer()
        self.color(colors.color_list[index])

    def clearer(self):
        self.clear()

