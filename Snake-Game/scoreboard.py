from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.style = ('Courier', 12, 'bold')
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        print(self.score)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}", move=False, align="center", font=self.style)

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"GAME OVER!", move=False, align="center", font=self.style)
