from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.head.distance(food) < 20:
        food.move_random_location()
        scoreboard.add_score()
        snake.extend()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        is_game_on = False
        scoreboard.game_over()
    for segment in snake.created_snakes[1:]:
        if snake.head.distance(segment) < 8:
            is_game_on = False
            scoreboard.game_over()
screen.exitonclick()
