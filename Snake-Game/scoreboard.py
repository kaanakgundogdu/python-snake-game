from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        with  open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.style = ('Courier', 12, 'bold')
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.high_score}", move=False, align="center", font=self.style)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with  open("data.txt", "w") as high_score_file:
                high_score_file.write(f'{self.score}')

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.color('red')
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", move=False, align="center", font=self.style)
