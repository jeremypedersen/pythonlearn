# Bubble Pop
# 
# A simple game: avoid the red bubbles and stay alive! 
# eat blue bubbles to get bigger!
#
# Author: Jeremy Pedersen
#
# Licensed under the Simplified BSD (2-clause) License
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

# Set clock speed
FPS = 60
fpsClock = pygame.time.Clock()

# Set up screen
WIDTH = 400
HEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubble Pop')

# Define game colors and sprites
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

# Set up game constants
PLAYER_X = 50
PLAYER_Y = 50
PLAYER_R = 10 # Radius of player bubble

RADIUS = 5 # Radius of food/enemy bubbles
BLUE_CIRCLES = 10
RED_CIRCLES = 50

# Test if any two circles are touching
def circleTouching(circleA, circleB):
    dist = ((circleB['x'] - circleA['x'])**2 + (circleB['y'] - circleA['y'])**2)**(1/2)
    
    if dist > (circleA['r'] + circleB['r']):
        return False
    else:
        return True
    
# Make a list of new circles
def makeCircles(color, r, number):
    circles = []
    for _ in range(0, number):
        x = randint(10, WIDTH-10)
        y = randint(10, HEIGHT-10)
        circles.append({'x': x, 'y': y, 'r':r, 'color': color})
    return circles

# Draw circles (from a list) onto the screen
def drawCircles(circles):
    for circle in circles:
        pygame.draw.circle(DISPLAYSURF, circle['color'], (circle['x'], circle['y']), circle['r'], 0)

# Make text on the screen
def makeText(text, size, x, y, textcolor, bgcolor):
    fontObj = pygame.font.Font('freesansbold.ttf', size)
    textSurfaceObj = fontObj.render(text, True, textcolor, bgcolor)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x, y)
    
    return textSurfaceObj, textRectObj

# Move circles towards/away from player
def moveCircles(playerCircle, circles):
    i = randint(0,len(circles)-1)

    if circles[i]['color'] == RED:
        if playerCircle['x'] > circles[i]['x']:
            circles[i]['x'] += randint(0,2)
        else:
            circles[i]['x'] += randint(-2,0)
        
        if playerCircle['y'] > circles[i]['y']:
            circles[i]['y'] += randint(0,2)
        else:
            circles[i]['y'] += randint(-2,0)
    else:
        if playerCircle['x'] > circles[i]['x']:
            circles[i]['x'] -= randint(0,2)
        else:
            circles[i]['x'] -= randint(-2,0)
 
        if playerCircle['y'] > circles[i]['y']:
            circles[i]['y'] -= randint(0,2)
        else:
            circles[i]['y'] -= randint(-2,0)
    
    if circles[i]['x'] > WIDTH or circles[i]['x'] < 0:
        del circles[i]
    elif circles[i]['y'] > HEIGHT or circles[i]['y'] < 0:
        del circles[i]

# Set up the game!
def initGame():

    playerCircle = {'x': PLAYER_X, 'y': PLAYER_Y, 'r': PLAYER_R, 'color': GREEN}

    blueCircles = makeCircles(BLUE, RADIUS, BLUE_CIRCLES)
    redCircles = makeCircles(RED, RADIUS, RED_CIRCLES)

    return playerCircle, blueCircles, redCircles

# Check if the player's circle is touching any of the blue
# or red circles, and makes the circle bigger or smaller depending
# on what type of circle has been touched
def checkAllCircles(player, circleList):
    for circle in circleList:
        if circleTouching(player, circle):
            if circle['color'] == RED:
                player['r'] -= 5
            elif circle['color'] == BLUE:
                player['r'] += 5
            circleList.remove(circle)

playerCircle, blueCircles, redCircles = initGame()

# Main game loop - check for user clicking 'X' on window
# if user has clicked the 'X', then kill the program
winning = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            playerCircle['x'] = event.pos[0]
            playerCircle['y'] = event.pos[1]
        if event.type == MOUSEBUTTONUP:
            # If we are currently playing
            if winning:
                playerCircle['r'] -= 5 # Make circle smaller
            else:
                mousex, mousey = event.pos
                if quitRect.collidepoint(mousex,mousey):
                    pygame.quit()
                    sys.exit()
                elif restartRect.collidepoint(mousex,mousey):
                    playerCircle, blueCircles, redCircles = initGame()
                    winning = True
                    continue
                
        if event.type == KEYUP:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
            elif event.key == K_r:
                playerCircle, blueCircles, redCircles = initGame()
                winning = True # Set winning state to true again

    if winning:   
        DISPLAYSURF.fill(WHITE)
        
        moveCircles(playerCircle, blueCircles)
        moveCircles(playerCircle, redCircles)
     
        checkAllCircles(playerCircle, blueCircles)
        checkAllCircles(playerCircle, redCircles)
    
        # Replace red circles as needed
        if len(redCircles) < RED_CIRCLES:
            redCircles.extend(makeCircles(RED, RADIUS, RED_CIRCLES-len(redCircles)))

        # Replace blue circles as needed
        if len(blueCircles) < BLUE_CIRCLES:
            blueCircles.extend(makeCircles(BLUE, RADIUS, BLUE_CIRCLES-len(blueCircles)))
        
        # Draw all the blue and red circles on the screen (combine lists first)
        drawCircles(blueCircles+redCircles)      
    
        if playerCircle['r'] < 5:
            loseSurf, loseRect = makeText("YOU LOSE", 72, WIDTH/2, HEIGHT/2, RED, BLUE)
            DISPLAYSURF.blit(loseSurf,loseRect)
            
            # Draw quit and restart buttons
            quitSurf, quitRect = makeText("QUIT", 32, 0, 0, RED, BLUE)
            quitRect.right = WIDTH
            quitRect.bottom = HEIGHT
            
            DISPLAYSURF.blit(quitSurf,quitRect)
            
            restartSurf, restartRect = makeText("RESTART", 32, 0, 0, RED, BLUE)
            restartRect.left = 0
            restartRect.bottom = HEIGHT
            
            DISPLAYSURF.blit(restartSurf,restartRect)
                        
            winning = False
        else:
            drawCircles([playerCircle])
    
    pygame.display.update()
    
    fpsClock.tick(FPS)
