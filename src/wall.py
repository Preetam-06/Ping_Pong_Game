from turtle import *

class border(Turtle):
    def __init__(self):
        # Create a red border around the play area
        bd = Turtle()
        bd.color("red")
        bd.hideturtle()
        bd.pensize(10)
        bd.penup()
        bd.goto(400, 300)    # top right corner
        bd.pendown()
        bd.goto(400, -300)   # draw right wall
        bd.goto(-400, -300)  # draw bottom wall
        bd.goto(-400, 300)   # draw left wall
        bd.goto(400, 300)    # close the rectangle (back to top right)
