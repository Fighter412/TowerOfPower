import pygame, random, genBlocks, numpy
from pyvidplayer import Video

pygame.init()

WIDTH, HEIGHT = 1900, 1000
SCREENHEIGHT, VALUE = 10000, 9000
PLAYERWIDTH, PLAYERHEIGHT = 66, 96
BLOCKWIDTH = 50

FRAMERATE = 60

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The tower of power")

BG_COLOR = (214, 201, 227)

vid = Video(r"Assets\Video2.mp4")
vid.set_size((WIDTH, HEIGHT))

PLAYER = pygame.image.load(r"player.png")
BG = pygame.image.load(r"Assets\Others\bg2.png")
WL = pygame.image.load(r"Assets\Others\wall2.png")
SIDE = pygame.image.load(r"Assets\Others\side.png")
UP = pygame.image.load(r"Assets\Others\up.png")
DBL = pygame.image.load(r"Assets\Others\dbl.png")
LAVA = pygame.image.load(r"Assets\Others\lava.jpg")
DED = pygame.image.load(r"Assets\Others\ded.jpg")
CTRL = pygame.image.load(r"Assets\Others\controls.png")
ADVA = pygame.image.load(r"Assets\Others\advanced.png")
SELECT = pygame.image.load(r"Assets\Others\select.png")
HEART = pygame.image.load(r"Assets\Others\heart.png")
spider = pygame.image.load(r"Assets\Others\spider.jpg")
SWORDimg = pygame.image.load(r"Assets\Others\sword.png")
TRACK = pygame.mixer.Sound(r"Sounds\track.mp3")
JUMP = pygame.mixer.Sound(r"Sounds\jump.mp3")
DIE = pygame.mixer.Sound(r"Sounds\die.mp3")
SPIDER = pygame.mixer.Sound(r"Sounds\spider.mp3")
DMG = pygame.mixer.Sound(r"Sounds\dmg.mp3")
DAGGER = pygame.mixer.Sound(r"Sounds\dagger.mp3")
SWORD = pygame.mixer.Sound(r"Sounds\sword.mp3")
fpsClock = pygame.time.Clock()

array = genBlocks.blocks2()
blocks = array[0]
lava = array[1]

