import pygame

from game import gamelogic
from game import SettingGame

from PIL import Image, ImageDraw, ImageOps

RED = (255, 0, 0)
COLOR_PADDLE = (255, 0, 0)
COLOR_BOARD_LINE = (0, 255, 0)
COLOR_BACKGROUND = (100, 0, 100)
COLOR_BALL = (222, 222, 222)


class Painter:
    def __init__(self, SCREEN: pygame.display, game: gamelogic.Game, game_setting: SettingGame.SettingGame):
        self.SCREEN = SCREEN
        self.GAME = game
        self.WIDTH = game_setting.WIDTH
        self.HEIGHT = game_setting.HEIGHT
        self.center_X = game_setting.HEIGHT // 2
        self.center_Y = game_setting.WIDTH // 2

        self.font = pygame.font.SysFont(None, 40)

        self.LEFT_TOP_CORNER = game_setting.LEFT_TOP_CORNER
        self.LEFT_BOT_CORNER = game_setting.LEFT_BOT_CORNER
        self.RIGHT_TOP_CORNER = game_setting.RIGHT_TOP_CORNER
        self.RIGHT_BOT_CORNER = game_setting.RIGHT_BOT_CORNER
        self.paddle_size_x = game_setting.paddle_size
        self.paddle_size_y = 100
        self.paddle_r = game_setting.paddle_r_size
        self.ball_size = game_setting.ball_size

        self.paddle_image_1 = self.create_paddle_py_image(self.paddle_r, 1)
        self.paddle_image_2 = self.create_paddle_py_image(self.paddle_r, 2)
        self.paddle_image_1_size_y = 100
        self.paddle_image_2_size_y = 100
        self.paddle_image_size = 100

    def draw_rect(self, pos_x, pos_y):
        pygame.draw.rect(self.SCREEN, (255, 0, 0,), (100, 100, self.paddle_size_x, self.paddle_size_y))

    def create_paddle_py_image(self, paddle_r, player_nr):
        paddle_image = Image.new("RGBA", (self.paddle_r, self.paddle_r))
        paddle_draw = ImageDraw.Draw(paddle_image)
        paddle_draw.pieslice((0, 0, self.paddle_r, self.paddle_r), 0, 360, fill=COLOR_PADDLE)
        cut = (
            self.paddle_r - self.paddle_r * 0.1 / 2, self.paddle_r // 3, self.paddle_r,
            self.paddle_r - self.paddle_r // 3)
        paddle_image = paddle_image.crop(cut)
        paddle_image = self.resize_image(0.3, paddle_image)
        mode = paddle_image.mode
        size = paddle_image.size
        self.paddle_size_x = size[0]
        self.paddle_image_1_size_y = size[1]
        if player_nr == 2:
            paddle_image = paddle_image.rotate(180)
        data = paddle_image.tobytes()
        paddle_image = pygame.image.fromstring(data, size, mode)
        return paddle_image

    def draw_paddle_1(self, pos):
        self.SCREEN.blit(self.paddle_image_1, (pos[0] - self.paddle_size_x, pos[1] - self.paddle_image_1_size_y // 2))
        # pygame.draw.rect(self.SCREEN, (255, 222, 222), (pos[0], pos[1], 5, 5))

    def draw_paddle_2(self, pos):
        self.SCREEN.blit(self.paddle_image_2, (pos[0], pos[1] - self.paddle_image_1_size_y // 2))
        # pygame.draw.rect(self.SCREEN, (255, 222, 222), (pos[0], pos[1] - 10, 5, 5))
        # pygame.draw.rect(self.SCREEN, (255, 222, 222), (pos[0], pos[1] - 30, 5, 5))
        # pygame.draw.rect(self.SCREEN, (255, 222, 222), (pos[0], pos[1] - 20, 5, 5))
        # pygame.draw.rect(self.SCREEN, (255, 222, 222), (pos[0], pos[1] - 40, 5, 5))
        # pygame.draw.rect(self.SCREEN, (255, 222, 222), (pos[0], pos[1] - 50, 5, 5))

    def resize_image(self, factory, image: Image):
        size = image.size
        new_size = (int(size[0] * factory), int(size[1] * factory))
        image = image.resize(new_size)
        return image

    def draw_background(self):
        self.SCREEN.fill(COLOR_BACKGROUND)

    def draw_board_line(self):
        pygame.draw.line(self.SCREEN, COLOR_BOARD_LINE, self.LEFT_TOP_CORNER, self.RIGHT_TOP_CORNER)
        pygame.draw.line(self.SCREEN, COLOR_BOARD_LINE, self.LEFT_BOT_CORNER, self.RIGHT_BOT_CORNER)
        pygame.draw.line(self.SCREEN, COLOR_BOARD_LINE, self.LEFT_TOP_CORNER, self.LEFT_BOT_CORNER)
        pygame.draw.line(self.SCREEN, COLOR_BOARD_LINE, self.RIGHT_TOP_CORNER, self.RIGHT_BOT_CORNER)

    def draw_ball(self, pos):
        pygame.draw.circle(self.SCREEN, COLOR_BALL, (pos[0], pos[1]),
                           self.ball_size // 2)

    def draw_all(self):
        self.draw_background()
        self.draw_paddle_1(self.GAME.paddle_1_pos())
        self.draw_paddle_2(self.GAME.paddle_2_pos())
        self.draw_board_line()
        self.draw_ball(self.GAME.ball_pos())
        self.draw_score()

    def draw_score(self):
        img3 = self.font.render(str(self.GAME.player_1_score), True, (0, 0, 255))
        img2 = self.font.render(":", True, (0, 0, 255))
        img1 = self.font.render(str(self.GAME.player_2_score), True, (0, 0, 255))
        self.SCREEN.blit(img1, (500 + 80, 10))
        self.SCREEN.blit(img2, (525 + 80, 10))
        self.SCREEN.blit(img3, (540 + 80, 10))
