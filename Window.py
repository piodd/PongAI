import pygame
from game import gamelogic
from game import SettingGame
from graphic import painter
import sys


def eventLisiner():
    global player_1_move
    global player_2_move
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_2_move = "Up"
            elif event.key == pygame.K_s:
                player_2_move = "Down"
            elif event.key == pygame.K_i:
                player_1_move = "Up"
            elif event.key == pygame.K_k:
                player_1_move = "Down"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player_2_move == "Up":
                player_2_move = "Static"
            elif event.key == pygame.K_s and player_2_move == "Down":
                player_2_move = "Static"
            elif event.key == pygame.K_i and player_1_move == "Up":
                player_1_move = "Static"
            elif event.key == pygame.K_k and player_1_move == "Down":
                player_1_move = "Static"


pygame.init()

HEIGHT = 800
WIDTH = 1200

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

pygame.display.set_caption("PONG")

playerX = 370
playerY = 480

LEFT_TOP_CORNER = (40, 40)
LEFT_BOT_CORNER = (40, HEIGHT - 40)
RIGHT_TOP_CORNER = (WIDTH - 40, 40)
RIGHT_BOT_CORNER = (WIDTH - 40, HEIGHT - 40)
setting_game = SettingGame.SettingGame(WIDTH, HEIGHT, LEFT_TOP_CORNER, LEFT_BOT_CORNER, RIGHT_TOP_CORNER,
                                       RIGHT_BOT_CORNER)
game = gamelogic.Game(setting_game)

painter = painter.Painter(screen, game, setting_game)

player_1_move = "STATIC"
player_2_move = "STATIC"

pause = False

clock = pygame.time.Clock()
while running:
    eventLisiner()
    game.update(player_1_move=player_1_move, player_2_move=player_2_move)
    painter.draw_all()
    pygame.display.update()
    clock.tick(120)
