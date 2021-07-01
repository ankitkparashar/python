from turtle import Turtle
from typing import Tuple

ALIGNMENT = "center"
FONT: Tuple[str, int, str] = ("Courier", 24, "normal")


def get_high_score():
    with open("data.txt") as high_score:
        return int(high_score.read())


def update_high_score(new_high_score):
    with open("data.txt", "w") as high_score:
        high_score.write(f"{new_high_score}")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            update_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)
