import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        x_cor =  random.randint(-250,250)
        y_cor = random.randint(-250,250)
        self.goto(x_cor,y_cor)