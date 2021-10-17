from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor('black')
screen.title('Python: Snake!')
screen.tracer(0)


gameIsOn = True
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')

screen.onkey(snake.down, 'Down')

screen.onkey(snake.left, 'Left')

screen.onkey(snake.right, 'Right')

while gameIsOn:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.checkCollisionWithWall() or snake.checkCollisionWithTail():
        gameIsOn = False
        score.gameOver()

    if snake.head.distance(food) <= 15:
        score.updateScore()
        food.spawn()
        snake.grow()

screen.exitonclick()
