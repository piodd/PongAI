import pygame
from game import gamelogic
from game import SettingGame
from graphic import painter
import sys

from Ai.net import Net
from Ai.net_tournament import Tournament

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


def eventLisiner():
    global player_1_move
    global player_2_move
    global pause
    global running
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                pause = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                running = False


clock = pygame.time.Clock()


def ai_decision(entry_node: [], net: Net):
    decision = net.calculateDecision(enterNode=entry_node)
    return decision


def make_ai_move():
    decision_1 = ai_decision(game.give_info_for_net_1_v2(), ai_player_1)
    decision_2 = ai_decision(game.give_info_for_net_2_v2(), ai_player_2)
    global player_1_move
    global player_2_move
    if decision_1[0] > decision_1[1]:
        player_1_move = "Up"
    elif True:
        player_1_move = "Down"
    else:
        player_1_move = "Static"
    if decision_2[0] > decision_2[1]:
        player_2_move = "Up"
    elif True:
        player_2_move = "Down"
    else:
        player_2_move = "Static"


def make_human_vs_ai_move():
    decision_1 = ai_decision(game.give_info_for_net_1_v2(), ai_player_1)
    global player_1_move
    if decision_1[0] > decision_1[1]:
        player_1_move = "Up"
    elif True:
        player_1_move = "Down"
    else:
        player_1_move = "Static"


def make_ai_move_wall(ai_number):
    global player_1_move
    global player_2_move
    if ai_number == 1:
        decision_1 = ai_decision(game.give_info_for_net_1_v2(), ai_player_1)
        if decision_1[0] > decision_1[1]:
            player_1_move = "Up"
        elif True:
            player_1_move = "Down"
        else:
            player_1_move = "Static"
    elif ai_number == 2:
        decision_2 = ai_decision(game.give_info_for_net_2_v2(), ai_player_2)
        if decision_2[0] > decision_2[1]:
            player_2_move = "Up"
        elif True:
            player_2_move = "Down"
        else:
            player_2_move = "Static"


def make_ai_move_wall_test(ai_number):
    global player_1_move
    global player_2_move
    if ai_number == 1:
        decision_1 = game.give_info_for_net_1_v2()[1]
        print(decision_1)
        if decision_1 < 0:
            player_1_move = "Up"
        elif True:
            player_1_move = "Down"
        else:
            player_1_move = "Static"
    elif ai_number == 2:
        decision_2 = game.give_info_for_net_2_v2()[1]
        if decision_2 < 0:
            player_2_move = "Up"
        elif True:
            player_2_move = "Down"
        else:
            player_2_move = "Static"


def metric_score(score_1, score_2):
    mark1 = 100 * score_1 / (score_2 + 10)
    mark2 = 100 * score_2 / (score_1 + 10)
    print([mark1, mark2])
    return [mark1, mark2]


def metric_score_wall(lose):
    mark = 100 - lose
    return mark


def next_round():
    global tournament
    global ai_player_1
    global ai_player_2
    global next_players
    next_players = tournament.next_pair()
    ai_player_1 = next_players[0].net
    ai_player_2 = next_players[1].net


# ai_player_1 = Net()
# ai_player_2 = Net()


counter = 0
tournament = Tournament(10, 10)
next_players = tournament.next_pair()
ai_player_1 = next_players[0].net
ai_player_2 = next_players[1].net
max_time = 1000 * 10 * 2 // 2
time_counter = 0
mark = [0, 0]


# number 1 ==left
# number 2 = right
# left is right ,right is left (mistake) so this is a reason why game.update_wall_game ai_number=1  => make_ai_move=2
def play_vs_wall():
    global time_counter
    global counter
    global mark
    while running:
        eventLisiner()
        make_ai_move_wall_test(2)
        game.update_wall_game(player_1_move=player_1_move, player_2_move=player_2_move, ai_number=1)
        if counter >= 100 * 2 or pause:
            painter.draw_all()
            pygame.display.update()
            counter = 0
        if time_counter > max_time:
            mark = metric_score_wall(game.player_2_score)
            next_players[0] = mark
            time_counter = 0
            next_round()
            game.restart(setting=setting_game)
        time_counter += 1
        counter += 1
        if pause:
            clock.tick(240)


def play_ai_vs_ai():
    global time_counter
    global counter
    global mark
    while running:
        eventLisiner()
        make_ai_move()
        game.update(player_1_move=player_1_move, player_2_move=player_2_move)
        if counter >= 100 * 2 or pause:
            painter.draw_all()
            pygame.display.update()
            counter = 0
        if time_counter > max_time:
            mark = metric_score(game.player_1_score, game.player_2_score)
            next_players[0].score += mark[0]
            next_players[1].score += mark[1]
            time_counter = 0
            next_round()
            game.restart(setting=setting_game)
        time_counter += 1
        counter += 1
        if pause:
            clock.tick(240)


def play_human_vs_ai():
    global time_counter
    global counter
    global mark
    global running
    print("human vs ai")
    running = True
    game.restart(setting=setting_game)
    while running:
        make_human_vs_ai_move()
        eventLisiner()
        game.update(player_1_move=player_1_move, player_2_move=player_2_move)
        painter.draw_all()
        pygame.display.update()
        clock.tick(120)



play_ai_vs_ai()
print("skonczylo sie ai vs ai")

play_human_vs_ai()
