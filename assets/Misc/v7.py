import pygame, sys
from pyvidplayer import Video
import genBlocks
pygame.init()

WIDTH, HEIGHT = 1900, 1000
SCREENHEIGHT, VALUE = 10000, 9000
PLAYERWIDTH, PLAYERHEIGHT = 36, 100
BLOCKWIDTH = 50

FRAMERATE = 120

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The tower of power")

BG_COLOR = (214, 201, 227)

vid = Video(r"School\Assignments\Game\Video2.mp4")
vid.set_size((WIDTH, HEIGHT))

PLAYER = pygame.image.load(r"School\Assignments\Game\player.jpg")
BG = pygame.image.load(r"School\Assignments\Game\bg2.png")
WL = pygame.image.load(r"School\Assignments\Game\wall2.png")
SIDE = pygame.image.load(r"School\Assignments\Game\side.png")
UP = pygame.image.load(r"School\Assignments\Game\up.png")
DBL = pygame.image.load(r"School\Assignments\Game\dbl.png")
LAVA = pygame.image.load(r"School\Assignments\Game\lava.jpg")

fpsClock = pygame.time.Clock()

array = genBlocks.blocks2()
blocks = array[0]
lava = array[1]

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
    offset = 0
    player_coords = [500, 500]
    player_vertical_velocity = 0
    player_status = 3   # 0: hasnt jumped since ground, 1: air, 2: airjump
    BACKGROUND = pygame.Surface((WIDTH, 1080))
    for i in range(0, 1920, 50):
        for j in range(0, 1080, 50):
            BACKGROUND.blit(BG, (i, j))
    WALL = pygame.Surface((WIDTH, SCREENHEIGHT), pygame.SRCALPHA, 32)
    WALL = WALL.convert_alpha()
    WALL.fill((0, 0, 0, 0))
    for item in blocks:
        WALL.blit(WL, (item[0], item[1]+VALUE))
    for item in lava:
        WALL.blit(LAVA, (item[0], item[1]+VALUE))
    frame=0
    HP = 1000
    while True:
        frame += 1
        if frame == FRAMERATE * 1:
            WALL.blit(SIDE, (600, 725+VALUE))
        elif frame == FRAMERATE * 2:
            WALL.blit(UP, (375, 575+VALUE))
        elif frame == FRAMERATE * 5:
            WALL.blit(DBL, (1000, 200+VALUE))
        if player_coords[1] + offset < 500:
            offset += 2
        elif player_coords[1] + offset > 600:
            offset -= 2
        lr_movement = [True, True]
        for item in lava:
            if True:
                if item[0] <= player_coords[0]+PLAYERWIDTH/2 <= item[0]+BLOCKWIDTH and item[1] <= player_coords[1]+PLAYERHEIGHT <= item[1]+BLOCKWIDTH:
                    HP -= 1
        for item in blocks:
            if True:
                if player_coords[1] < item[1]+BLOCKWIDTH and player_coords[1]+PLAYERHEIGHT > item[1]:
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
        SCREEN.blit(BACKGROUND, (0, 0+offset%50-50))
        SCREEN.blit(WALL, (0, 0+offset-VALUE))
        SCREEN.blit(PLAYER, (player_coords[0], player_coords[1]+offset))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1630, 30, 210, 30))
        pygame.draw.rect(SCREEN, (255, 200, 200), pygame.Rect(1635, 35, 200, 20))
        pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(1635, 35, HP/5, 20))
        pygame.display.flip()
        fpsClock.tick(FRAMERATE)



PROCEDURE_CUTSCENE() 