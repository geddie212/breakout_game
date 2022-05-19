from turtle import Turtle, Screen
from spaceship import SpaceShip
from ball import Ball
from bricks import Bricks
from walls import Walls
import time
from score_board import ScoreBoard
from loss_timer import LossTimer
import colors

screen = Screen()
screen._root.iconbitmap("game_ico.ico")
width = 800
height = 800
screen.bgpic("universe.png")
screen.title('Break Out')
screen.setup(width=width, height=height)
screen.tracer(0)


level_layer = 2
level = 1
level_str = f'Level: {level}'
game_on = True
level_finish = False
lost_ball = False
ceiling_bounce = False
move_speed = 0.05

left_wall = 0 - (width / 2) + 15
right_wall = 0 + (width / 2) - 15
ceiling = 0 + (height / 2) - 150
bottom = 0 - (height / 2)


space_ship = SpaceShip()
ball = Ball()
bricks = Bricks()
position_list = bricks.lay_bricks(level_layer)
score = ScoreBoard(len(position_list), level)
walls = Walls(width, height)
loss_time = LossTimer()
# loss_time.update('HELLO')


while game_on:
    time.sleep(move_speed)

    y_cor = ball.ycor()
    x_cor = ball.xcor()
    s_y_cor = space_ship.ycor()
    s_x_cor = space_ship.xcor()

    if level_finish:
        level_layer += 1
        level += 1
        position_list = bricks.lay_bricks(level_layer)
        loss_time.update_color(-1)
        loss_time.update(f'YOU WIN')
        time.sleep(1)
        countdown = 3
        loss_time.update_color(countdown - 1)
        loss_time.update(countdown)
        for i in range(0, 3):
            time.sleep(1)
            loss_time.update_color(countdown - 1)
            loss_time.update(countdown)
            countdown -= 1
        level_finish = False
        loss_time.clearer()
        move_speed = 0.05

    if lost_ball:
        countdown = 3
        loss_time.update_color(countdown - 1)
        loss_time.update(countdown)
        for i in range(0, 3):
            time.sleep(1)
            countdown -= 1
            loss_time.update_color(countdown - 1)
            loss_time.update(countdown)
        lost_ball = False
        loss_time.clearer()

    ball.move()

    screen.listen()
    screen.onkey(key='Left', fun=space_ship.move_left)
    screen.onkey(key='Right', fun=space_ship.move_right)

    if y_cor <= s_y_cor + 15:
        if s_x_cor - 50 <= x_cor <= s_x_cor + 50:
            ball.hit()
            ball.setposition(x_cor, y_cor + 15)

    if left_wall >= x_cor:
        ball.bounce()
        ball.setposition(x_cor + 15, y_cor)
    elif x_cor >= right_wall:
        ball.bounce()
        ball.setposition(x_cor - 15, y_cor)
    elif y_cor >= ceiling:
        ball.bounce_back()
        ceiling_bounce = True
        ball.setposition(x_cor, y_cor - 15)
    for idx, pos in enumerate(position_list):

        if pos[0] - 50 <= x_cor <= pos[0] + 50 and y_cor >= pos[1] - 15 and ball.y_move > 0:
            ball.hit()
            score.hit()
            del position_list[idx]
            for idx, brick in enumerate(bricks.bricks):
                if brick.xcor() == pos[0] and brick.ycor() == pos[1]:
                    brick.setposition(0, height)
                    if move_speed > 0:
                        move_speed -= 0.002
            ball.setposition(x_cor, y_cor - 15)
            break

        elif pos[0] - 50 <= x_cor <= pos[0] + 50 and y_cor <= pos[1] + 15 and ball.y_move < 0 and ceiling_bounce:
            ball.hit()
            score.hit()
            del position_list[idx]
            for idx, brick in enumerate(bricks.bricks):
                if brick.xcor() == pos[0] and brick.ycor() == pos[1]:
                    brick.setposition(0, height)
                    if move_speed > 0:
                        move_speed -= 0.002
            ball.setposition(x_cor, y_cor + 15)
            ceiling_bounce = False
            break

    if len(position_list) == 0:
        level_finish = True
        ball.goto(s_x_cor, s_y_cor + 25)
        score.level_finish()

    if y_cor <= bottom:
        ball.goto(s_x_cor, s_y_cor + 25)
        if ball.y_move <= 0:
            ball.y_move = ball.y_move * -1
        lost_ball = True

    screen.update()

screen.exitonclick()
