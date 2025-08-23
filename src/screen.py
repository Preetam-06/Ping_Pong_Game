from turtle import *
from paddle import *
from ball import *
from wall import *
from score import *
import time

# Setup the game window
screen = Screen()
screen.title("PING PONG")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)  # turn off auto screen updates for smooth animation

# Create game components
bd = border()        # draw border
sc = score_bd()      # scoreboard
m1 = menu_bd()       # menu instructions

pd1 = Paddle(350, 0)   # player paddle (right side)
pd2 = Paddle(-350, 0)  # computer paddle (left side)
ball = Ball()          # ball object

# Keyboard input for player
screen.listen()
screen.onkeypress(pd1.up, "Up")
screen.onkeypress(pd1.down, "Down")

game_is_on = True

def game_start():
    global game_is_on, sc, pd2, ball
    while game_is_on:
        time.sleep(0.01)      # control game speed
        pd2.auto_move(ball)   # computer paddle follows ball
        screen.update()       # refresh screen
        ball.move()           # move ball step by step

        # Bounce from top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
           
        # Ball hits player paddle
        if (ball.distance(pd1.paddle) < 30 and ball.xcor() > 340):
            ball.bounce_x()
            ball.change_color()
            sc.scores += 1     # increase score when player hits
            sc.update_score()
        # Ball hits computer paddle
        elif (ball.distance(pd2.paddle) < 30 and ball.xcor() < -340):
            ball.bounce_x()
            ball.change_color()

        # If player misses → computer wins
        if ball.xcor() > 400:
            game_is_on = False
            print("User Game Over")
            sc.end_game2()  
        # If computer misses → player wins
        elif ball.xcor() < -400:
            game_is_on = False
            print("Computer Game Over")
            sc.end_game1()

# Start game with Space key
screen.onkeypress(game_start, "space")

screen.mainloop()
