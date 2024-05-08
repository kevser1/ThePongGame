from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
