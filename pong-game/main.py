from turtle import Turtle, Screen
from ball import Ball
import time
from paddle import Paddle
from scoreborad import  Scoreboard

screen = Screen()
screen.tracer(0)
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")




screen.listen()
screen.onkey(l_paddle.move_up,"w")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #Detect collision with wall
    if  ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
        ball.speed(10)
        ball.bounce_x()


    #Detect R paddle misses
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()
        scoreboard.update_scoreboard()





screen.exitonclick()