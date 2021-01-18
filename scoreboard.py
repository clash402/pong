from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.FONT = ("Courier", 80, "normal")
        self.ALIGNMENT = "center"

        self.score_l = 0
        self.score_r = 0

        self.penup()
        self.hideturtle()
        self.color("white")

        self._update_display()

    # PRIVATE METHODS
    def _update_display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align=self.ALIGNMENT, font=self.FONT)

        self.goto(100, 200)
        self.write(self.score_r, align=self.ALIGNMENT, font=self.FONT)

    # PUBLIC METHODS
    def increase_score(self, paddle_id):
        if paddle_id == "paddle_l":
            self.score_l += 1
        elif paddle_id == "paddle_r":
            self.score_r += 1
        self._update_display()
