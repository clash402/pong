from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.SPEED = 1

        self.penup()
        self.color("white")
        self.shape("circle")

        self.x_move = self.SPEED
        self.y_move = self.SPEED

    # PRIVATE METHODS
    def _bounce_x(self):
        self.x_move *= -1

    def _bounce_y(self):
        self.y_move *= -1

    def _increase_speed(self):
        self.x_move *= 1.15

    # PUBLIC METHODS
    def reset_pos(self):
        self.goto(0, 0)
        self._bounce_x()
        self.x_move = self.SPEED

    def move(self):
        pos_x = self.xcor() + self.x_move
        pos_y = self.ycor() + self.y_move
        self.goto(pos_x, pos_y)

    def check_if_has_touched_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self._bounce_y()
            return True

    def check_if_has_touched_paddle(self, paddle_l, paddle_r):
        if (self.distance(paddle_r) < 50 and self.xcor() > 330) \
                or (self.distance(paddle_l) < 50 and self.xcor() < -330):
            self._bounce_x()
            self._increase_speed()
            return True
