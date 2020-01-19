import pygame, sys
from pygame.locals import *


pygame.init()

res = (1200, 600)

pygame.mixer.music.load('blue_sky.mp3')
pygame.mixer.music.play(-1)

DISPLAYSURF = pygame.display.set_mode(res)
pygame.display.set_caption('Math Dash')

clock = pygame.time.Clock()
player_token = pygame.image.load('player_token.png')

def player(x,y):
    DISPLAYSURF.blit(player_token, (x,y))

x = (res[0] * .15)
y = (res[1] * .75)

while True: # main game loop 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    player(x, y)

    pygame.display.update()
    clock.tick(60)
