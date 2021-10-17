from turtle import Turtle

class Score(Turtle):
    score = 0
    def __init__(self):
        super(Score, self).__init__()
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.color('white')
        self.printScore()
    
    def printScore(self):
        self.write('Score: {}'.format(self.score), align='center', font=('Arial', 30, 'normal'))

    def updateScore(self):
        self.clear()
        self.score += 1
        self.printScore()
    
    def gameOver(self):
        self.goto(0, 0)
        self.write('Game Over!', align='center', font=('Arial', 30, 'normal'))