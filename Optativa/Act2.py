import pygame
from math import floor
from copy import deepcopy

WIDTH = 600
HEIGHT = 600
NTILES = 13
WIDTHT = int(WIDTH/(NTILES+2))
HEIGHTT = int(HEIGHT/(NTILES+2))
TIMES = 60*2

time = 0
tiles = [[0 for i in range(NTILES)] for j in range(NTILES)]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
start = 0

imgtiles = []

pygame.display.set_caption('Actividad 2')

tileb = pygame.image.load("Tileb.png")
tileb = pygame.transform.scale(tileb, (WIDTHT, HEIGHTT))

for i in range(NTILES*NTILES):
    try:
        tilew = pygame.image.load("Fotos/" + str(i) + ".png")
    except:
        tilew = pygame.image.load("Tilew.png")

    tilew = pygame.transform.scale(tilew, (WIDTHT, HEIGHTT))
    imgtiles.append(tilew)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if start == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                ph = floor(event.pos[0]/int(WIDTH/NTILES))
                pw = floor(event.pos[1]/int(HEIGHT/NTILES))
                if tiles[pw][ph] == 0:
                    tiles[pw][ph] = 1
                else:
                    tiles[pw][ph] = 0
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    start = 1

    screen.fill((85, 85, 85))

    if time == 0 and start == 1:
        time = TIMES;
        next_tiles = deepcopy(tiles)
        for i in range(NTILES):
            for j in range(NTILES):
                if i == 0 and j != NTILES-1:
                    suma = tiles[i+1][j] + tiles[i][j+1] + tiles[i][j-1] + tiles[i+1][j+1] + tiles[i+1][j-1]
                elif i == 0 and j == NTILES-1:
                    suma = tiles[i+1][j] + tiles[i][j-1] + tiles[i+1][j-1]
                elif i == NTILES-1 and j != NTILES-1:
                    suma = tiles[i-1][j] + tiles[i][j+1] + tiles[i][j-1] + tiles[i-1][j+1] + tiles[i-1][j-1]
                elif i == NTILES-1 and j == NTILES-1:
                    suma = tiles[i-1][j] + tiles[i][j-1] + tiles[i-1][j-1]
                elif j == 0 and i != NTILES-1:
                    suma = tiles[i+1][j] + tiles[i-1][j] + tiles[i][j+1] + tiles[i+1][j+1] + tiles[i-1][j+1]
                elif j == 0 and i == NTILES-1:
                    suma = tiles[i-1][j] + tiles[i][j+1] + tiles[i-1][j+1]
                elif j == NTILES-1 and i != NTILES-1:
                    suma = tiles[i+1][j] + tiles[i-1][j] + tiles[i][j-1] + tiles[i+1][j-1] + tiles[i-1][j-1]
                else:
                    suma = tiles[i+1][j] + tiles[i-1][j] + tiles[i][j+1] + tiles[i][j-1] + tiles[i+1][j+1] + tiles[i+1][j-1] + tiles[i-1][j+1] + tiles[i-1][j-1]
                if tiles[i][j] == 1:
                    if suma == 2 or suma == 3:
                        next_tiles[i][j] = 1
                    else:
                        next_tiles[i][j] = 0
                elif tiles[i][j] == 0:
                    if suma == 3:
                        next_tiles[i][j] = 1
        tiles = deepcopy(next_tiles)
    elif start == 1:
        time -= 1

    k = 0
    for i in range(NTILES):
        for j in range(NTILES):
            if tiles[i][j] == 1:
                screen.blit(imgtiles[k], ((int(WIDTH/NTILES)*j) + int(((WIDTH/NTILES)-WIDTHT)/2), (int(HEIGHT/NTILES)*i) + int(((HEIGHT/NTILES)-HEIGHTT)/2)))
            else:
                screen.blit(tileb, ((int(WIDTH/NTILES)*j) + int(((WIDTH/NTILES)-WIDTHT)/2), (int(HEIGHT/NTILES)*i) + int(((HEIGHT/NTILES)-HEIGHTT)/2)))
            k += 1

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
