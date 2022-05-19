from turtle import Turtle

POSITION = (0, 310)
ALIGNMENT = 'center'
FONT = ('Arial', 50, 'bold')


class ScoreBoard(Turtle):

    def __init__(self, total, level):
        super().__init__()
        self.penup()
        self.color('#fa6ee8')
        self.hideturtle()
        self.speed('fastest')
        self.goto(POSITION)
        self.score = 0
        self.level = level
        self.total = total
        self.update()


    def update(self):
        self.clear()
        self.write(f'SCORE: {self.score}/{self.total} LEVEL: {self.level}', False, align=ALIGNMENT, font=FONT)

    def hit(self):
        self.score += 1
        self.update()

    def level_finish(self):
        self.level += 1
        self.score = 0
        self.update()