# A simple program to demonstrate mouse events
# in PyGame
# 
# Based on code from Al Sweigart's book: https://inventwithpython.com/pygame/
#
# Author: Jeremy Pedersen
#
# Licensed under the Simplified BSD (2-clause) License
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            catx, caty = event.pos

    pygame.display.update()
    fpsClock.tick(FPS)