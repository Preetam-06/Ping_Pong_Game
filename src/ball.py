from turtle import *
import random

colormode(255)  # allow RGB values for colors

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0, 0)

        # Random initial direction and speed
        self.new_dx = random.choice([-3, -2.9, -2.8, 2.8, 2.9, 3])
        self.new_dy = random.choice([-3, -2.9, -2.8, 2.8, 2.9, 3])

        # Give the ball a random color
        self.change_color()

    def random_color(self):
        # Generate a random RGB color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def change_color(self):
        # Apply a random color to the ball
        self.color(self.random_color())

    def move(self):
        # Update ball position based on dx and dy
        self.goto(self.xcor() + self.new_dx, self.ycor() + self.new_dy)

    def bounce_y(self):
        # Reverse vertical direction when hitting top/bottom wall
        self.new_dy *= -1

    def bounce_x(self):
        # Reverse horizontal direction when hitting paddle
        self.new_dx *= -1
