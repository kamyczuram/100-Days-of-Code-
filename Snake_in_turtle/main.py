from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on= True

score = 0

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.append()
        score = score +1
        print(score)

    if abs(snake.head.xcor())>280 or abs(snake.head.ycor()) >280:
        game_is_on = False
        print("Game Over")


    for index in range (1, len(snake.segments), 1):
        if snake.head.distance(snake.segments[index]) < 15:
            game_is_on = False
            print("Game Over")

screen.exitonclick()