from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.created_snakes = []
        self.create_snakes()
        self.head = self.created_snakes[0]

    def create_snakes(self):
        for i in range(0, 3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(0 - i * 20, 0)
            self.created_snakes.append(snake)

    def move(self):
        for snake_num in range(len(self.created_snakes) - 1, 0, -1):
            new_x = self.created_snakes[snake_num - 1].xcor()
            new_y = self.created_snakes[snake_num - 1].ycor()
            self.created_snakes[snake_num].goto(new_x, new_y)
        self.created_snakes[0].forward(MOVE_DISTANCE)

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
