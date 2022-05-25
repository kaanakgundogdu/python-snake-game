from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.created_snakes = []
        self.create_snakes_onstart()
        self.head = self.created_snakes[0]

    def create_snakes_onstart(self):
        for i in POSITIONS:
            self.create_snake(i)

    def create_snake(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.created_snakes.append(snake)

    def reset_snake(self):
        for sn in self.created_snakes:
            sn.goto(1000,1000)
        self.created_snakes.clear()
        self.create_snakes_onstart()
        self.head = self.created_snakes[0]

    def extend(self):
        self.create_snake(self.created_snakes[-1].position())

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
