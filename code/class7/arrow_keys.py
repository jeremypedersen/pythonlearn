# A simple program to demonstrate using the arrow
# keys in Pygame
# 
# Based on code from Al Sweigart's book: https://inventwithpython.com/pygame/
#
# Author: Jeremy Pedersen
#
# Licensed under the Simplified BSD (2-clause) License
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 5 # frames per second setting
fpsClock = pygame.time.Clock()

# Window size
WIDTH = 200
HEIGHT = 150
CENTER_X = 100
CENTER_Y = 75

# set up the window
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Arrow Keys')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# run the game loop
while True:
    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # Check if any of the arrow keys have been pressed
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                pygame.draw.polygon(DISPLAYSURF, RED, ( (CENTER_X-10, CENTER_Y - 10), (CENTER_X-20, CENTER_Y), (CENTER_X-10, CENTER_Y+10) ))
            if event.key == K_RIGHT:
                pygame.draw.polygon(DISPLAYSURF, RED, ( (CENTER_X+10, CENTER_Y-10), (CENTER_X+20, CENTER_Y), (CENTER_X+10, CENTER_Y+10) ))
            if event.key == K_UP:
                pygame.draw.polygon(DISPLAYSURF, RED, ( (CENTER_X-10, CENTER_Y-10), (CENTER_X, CENTER_Y-20), (CENTER_X+10, CENTER_Y-10) ))
            if event.key == K_DOWN:
                pygame.draw.polygon(DISPLAYSURF, RED, ( (CENTER_X-10, CENTER_Y+10), (CENTER_X, CENTER_Y+20), (CENTER_X+10, CENTER_Y+10) ))

    pygame.display.update()
    fpsClock.tick(FPS)