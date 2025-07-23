import pygame, sys
from pyvidplayer import Video

pygame.init()

WIDTH, HEIGHT = 1920, 1009

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The tower of power")

vid = Video(r"C:\Users\seanr\Documents\Programming\School\Assignments\Game\Video.mp4")
vid.set_size((WIDTH, HEIGHT))

def PROCEDURE_CUTSCENE():
    while True:
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                PROCEDURE_MAINGAME()

def PROCEDURE_MAINGAME():
    SCREEN.fill((0, 0, 0))
    pygame.display.update()