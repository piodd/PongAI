from game import Ball
from game import Paddle
from game import gamelogic


class CollisionCalculator:
    def __init__(self, min_x, min_y, max_x, max_y, paddle_1: Paddle, paddle_2: Paddle,
                 ball: Ball, game: gamelogic):
        self.game = game
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.ball = ball
        self.untouchable = 0

    def board_collision_check_paddle(self, paddle: Paddle):
        if paddle.pos_y - paddle.size // 2 < self.min_y:
            paddle.pos_y = self.min_y + paddle.size // 2
        elif paddle.pos_y + paddle.size // 2 > self.max_y:
            paddle.pos_y = self.max_y - paddle.size // 2

    def board_collision_check_ball(self):
        if self.ball.pos_y - self.ball.size // 2 < self.min_y:
            self.ball.pos_y = self.min_y + self.ball.size // 2
            self.ball.speed_y = -self.ball.speed_y
        elif self.ball.pos_y + self.ball.size // 2 > self.max_y:
            self.ball.pos_y = self.max_y - self.ball.size // 2
            self.ball.speed_y = -self.ball.speed_y

        if self.ball.pos_x - self.ball.size // 2 < self.min_x:
            self.ball.pos_x = self.min_x + self.ball.size // 2
            self.ball.speed_x = -self.ball.speed_x
            self.game.get_score(1)
        elif self.ball.pos_x + self.ball.size // 2 > self.max_x:
            self.ball.pos_x = self.max_x - self.ball.size // 2
            self.ball.speed_x = -self.ball.speed_x
            self.game.get_score(2)

    def paddle_ball_collision_check(self, paddle: Paddle):
        if abs(self.ball.pos_x - paddle.pos_x) < self.ball.size // 2 and abs(
                self.ball.pos_y - paddle.pos_y) < paddle.size // 2:
            self.bounce_the_ball(paddle=paddle)

    def all_collision_check(self):
        self.board_collision_check_ball()
        self.board_collision_check_paddle(paddle=self.paddle_1)
        self.board_collision_check_paddle(paddle=self.paddle_2)
        if self.untouchable <= 0:
            self.paddle_ball_collision_check(paddle=self.paddle_1)
            self.paddle_ball_collision_check(paddle=self.paddle_2)
        else:
            self.untouchable -= 1

    def dist_ball_from_paddle(self, paddle: Paddle):
        return ((self.ball.pos_x - paddle.pos_x) ** 2 + (self.ball.pos_y - paddle.pos_y) ** 2) ** (1 / 2)

    def bounce_the_ball(self, paddle: Paddle):
        speed = (self.ball.speed_y ** 2 + self.ball.speed_x ** 2) ** (1 / 2)
        self.ball.speed_x = -self.ball.speed_x
        self.ball.speed_y += (self.ball.pos_y - paddle.pos_y) * speed // paddle.size
        if self.ball.speed_y > 0.8 * speed:
            self.ball.speed_y = 0.8 * speed
        if -self.ball.speed_y > 0.8 * speed:
            self.ball.speed_y = -0.8 * speed
        if self.ball.speed_x > 0:
            self.ball.speed_x = (speed ** 2 - self.ball.speed_y ** 2) ** (1 / 2)
        else:
            self.ball.speed_x = -((speed ** 2 - self.ball.speed_y ** 2) ** (1 / 2))
        self.untouchable = 50

    def all_collision_check_wall(self, ai_number):
        self.board_collision_check_ball()

        self.board_collision_check_paddle(paddle=self.paddle_1)
        self.board_collision_check_paddle(paddle=self.paddle_2)
        if self.untouchable <= 0:
            if ai_number == 1:
                self.paddle_ball_collision_check(paddle=self.paddle_1)
                self.paddle_wall_ball_collision_check(paddle=self.paddle_2)
            if ai_number == 2:
                self.paddle_ball_collision_check(paddle=self.paddle_2)
                self.paddle_wall_ball_collision_check(paddle=self.paddle_1)
        else:
            self.untouchable -= 1

    def paddle_wall_ball_collision_check(self, paddle: Paddle):
        if abs(self.ball.pos_x - paddle.pos_x) < self.ball.size*10 // 2:
            self.bounce_the_ball(paddle=paddle)

    def bounce_the_ball_wall(self, paddle: Paddle):
        speed = (self.ball.speed_y ** 2 + self.ball.speed_x ** 2) ** (1 / 2)
        self.ball.speed_x = -self.ball.speed_x
        self.ball.speed_y += (self.ball.pos_y - paddle.pos_y) * speed // paddle.size
        if self.ball.speed_y > 0.8 * speed:
            self.ball.speed_y = 0.8 * speed
        if -self.ball.speed_y > 0.8 * speed:
            self.ball.speed_y = -0.8 * speed
        if self.ball.speed_x > 0:
            self.ball.speed_x = (speed ** 2 - self.ball.speed_y ** 2) ** (1 / 2)
        else:
            self.ball.speed_x = -((speed ** 2 - self.ball.speed_y ** 2) ** (1 / 2))
        self.untouchable = 50