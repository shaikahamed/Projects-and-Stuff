from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)
# create two paddles left and right
r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
# create a ball
ball = Ball()
# create a scoreboard
scoreboard = Scoreboard()
# Event listeners
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
is_game_on = True

# play game till over
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ball.move()
    # detect ball touch the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect ball is out of the screen
    if ball.xcor() > 380:
        time.sleep(1)
        ball.reverse_direction()
        scoreboard.l_point()

    if ball.xcor() < -380:
        time.sleep(1)
        ball.reverse_direction()
        scoreboard.r_point()

    # check for game over
    if scoreboard.is_over():
        is_game_on = False
        scoreboard.declare_winner()

screen.exitonclick()
