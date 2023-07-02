import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_LEFT, K_UP, K_RIGHT, K_ESCAPE

pygame.init()

FPS = pygame.time.Clock()

DISP_HEIGHT = 800
DISP_WIDTH = 1200

MAP_WIDTH = 2500
MAP_HEIGHT = 2500

FONT = pygame.font.SysFont('Arial', 20)

COLOR_PLAYER = (255, 255, 255)
SIZE_PLAYER = (20, 20)
COLOR_BG = (10, 10, 10)

main_display = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT))


class MovObject:
    def __init__(self, speed):
        self.move_down = [0, speed]
        self.move_up = [0, -speed]
        self.move_left = [-speed, 0]
        self.move_right = [speed, 0]
        pass


player_move = MovObject(speed=4)

player = pygame.Surface(SIZE_PLAYER)
player.fill(COLOR_PLAYER)
player_rect = player.get_rect()
score = 0
playing = True


while playing:
    FPS.tick(120)
    main_display.fill(COLOR_BG)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    keys = pygame.key.get_pressed()
    if keys[K_DOWN] and player_rect.bottom <= DISP_HEIGHT:
        player_rect = player_rect.move(player_move.move_down)
    if keys[K_UP] and player_rect.top > -1:
        player_rect = player_rect.move(player_move.move_up)
    if keys[K_LEFT] and player_rect.left > -1:
        player_rect = player_rect.move(player_move.move_left)
    if keys[K_RIGHT] and player_rect.right <= DISP_WIDTH:
        player_rect = player_rect.move(player_move.move_right)

    main_display.blit(player, player_rect)
    main_display.blit(FONT.render(str(score), True,
                      COLOR_PLAYER), (DISP_WIDTH-50, 20))

    if keys[K_ESCAPE]:
        break
    pygame.display.flip()
    print(player_rect.center)
