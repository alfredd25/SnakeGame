from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font = FONT)
        self.hideturtle()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
