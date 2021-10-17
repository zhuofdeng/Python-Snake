from turtle import Turtle, heading

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_UNIT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :
    segments = []
    head = None

    # default constructor
    def __init__(self):
        #create the intial snake body and put it at the center of the screen.
        for position in STARTING_POSITIONS:
            self.addSegment(position)
            self.head = self.segments[0]

    def update():
        print('update sname')

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def move(self):
        for segIndex in range(len(self.segments) - 1, 0, -1):
            xPos = self.segments[segIndex - 1].xcor()
            yPos = self.segments[segIndex - 1].ycor()
            self.segments[segIndex].goto(xPos, yPos)
        self.head.forward(MOVEMENT_UNIT)
        
    def checkCollisionWithWall(self):
        if self.head.xcor() <= -290 or self.head.xcor() >= 290 or self.head.ycor() <= -240 or self.head.ycor() >= 240:
            return True
        else:
            return False

    def checkCollisionWithTail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) <= 10:
                return True
        
        return False

    def addSegment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        self.addSegment(self.segments[-1].position())