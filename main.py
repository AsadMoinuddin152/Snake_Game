import time
from turtle import Screen, Turtle
from Snake import Snake
from Food import Food
from score import Score

# Screen Setup Code
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake_Game")

# 1st Task:-  Create a Snake Body and Food
snake = Snake()
food = Food()
score = Score()

# 2nd Task:- Creating moving keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 3rd Task:- Move the Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.moving()

    # 3.1 task:- Detecting the collision and score board
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.increase_score()

    # 3.2 task:- Detecting the Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.gameOver()

    # 3.3 task:- Detect the collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameOver()

screen.exitonclick()
