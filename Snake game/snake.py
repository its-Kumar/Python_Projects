import turtle as t
UP =90
DOWN =270
LEFT = 180
RIGHT = 0
MOVEPOSITION = 20
CREATESNAKE = 3

import time
class Snake:

    def __init__(self):
        self.z =0
        self.w = 0
        self.segments = []
        self.is_game_on = True
        self.screen = t.Screen()

    def position(self):
        for i in range(CREATESNAKE):
            self.add_snake(self.z,self.w)
            self.z -= 20
    def add_snake(self,z,w):
        self.new_snake = t.Turtle(shape="square")
        self.new_snake.penup()
        self.new_snake.goto(x=z, y=w)
        self.new_snake.color("white")
        self.segments.append(self.new_snake)

    def extend(self):
        self.z = self.segments[-1].xcor()
        self.w = self.segments[-1].ycor()
        self.add_snake(self.z,self.w)
    def move(self):

            for seg in range((len(self.segments) - 1), 0, -1):
                self.new_xcor = self.segments[seg - 1].xcor()
                self.new_ycor = self.segments[seg - 1].ycor()
                self.segments[seg].goto(self.new_xcor, self.new_ycor)
            self.segments[0].forward(MOVEPOSITION)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.z =0
        self.w =0
        self.position()



    def Up(self):
        if self.segments[0].heading() != DOWN:
           self.segments[0].setheading(UP)

    def Down(self):
        if self.segments[0].heading() != UP:
           self.segments[0].setheading(DOWN)
    def Left(self):
        if self.segments[0].heading() != RIGHT:
           self.segments[0].setheading(LEFT)
    def Right(self):
        if self.segments[0].heading() != LEFT:
           self.segments[0].setheading(RIGHT)