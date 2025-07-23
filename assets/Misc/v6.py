import pygame, sys
from pyvidplayer import Video
import genBlocks
pygame.init()

WIDTH, HEIGHT = 1900, 1000
PLAYERWIDTH, PLAYERHEIGHT = 36, 100
BLOCKWIDTH = 50

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The tower of power")

BG_COLOR = (214, 201, 227)

vid = Video(r"School\Assignments\Game\Video2.mp4")
vid.set_size((WIDTH, HEIGHT))

PLAYER = pygame.image.load(r"School\Assignments\Game\player.jpg")
BG = pygame.image.load(r"School\Assignments\Game\bg2.png")
WL = pygame.image.load(r"School\Assignments\Game\wall2.png")
fpsClock = pygame.time.Clock()

blocks = genBlocks.blocks()

def PROCEDURE_CUTSCENE():
    while True:
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                PROCEDURE_MAINGAME()
            if event.type == pygame.QUIT: 
                pygame.quit()


def PROCEDURE_MAINGAME():
    global offset
    offset = [0, 0]
    player_coords = [500, 500]
    player_vertical_velocity = 0
    player_status = 3   # 0: hasnt jumped since ground, 1: air, 2: airjump
    BACKGROUND = pygame.Surface((WIDTH, HEIGHT))
    for i in range(0, 1920, 50):
        for j in range(0, 1080, 50):
            BACKGROUND.blit(BG, (i, j))
    WALL = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
    WALL = WALL.convert_alpha()
    WALL.fill((0, 0, 0, 0))
    for item in blocks:
        WALL.blit(WL, (item[0], item[1]))
    while True:
        lr_movement = [True, True]
        for item in blocks:
            if True:
                if player_coords[1] < item[1]+BLOCKWIDTH and player_coords[1] > item[1]:
                    if player_coords[0] == item[0]+BLOCKWIDTH:
                        lr_movement[0] = False
                    elif player_coords[0]+PLAYERWIDTH == item[0]:
                        lr_movement[1] = False
                if player_coords[0]+PLAYERWIDTH > item[0] and player_coords[0] < item[0]+BLOCKWIDTH:
                    if player_coords[1] <= item[1]+BLOCKWIDTH and player_coords[1] > item[1]:
                        player_coords[1] = item[1]+BLOCKWIDTH+1
                        player_vertical_velocity = 0
                    if player_coords[1]+PLAYERHEIGHT >= item[1] and player_coords[1] < item[1]+BLOCKWIDTH:
                        player_status = 0
                        player_vertical_velocity = 0
                        player_coords[1] = item[1]-PLAYERHEIGHT
                        print(player_coords, item)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_status < 2:
                    player_vertical_velocity -= 8/(player_status+1)
                    player_status += 1
            if event.type == pygame.QUIT: 
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and lr_movement[0]:
            player_coords[0] -= 2
        if keys[pygame.K_d] and lr_movement[1]:
            player_coords[0] += 2
        player_coords[1] += player_vertical_velocity
        player_vertical_velocity += 0.1
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(WALL, (0, 0))
        SCREEN.blit(PLAYER, (player_coords[0], player_coords[1]))
        pygame.display.flip()
        fpsClock.tick(60)



PROCEDURE_CUTSCENE() 