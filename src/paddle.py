from turtle import Turtle

class Paddle:
    def __init__(self, positionx, positiony):
        # Create a paddle object
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)  # make it tall like a paddle
        self.paddle.penup()
        self.paddle.goto(positionx, positiony)

    def up(self):
        # Move paddle up (but keep inside game border)
        new_y = self.paddle.ycor() + 25
        if new_y < 260:  # upper limit
            self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        # Move paddle down (but keep inside game border)
        new_y = self.paddle.ycor() - 25
        if new_y > -260:  # lower limit
            self.paddle.goto(self.paddle.xcor(), new_y)

    def auto_move(self, ball):
        # Computer paddle: automatically follows the ball's Y position
        if self.paddle.ycor() < ball.ycor():
            self.paddle.sety(self.paddle.ycor() + 5)
        elif self.paddle.ycor() > ball.ycor():
            self.paddle.sety(self.paddle.ycor() - 5)
