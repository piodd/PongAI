from game import SettingGame
from game import Ball
from game import Paddle
from game import CollisionCalculator
import random


class Game:
    def __init__(self, setting: SettingGame.SettingGame):
        self.HEIGHT = setting.HEIGHT
        self.WIDTH = setting.WIDTH
        self.paddle_speed = setting.paddle_speed
        self.ball_speed = setting.ball_speed
        self.ball_size = setting.ball_size
        self.paddle_size = setting.paddle_size
        self.paddle_r_size = setting.paddle_r_size
        self.max_duration_game = setting.max_game_duration
        self.max_score = setting.max_score
        self.ai_number = setting.ai_number
        self.random_reflection = setting.random_reflection

        self.min_x = setting.LEFT_TOP_CORNER[0]
        self.min_y = setting.LEFT_TOP_CORNER[1]
        self.max_x = setting.RIGHT_BOT_CORNER[0]
        self.max_y = setting.RIGHT_BOT_CORNER[1]

        self.player_1_score = 0
        self.player_2_score = 0

        self.paddle_1 = Paddle.Paddle(self.min_x + 50, (self.min_y + self.max_y) // 2, self.paddle_speed,
                                      self.paddle_r_size, self.paddle_size)
        self.paddle_2 = Paddle.Paddle(self.max_x - 50, (self.min_y + self.max_y) // 2, self.paddle_speed,
                                      self.paddle_r_size, self.paddle_size)

        self.ball = Ball.Ball((self.min_x + self.max_x) // 2, (self.min_y + self.max_y) // 2,
                              self.ball_speed, self.ball_speed, self.ball_size)

        self.collision_calculator = CollisionCalculator.CollisionCalculator(self.min_x, self.min_y, self.max_x,
                                                                            self.max_y, self.paddle_1, self.paddle_2,
                                                                            self.ball, self)

    def update(self, player_1_move: str, player_2_move: str):
        # no logic just mistake
        self.paddle_1.make_move(player_2_move)
        self.paddle_2.make_move(player_1_move)
        self.ball.make_move()
        self.collision_calculator.all_collision_check()

    def update_wall_game(self, player_1_move: str, player_2_move: str, ai_number):
        self.paddle_1.make_move(player_2_move)
        self.paddle_2.make_move(player_1_move)
        self.ball.make_move()
        self.collision_calculator.all_collision_check_wall(ai_number)

    def paddle_1_pos(self):
        return [self.paddle_1.pos_x, self.paddle_1.pos_y]

    def paddle_2_pos(self):
        return [self.paddle_2.pos_x, self.paddle_2.pos_y]

    def ball_pos(self):
        return [int(self.ball.pos_x), int(self.ball.pos_y)]

    def get_score(self, player_nr):
        if player_nr == 1:
            self.player_1_score += 1
        if player_nr == 2:
            self.player_2_score += 1
        self.restart_ball()

    def restart_ball(self):
        side = 1
        if self.ball.speed_x < 0:
            side = -1
        self.ball.pos_x = (self.min_x + self.max_x) // 2
        self.ball.pos_y = (self.min_y + self.max_y) // 2
        self.make_ball_random()
        self.ball.speed_x = side * self.ball.speed_x

    def make_ball_random(self):
        rand_number = random.random()
        x = (self.ball_speed // 2) * rand_number + 2 * self.ball_speed // 3
        y = (self.ball_speed ** 2 - x ** 2) ** (1 / 2)
        self.ball.speed_x = abs(x)
        rand_number_2 = random.random()
        if rand_number_2 > 0.5:
            self.ball.speed_y = y
        else:
            self.ball.speed_y = -y

    def give_info_for_net_1(self):
        return [(self.ball.pos_x - self.paddle_2.pos_x) // 50, (self.ball.pos_y - self.paddle_2.pos_y) // 50,
                self.ball.speed_x,
                self.ball.speed_y, self.ball.pos_x // 50,
                self.ball.pos_y // 50, 1]

    def give_info_for_net_2(self):
        return [(self.ball.pos_x - self.paddle_1.pos_x) // 50, (self.ball.pos_y - self.paddle_1.pos_y) // 50,
                self.ball.speed_x,
                self.ball.speed_y, self.ball.pos_x // 50,
                self.ball.pos_y // 50, -1]

    def give_info_for_net_1_v2(self):
        return [abs(self.ball.pos_x - self.paddle_2.pos_x) // 50, (self.ball.pos_y - self.paddle_2.pos_y) // 50,
                abs(self.ball.speed_x),
                self.ball.speed_y, self.paddle_2.pos_y // 50,
                self.ball.pos_y // 50, 0]

    def give_info_for_net_2_v2(self):
        return [abs(self.ball.pos_x - self.paddle_1.pos_x) // 50, (self.ball.pos_y - self.paddle_1.pos_y) // 50,
                abs(self.ball.speed_x),
                self.ball.speed_y, self.paddle_1.pos_y // 50,
                self.ball.pos_y // 50, 0]

    def restart(self, setting: SettingGame.SettingGame):
        self.HEIGHT = setting.HEIGHT
        self.WIDTH = setting.WIDTH
        self.paddle_speed = setting.paddle_speed
        self.ball_speed = setting.ball_speed
        self.ball_size = setting.ball_size
        self.paddle_size = setting.paddle_size
        self.paddle_r_size = setting.paddle_r_size
        self.max_duration_game = setting.max_game_duration
        self.max_score = setting.max_score
        self.ai_number = setting.ai_number
        self.random_reflection = setting.random_reflection

        self.min_x = setting.LEFT_TOP_CORNER[0]
        self.min_y = setting.LEFT_TOP_CORNER[1]
        self.max_x = setting.RIGHT_BOT_CORNER[0]
        self.max_y = setting.RIGHT_BOT_CORNER[1]

        self.player_1_score = 0
        self.player_2_score = 0

        self.paddle_1 = Paddle.Paddle(self.min_x + 50, (self.min_y + self.max_y) // 2, self.paddle_speed,
                                      self.paddle_r_size, self.paddle_size)
        self.paddle_2 = Paddle.Paddle(self.max_x - 50, (self.min_y + self.max_y) // 2, self.paddle_speed,
                                      self.paddle_r_size, self.paddle_size)

        self.ball = Ball.Ball((self.min_x + self.max_x) // 2, (self.min_y + self.max_y) // 2,
                              self.ball_speed, self.ball_speed, self.ball_size)

        self.collision_calculator = CollisionCalculator.CollisionCalculator(self.min_x, self.min_y, self.max_x,
                                                                            self.max_y, self.paddle_1, self.paddle_2,
                                                                            self.ball, self)
