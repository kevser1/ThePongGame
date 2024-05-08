from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)
ball1 = Ball()



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

r_paddle_score = Scoreboard((-150, 260))
l_paddle_score = Scoreboard((150, 260))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball1.move()
    #detect collision with wall
    if ball1.ycor() > 280 or ball1.ycor() < -280:
        #needs to bounce
        ball1.bounce_y()

    if ball1.xcor() > 360:
        ball1.bounce_x()
        r_paddle_score.increase_score()
        ball1.reset_position()
    if ball1.xcor() < - 360:
        ball1.bounce_x()
        l_paddle_score.increase_score()
        ball1.reset_position()

    #detech collision with r_paddle
    if ball1.distance(r_paddle) <50 and ball1.xcor()>320 or ball1.distance(l_paddle) < 50 and ball1.xcor()<-320 :
        print("made contact")
        ball1.bounce_x()



screen.exitonclick()
