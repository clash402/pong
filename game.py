from gui import GUI
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle


class Game:
    def __init__(self):
        self.gui = GUI()
        self.scoreboard = Scoreboard()
        self.ball = Ball()

        self.paddle_l = Paddle((-350, 0), self.gui, "paddle_l")
        self.paddle_r = Paddle((350, 0), self.gui, "paddle_r")

        self.game_is_in_progress = True

    # PUBLIC METHODS
    def play(self):
        while self.game_is_in_progress:
            self.gui.update()

            self.ball.move()
            self.ball.check_if_has_touched_wall()
            self.ball.check_if_has_touched_paddle(self.paddle_l, self.paddle_r)

            if self.paddle_l.has_scored(self.paddle_l.id, self.ball):
                self.ball.reset_pos()
                self.scoreboard.increase_score(self.paddle_l.id)

            if self.paddle_r.has_scored(self.paddle_r.id, self.ball):
                self.ball.reset_pos()
                self.scoreboard.increase_score(self.paddle_r.id)
