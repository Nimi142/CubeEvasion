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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,153)
GREEN = (0,255,0)
PLAYER_SPEED = 4
SCROLL_SPEED = 4
r = random.randint(0,1000)
random.seed(r)
def makeCol(x,amountCols):
    newBlocks = []
    blockPlacements = []
    for j in range(0,amountCols):
        if j%2 == 0:
            ry = random.randint(0,10)
            rx = random.randint(x,x+amountCols)
            if ry != 0:
                blockPlacements.append((rx,ry))
    for i in range(0,len(blockPlacements)):
        newBlocks.append(Block(BLUE,screen,blockPlacements[i][0]*32,blockPlacements[i][1]*32))
    return newBlocks
def restart():
    global player
    global player2
    global blocks
    global running
    global isDead
    global start
    global counter
    global r
    global SCROLL_SPEED
    global players
    global score
    score = 0
    SCROLL_SPEED = 4
    r = random.randint(0,1000)
    random.seed(r)
    counter = 0
    start = time()
    screen = pygame.display.set_mode((800, TOTAL_H))
    screen.fill(BLACK)
    blocks = []
    players = []
    player = Block(RED, screen, 0, 32, 28, 28, True,players)
    if isPlayerTwo:
        player2 = Block(GREEN, screen, 0, 32, 28, 28, True,players)
        players.append(player2)
    players.append(player)
    running = True
    isDead = False
    upBlue.draw(screen)
    downBlue.draw(screen)


failFont = pygame.font.SysFont('Arial', 52)
tFailed = failFont.render('GAME OVER!', True, (255, 0, 0))
TOTAL_H = 384
TOTAL_W = 2048
screen = pygame.display.set_mode((800, TOTAL_H))
players = []
player = Block(RED, screen, 0,32,28,28,True,players)
player2 = Block(GREEN,screen,0,32,28,28,True,players)
players.append(player)
print(player.groups())
isPlayerTwo = False
running = True
isDead = False
start = time()
time_since_change = 0
blocks = []
upBlue = Block(BLUE,screen, 0,0,TOTAL_W)
downBlue = Block(BLUE,screen, 0,TOTAL_H - 32,TOTAL_W)
upBlue.draw(screen)
downBlue.draw(screen)
timefont = pygame.font.SysFont('Consolas', 13)
counter = 0
score = 0
while running:
    keys = pygame.key.get_pressed()
    player.draw(screen)
    SCROLL_SPEED += 0.001
    pygame.time.delay(16)
    if not isDead:
        if counter % 64 == 0:
            blocks.extend(makeCol(33,8))
        upBlue.draw(screen)
        tScore = timefont.render("Score: " + str(round(score,0)), True, RED)
        tTime = timefont.render("seed: "+str(r) + ", Scroll Speed: "+ str(round(SCROLL_SPEED,3)) + ", Time: " + str(round(time()-start,3)) , True, (255, 0, 0))
        screen.blit(tTime,(10,10))
        screen.blit(tScore,(600,10))
        for i in blocks:
            i.update(-SCROLL_SPEED,0)
            if i.x == -32:
                blocks.remove(i)
            for j in players:
                if (i.shape.colliderect(j.shape)  or upBlue.shape.colliderect(j.shape) or downBlue.shape.colliderect(j.shape)):
                    screen.blit(tFailed,(200,150))
                    isDead = True
        pygame.display.flip()
        if keys[pygame.K_UP]:
            player.update(0,-PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            player.update(0,PLAYER_SPEED)
        if keys[pygame.K_RIGHT]:
            player.update(PLAYER_SPEED,0)
        if keys[pygame.K_LEFT]:
            player.update(-PLAYER_SPEED,0)
        if pygame.key.get_pressed()[pygame.K_p] and time() - time_since_change > 1:
            time_since_change = time()
            if isPlayerTwo:
                print(players)
                isPlayerTwo = False
                # players.remove(player2)
                player2.kill()
            else:
                print(players)
                player2.x = 0
                player2.y = 32
                player2.updateShape()
                player2.draw(screen)
                isPlayerTwo = True
                players.append(player2)
        if isPlayerTwo and not isDead:
            player2.draw(screen)
            if keys[pygame.K_w]:
                player2.update(0, -PLAYER_SPEED)
            if keys[pygame.K_s]:
                player2.update(0, PLAYER_SPEED)
            if keys[pygame.K_d]:
                player2.update(PLAYER_SPEED, 0)
            if keys[pygame.K_a]:
                player2.update(-PLAYER_SPEED, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE]:
        restart()
    if not isDead:
        counter += 1
        score += len(blocks)/10

