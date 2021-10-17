from turtle import Turtle
import random
from snake import Snake

class Food(Turtle):
    # default constructor
    def __init__(self):
        super(Food, self).__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.penup()
        self.spawn()
        self.pendown()

    def spawn(self):
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-230, 230))
        self.pendown()
