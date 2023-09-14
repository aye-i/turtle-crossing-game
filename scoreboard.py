from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("Indigo")
        self.hideturtle()
        self.goto(0, 270)
        self.stage = 1
        self.write(align="center", font=FONT, arg=f"STAGE {self.stage}")

    def next_stage(self):
        self.clear()
        self.stage += 1
        self.write(align="center", font=FONT, arg=f"STAGE {self.stage}")

    def game_over(self):
        self.goto(0, 0)
        self.color("Indigo")
        self.write(align="center", font=FONT, arg="GAME OVER!")
