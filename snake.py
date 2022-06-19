from turtle import Turtle, Screen
import time

screen = Screen()
x_coordinates = [0, -20, -40]
move_distance = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):

        for num in range(3):
            new_segment = Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(x_coordinates[num], 0)
            self.segments.append(new_segment)

    def movesnake(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(move_distance)


    def extend(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        if self.head.heading() == 270:
            new_segment.setposition(self.segments[-1].xcor(), self.segments[-1].ycor() + 20)

        elif self.head.heading() == 90:
            new_segment.setposition(self.segments[-1].xcor(), self.segments[-1].ycor() - 20)

        elif self.head.heading() == 180:
            new_segment.setposition(self.segments[-1].xcor() + 20, self.segments[-1].ycor())

        elif self.head.heading() == 0:
            new_segment.setposition(self.segments[-1].xcor() - 20, self.segments[-1].ycor())


        self.segments.append(new_segment)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def resetsnake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
        self.movesnake()
