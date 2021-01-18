from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, gui, paddle_id):
        super().__init__()

        self.gui = gui
        self.id = paddle_id

        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(pos)

        self._update_movement()

    # PRIVATE METHODS
    def _update_movement(self):
        self.gui.listen()

        if self.id == "paddle_l":
            self.gui.onkey(self._move_up, "w")
            self.gui.onkey(self._move_down, "s")
        elif self.id == "paddle_r":
            self.gui.onkey(self._move_up, "Up")
            self.gui.onkey(self._move_down, "Down")

    def _move_up(self):
        pos_y = self.ycor() + 30
        self.goto(self.xcor(), pos_y)

    def _move_down(self):
        pos_y = self.ycor() - 30
        self.goto(self.xcor(), pos_y)

    # PUBLIC METHODS
    def has_scored(self, paddle, ball):
        if paddle == "paddle_l":
            if ball.xcor() > 420:
                return True
        elif paddle == "paddle_r":
            if ball.xcor() < -420:
                return True
