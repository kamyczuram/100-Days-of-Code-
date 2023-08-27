from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            turtle = Turtle("square")
            turtle.penup()
            turtle.goto(position)
            self.segments.append(turtle)

    def move(self):

        for segment_number in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_number].goto(self.segments[segment_number - 1].xcor(),
                                               self.segments[segment_number - 1].ycor())
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)

    def right(self):
        self.head.seth(0)

    def down(self):
        self.head.seth(270)

    def left(self):
        self.head.seth(180)

    def append(self):
        turtle = Turtle("square")
        turtle.penup()
        turtle.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(turtle)
