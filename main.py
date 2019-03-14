import pygame
import random
from time import sleep,time
from Block import Block
from ImageBackGround import *
pygame.init()
isDebug = True
transition = pygame.display.set_mode((400,400))
try:
    TransitionImage = pygame.image.load("TransitionLogo.png")
except:
    print("NO LOGO!")
else:
    TransitionImage = ImageBackground(TransitionImage,(0,0))
    TransitionImage.image = pygame.transform.scale(TransitionImage.image,(400,400))
    transition.fill([255, 255, 255])
    transition.blit(TransitionImage.image, TransitionImage.rect)
    pygame.display.flip()
    tt = time()
    while time() - tt < 3:
        pygame.event.get()

# Define some colors
from pygame.rect import Rect
# An idea for the randomizer, do it in batches and lkimit the number of blocks.
r = random.randint(0,1000)
random.seed(r)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,153)
PLAYER_SPEED = 4
SCROLL_SPEED = 4
def makeRow(x,amountRows = 16):
    newBlocks = []
    blockPlacements = []
    if x < 8 and amountRows != 8:
        amountRows = amountRows-(8-x)
        x = 8
    for j in range(x,x+amountRows):
        if j%2 == 0:
            ry = random.randint(0,10)
            rx = random.randint(x,x+amountRows)
            if ry != 0:
                blockPlacements.append((rx,ry))
    for i in range(0,len(blockPlacements)):
        newBlocks.append(Block(BLUE,screen,blockPlacements[i][0]*32,blockPlacements[i][1]*32))  
    return newBlocks
def restart():
    global player
    global blocks
    global running
    global isDead
    global start
    global counter
    global r
    r = random.randint(0,1000)
    random.seed(r)
    counter = 0
    start = time()
    screen = pygame.display.set_mode((800, TOTAL_H))
    screen.fill(BLACK)
    player = Block(RED, screen, 0, 32)
    running = True
    isDead = False
    x, y = 0, 0
    blocks = makeRow(0,66)
    upBlue.draw(screen)
    downBlue.draw(screen)

# Initialize Pygame
font = pygame.font.SysFont('Arial', 52)
tFailed = font.render('FAILED !', True, (255, 0, 0))
TOTAL_H, TOTAL_W = 384, 2048
screen = pygame.display.set_mode((800, TOTAL_H))
player = Block(RED, screen, 0,32)
x, y = 0, 0
blocks = makeRow(0,66)
# for x in range(1,len(lvl) - 1):
#     for y in range(0,len(lvl[x])):
#         if lvl[x][y] == "#":
#             blocks.append(Block(BLUE, screen, (y)*32,x*32))
clock = pygame.time.Clock()
clock.tick(60)
screen_width = 700
screen_height = 400
running = True
isDead = False
start = time()
upBlue = Block(BLUE,screen, 0,0,TOTAL_W)
downBlue = Block(BLUE,screen, 0,TOTAL_H - 32,TOTAL_W)
upBlue.draw(screen)
downBlue.draw(screen)
timefont = pygame.font.SysFont('Arial', 13)
tTime= timefont.render("Time: " + str(time()-start) + ", seed: "+str(r), True, (255, 0, 0))
counter = 0
while running:
    pygame.time.delay(15)
    for i in blocks:
        pass
    tTime = timefont.render("Time: " + str(time()-start) + ", seed: "+str(r), True, (255, 0, 0))
    screen.blit(tTime,(10,10))
    if counter % 64 == 0 and time()-start > 0.1:
        blocks.extend(makeRow(67,8))
    for i in blocks:
        i.update(-SCROLL_SPEED,0)
        if i.x == 0:
            i.kill()
            blocks.remove(i)
        if (i.shape.colliderect(player.shape)  or upBlue.shape.colliderect(player.shape) or downBlue.shape.colliderect(player.shape))and isDead == False:
            player.kill()
        if (i.shape.colliderect(player.shape)  or upBlue.shape.colliderect(player.shape) or downBlue.shape.colliderect(player.shape)):
            screen.blit(tFailed,(200,150))
            isDead = True
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE]:
        restart()
    if isDead is False:
        if keys[pygame.K_UP]:
            player.update(0,-PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            player.update(0,PLAYER_SPEED)
        if keys[pygame.K_RIGHT]:
            player.update(PLAYER_SPEED,0)
        if keys[pygame.K_LEFT]:
            player.update(-PLAYER_SPEED,0)
    else:
        screen.blit(tFailed, (200, 150))
    upBlue.draw(screen)
    screen.blit(tTime,(10,10))
    pygame.display.flip()
    counter += 1