status = ["IDLE_F", "IDLE_R", "IDLE_L", "WALK_R", "WALK_L","180_R_D", "180_L_U","180_L_D", "180_R_U","540_L", "540_R","DAG_R", "DAG_L","A_IDLE_R", "A_IDLE_L", "A_WALK_R", "A_WALK_L"]
frames = [8, 8, 8, 8, 8, 6, 6, 6, 6, 10, 10, 2, 2, 8, 8, 8, 8]
colors = ["BLUE", "GREEN", "FOREST", "RED", "TERRACOTTA", "BROWN", "ORANGE", "CREAM"]
avatars = []
avatar_no = 0
RED = (255, 0, 0)
PINK = (254, 204, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORSRGB = [(0,152,220), (51,152,75), (139,172,15), (234,50,60), (191,111,74), (200,239,216), (255,173,99), (255,219,162)]
COLORSRGBL = [(196,237,255), (209,152,75), (238,249,195), (250,214,216), (242,226,218), (244,233,216), (255,238,223), (254,247,236)]   


for i in colors:
    tmp = []
    for j in range(len(status)):
        tmp2 = []
        for k in range(frames[j]):
            tmp2.append(pygame.image.load(r"Assets\avatars\\"+str(i)+"\\"+status[j]+"_"+str(k)+".PNG"))
        tmp.append(tmp2)
    avatars.append(tmp)

def PROCEDURE_CUTSCENE():
    while True:
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                PROCEDURE_SELECT_AVATAR()
            if event.type == pygame.QUIT: 
                pygame.quit()

def PROCEDURE_SELECT_AVATAR():
    global avatar_no
    BACKGROUND = pygame.Surface((WIDTH, 1080))
    for i in range(0, 1920, 50):
        for j in range(0, 1080, 50):
            BACKGROUND.blit(BG, (i, j))
    BACKGROUND.blit(SELECT, (170, 300))
    BACKGROUND.blit(SELECT, (616, 300))
    BACKGROUND.blit(SELECT, (1042, 300))
    BACKGROUND.blit(SELECT, (1478, 300))
    BACKGROUND.blit(SELECT, (170, 700))
    BACKGROUND.blit(SELECT, (606, 700))
    BACKGROUND.blit(SELECT, (1042, 700))
    BACKGROUND.blit(SELECT, (1478, 700))
    while True:
        for i in range(len(avatars[0])):
            for j in range(frames[i]):
                SCREEN.blit(BACKGROUND, (0, 0))
                SCREEN.blit(avatars[0][i][j], (200, 100))
                SCREEN.blit(avatars[1][i][j], (636, 100))
                SCREEN.blit(avatars[2][i][j], (1072, 100))
                SCREEN.blit(avatars[3][i][j], (1508, 100))
                SCREEN.blit(avatars[4][i][j], (200, 500))
                SCREEN.blit(avatars[5][i][j], (636, 500))
                SCREEN.blit(avatars[6][i][j], (1072, 500))
                SCREEN.blit(avatars[7][i][j], (1508, 500))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        mouse = pygame.mouse.get_pos()
                        if 300 <= mouse[1] <= 384:
                            if 170 <= mouse[0] <= 422:
                                avatar_no = 0
                                PROCEDURE_MAINGAME()
                            elif 616 <= mouse[0] <= 868:
                                avatar_no = 1
                                PROCEDURE_MAINGAME()
                            elif 1042 <= mouse[0] <= 1294:
                                avatar_no = 2
                                PROCEDURE_MAINGAME()
                            elif 1478 <= mouse[0] <= 1730:
                                avatar_no = 3
                                PROCEDURE_MAINGAME()
                        elif 700 <= mouse[1] <= 784:
                            if 170 <= mouse[0] <= 422:
                                avatar_no = 4
                                PROCEDURE_MAINGAME()
                            elif 616 <= mouse[0] <= 868:
                                avatar_no = 5
                                PROCEDURE_MAINGAME()
                            elif 1042 <= mouse[0] <= 1294:
                                avatar_no = 6
                                PROCEDURE_MAINGAME()
                            elif 1478 <= mouse[0] <= 1730:
                                avatar_no = 7
                                PROCEDURE_MAINGAME()
                fpsClock.tick(10)

def PROCEDURE_MAINGAME():
    offset = 0
    player_coords = [500, 500]#[1700, -4000]
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
    WALL.blit(SWORDimg, (900, 800-4100+VALUE))
    frame=0
    HP = 200
    alive = True
    idlewalk = ["IDLE_F", 0]
    alternative = False
    access_level = 0
    blitted = False
    dag_L = True
    reload = [0, 0, 0] # Dagger 180 540
    attack_color = [True, True, True]
    maxspiders = 0
    spiders = []
    radius = 500
    play = True
    TRACK.play()
    while True:
        print(player_coords)
        lava_dmg = False
        frame += 1
        if access_level == 0 and player_coords[1] <= 350:
            access_level = 1
            blitted = False
        elif access_level == 1 and player_coords[1] <= -1100:
            access_level = 2
            maxspiders = 5
            blitted = False
        elif access_level == 2 and player_coords[1] <= -3150:
            access_level = 3
            maxspiders = 20
            blitted = False
        if len(spiders) < maxspiders and access_level >= 2:
            if random.randint(1, 120) == 1:
                x = random.randint(int(player_coords[0]+PLAYERWIDTH/2-radius), int(player_coords[0]+PLAYERWIDTH/2+radius))
                y = random.randint(int(player_coords[1]+PLAYERHEIGHT/2-radius), int(player_coords[1]+PLAYERHEIGHT/2+radius))
                if x*x + y*y >= 300:
                    spiders.append([x ,y])
        if HP <= 0:
            hp = 0
            alive = False
            TRACK.stop()
            SCREEN.blit(DED, (0, 250))
            if play:
                DIE.play()
                play = False
        if frame == FRAMERATE * 1:
            WALL.blit(SIDE, (600, 725+VALUE))
        elif frame == FRAMERATE * 2:
            WALL.blit(UP, (375, 575+VALUE))
        elif access_level == 1 and not blitted:
            WALL.blit(DBL, (1000, 200+VALUE))
            blitted = True
        elif access_level == 2 and not blitted:
            WALL.blit(CTRL, (1000, 800-2000+VALUE))
            blitted = True
        elif access_level == 3 and not blitted:
            WALL.blit(ADVA, (1150, 800-4200+VALUE))
            blitted = True
        if player_coords[1] + offset < 500:
            offset += 5
        elif player_coords[1] + offset > 600:
            offset -= 5
        lr_movement = [True, True]
        if reload[0] > 0:
            reload[0] -= 5
        if reload[1] > 0:
            reload[1] -= 5
        if reload[2] > 0:
            reload[2] -= 1
        for item in lava:
            if True:
                corners = [[player_coords[0]+1, player_coords[1]+1], [player_coords[0]+PLAYERWIDTH-1, player_coords[1]+1], [player_coords[0]+PLAYERWIDTH-1, player_coords[1]+PLAYERHEIGHT-1], [player_coords[0]+1, player_coords[1]+PLAYERHEIGHT-1], [player_coords[0]+PLAYERWIDTH/2, player_coords[1]+PLAYERHEIGHT/2]]
                for corner in corners:
                    if not lava_dmg and alive and item[0] < corner[0] < item[0]+BLOCKWIDTH and item[1] < corner[1] < item[1]+BLOCKWIDTH:
                        HP -= 1
                        lava_dmg = True
        for item in blocks:
            if True:
                if player_coords[1] < item[1]+BLOCKWIDTH and player_coords[1]+PLAYERHEIGHT > item[1]:
                    if player_coords[0] == item[0]+BLOCKWIDTH or player_coords[0]-2 == item[0]+BLOCKWIDTH:
                        lr_movement[0] = False
                    elif player_coords[0]+PLAYERWIDTH == item[0] or player_coords[0]+PLAYERWIDTH+2 == item[0]:
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
            if event.type == pygame.KEYDOWN and alive:
                if event.key == pygame.K_SPACE and (player_status < 2 and access_level > 0 or player_status == 0 and access_level == 0):
                    player_vertical_velocity = -11.5
                    player_status += 1
                    #JUMP.play()
            if event.type == pygame.QUIT: 
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and keys[pygame.K_d] and lr_movement[0] and alive:
            idlewalk[0] = "IDLE_F"
        elif keys[pygame.K_a] and lr_movement[0] and alive:
            idlewalk[0] = "WALK_L"
            player_coords[0] -= 4
        elif keys[pygame.K_d] and lr_movement[1] and alive:
            idlewalk[0] = "WALK_R"
            player_coords[0] += 4
        else:
            idlewalk[0] = "IDLE_F"
        if keys[pygame.K_s] and not alternative and access_level >= 2 and reload[0] == 0:
            if dag_L:
                alternative = ["DAG_L", 0, 2*6]
                dag_L = False
                attack_color[0] = False
            else:
                alternative = ["DAG_R", 0, 2*6]
                dag_L = True
                attack_color[0] = True
            DAGGER.play()
            reload[0] = 200
            lowest = [10000, 0]
            for item in spiders:
                AX, AY = item[0], item[1]
                BX, BY = player_coords[0]+PLAYERWIDTH/2, player_coords[1]+PLAYERHEIGHT/2
                totalDistance = numpy.sqrt(numpy.square(AX-BX)+numpy.square(AY-BY))
                if totalDistance < lowest[0]:
                    lowest[0] = totalDistance
                    lowest[1] = item
            print(lowest)
            if lowest[0] <= 100:
                spiders.remove(lowest[1])
                SPIDER.play()
        if not alternative and access_level == 3:
            if keys[pygame.K_q] and reload[1] == 0:
                alternative = ["180_L_D", 0, 6*6]
                attack_color[1] = not attack_color[1]
                reload[1] = 200
                SWORD.play()
            if keys[pygame.K_e] and reload[1] == 0:
                alternative = ["180_R_D", 0, 6*6]
                attack_color[1] = not attack_color[1]
                reload[1] = 200
                SWORD.play()
            if keys[pygame.K_z] and reload[2] == 0:
                alternative = ["540_L", 0, 10*6]
                attack_color[2] = not attack_color[2]
                reload[2] = 200
                SWORD.play()
            if keys[pygame.K_c] and reload[2] == 0:
                alternative = ["540_R", 0, 10*6]
                attack_color[2] = not attack_color[2]
                reload[2] = 200
                SWORD.play()
        player_coords[1] += player_vertical_velocity
        player_vertical_velocity += 0.2
        SCREEN.blit(BACKGROUND, (0, 0+offset%50-50))
        SCREEN.blit(WALL, (0, 0+offset-VALUE))
        if not alternative:
            SCREEN.blit(avatars[avatar_no][status.index(idlewalk[0])][idlewalk[1]//6], (player_coords[0]-63, player_coords[1]+offset-42))
            idlewalk[1] = (idlewalk[1]+1)%48
        else:
            SCREEN.blit(avatars[avatar_no][status.index(alternative[0])][alternative[1]//6], (player_coords[0]-63, player_coords[1]+offset-42))
            alternative[1] = alternative[1]+1
            if alternative[1] == alternative[2]:
                alternative = False
        #pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1630, 30, 210, 30))
        #pygame.draw.rect(SCREEN, (255, 200, 200), pygame.Rect(1635, 35, 200, 20))
        #pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(1635, 35, HP/5, 20))
        pygame.draw.polygon(SCREEN, BLACK, [(1560, 30), (1774, 30), (1794, 60), (1580, 60)])
        pygame.draw.polygon(SCREEN, PINK, [(1570, 35), (1770, 35), (1784, 55), (1584, 55)])
        pygame.draw.polygon(SCREEN, RED, [(1570, 35), (1570+HP, 35), (1584+HP, 55), (1584, 55)])
        SCREEN.blit(HEART, (1750, 0))
        if access_level >= 2:
            if reload [0] == 0: tmp = reload[0]
            else: tmp = reload[0]
            pygame.draw.polygon(SCREEN, BLACK, [(1560, 130), (1774, 130), (1794, 160), (1580, 160)])
            pygame.draw.polygon(SCREEN, WHITE, [(1570, 135), (1770, 135), (1784, 155), (1584, 155)])
            if attack_color[0]:
                tmp2 = COLORSRGB[avatar_no]
                tmp3 = COLORSRGBL[avatar_no]
            else:
                tmp2 = COLORSRGBL[avatar_no]
                tmp3 = COLORSRGB[avatar_no]
            pygame.draw.polygon(SCREEN, tmp3, [(1570, 135), (1570+200, 135), (1584+200, 155), (1584, 155)])
            pygame.draw.polygon(SCREEN, tmp2, [(1570, 135), (1570+tmp, 135), (1584+tmp, 155), (1584, 155)])
            SCREEN.blit(avatars[avatar_no][status.index("DAG_L")][1], (1693, 48))
            if access_level == 3:
                tmp = reload[2]
                pygame.draw.polygon(SCREEN, BLACK, [(1560, 330), (1774, 330), (1794, 360), (1580, 360)])
                pygame.draw.polygon(SCREEN, WHITE, [(1570, 335), (1770, 335), (1784, 355), (1584, 355)])
                if attack_color[2]:
                    tmp2 = COLORSRGB[avatar_no]
                    tmp3 = COLORSRGBL[avatar_no]
                else:
                    tmp2 = COLORSRGBL[avatar_no]
                    tmp3 = COLORSRGB[avatar_no]
                pygame.draw.polygon(SCREEN, tmp3, [(1570, 335), (1570+200, 335), (1584+200, 355), (1584, 355)])
                pygame.draw.polygon(SCREEN, tmp2, [(1570, 335), (1570+tmp, 335), (1584+tmp, 355), (1584, 355)])
                SCREEN.blit(avatars[avatar_no][status.index("540_R")][4], (1693, 248))

                tmp = reload[1]
                pygame.draw.polygon(SCREEN, BLACK, [(1560, 230), (1774, 230), (1794, 260), (1580, 260)])
                pygame.draw.polygon(SCREEN, WHITE, [(1570, 235), (1770, 235), (1784, 255), (1584, 255)])
                if attack_color[1]:
                    tmp2 = COLORSRGB[avatar_no]
                    tmp3 = COLORSRGBL[avatar_no]
                else:
                    tmp2 = COLORSRGBL[avatar_no]
                    tmp3 = COLORSRGB[avatar_no]
                pygame.draw.polygon(SCREEN, tmp3, [(1570, 235), (1570+200, 235), (1584+200, 255), (1584, 255)])
                pygame.draw.polygon(SCREEN, tmp2, [(1570, 235), (1570+tmp, 235), (1584+tmp, 255), (1584, 255)])
                SCREEN.blit(avatars[avatar_no][status.index("180_L_D")][2], (1693, 148))
        
            print(spiders)
        for item in spiders:
            AX, AY = item[0], item[1]
            BX, BY = player_coords[0]+PLAYERWIDTH/2, player_coords[1]+PLAYERHEIGHT/2
            totalDistance = numpy.sqrt(numpy.square(AX-BX)+numpy.square(AY-BY))
            if totalDistance <= 20:
                HP -= 10
                DMG.play()
                spiders.remove(item)
            elif random.randint(1, 50) == 1:
                if totalDistance < 50:
                    targetDistance = totalDistance
                else:
                    targetDistance = 50

                ratio = targetDistance / totalDistance

                diffX = BX - AX
                diffY = BY - AY

                targetX = AX + (ratio * diffX)
                targetY = AY + (ratio * diffY)
                item[0] = targetX
                item[1] = targetY
            SCREEN.blit(spider, (item[0]-15, item[1]-15+offset))
        pygame.display.flip()
        fpsClock.tick(FRAMERATE)


PROCEDURE_CUTSCENE() 