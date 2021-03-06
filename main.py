import random
from base64 import b64decode
from io import BytesIO
from time import time

from Classes.Block import Block
from Classes.ImageBackGround import *
from Classes.myCheckbox import *

GRAY = (63, 63, 63)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 153)
GREEN = (0, 255, 0)
PLAYER_SPEED = 4
pPlayer_SPEED = 4
SCROLL_SPEED = 4
pSCROLL_SPEED = 4
r = random.randint(0, 1000)
random.seed(r)
pygame.init()
main = Tk()
seedWindow = Toplevel()
controlsWindow = Toplevel()
colorWindow = Toplevel()
colorPicker = Toplevel()
colorChange = 0
image64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA" \
          "7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuNWRHWFIAAABOSURBVEhL7ZYhDgAgDAOreQb//yOQlARXtU6QXs7M9" \
          "OzQwQCmwTN7OYeDN9sXWEWSBIQkASFJQEgSEJIEhCQBIUlASL4M1NIYsD+/RoANprRM50WVCWoAAAAASUVORK5CYII="
logo = BytesIO(b64decode(image64))
logo = pygame.image.load(logo)
pygame.display.set_caption("Cube Evasion")
pygame.display.set_icon(logo)
main.title("Cube Evasion: Settings")
seedWindow.title("Cube Evasion: Seed")
controlsWindow.title("Cube Evasion: Controls")
colorWindow.title("Cube Evasion: Colors")
colorPicker.title("Cube Evasion: Color picker")
configs = {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT,
           "player2": pygame.K_p, "restart": pygame.K_SPACE, "pause": pygame.K_r, "settings": pygame.K_BACKQUOTE,
           "2up": pygame.K_w,
           "2down": pygame.K_s, "2left": pygame.K_a, "2right": pygame.K_d, "3up": pygame.K_y,
           "3down": pygame.K_h, "3left": pygame.K_g, "3right": pygame.K_j}
# "4up":pygame.K_w,"4down":pygame.K_s,"4left":pygame.K_a,"4right":pygame.K_d
colors = {"player": (127, 127, 255), "player2": (255, 127, 127), "player3": (127, 255, 127), "player4": (255, 255, 102),
          "blocks": (127, 127, 127), "bg": BLACK, "up": GRAY, "down": GRAY}
colorKeys = ["player", "player2", "blocks", "bg", "up", "down", "player3", "player4"]
configsKeys = ["up", "down", "left", "right", "player2", "pause", "settings", "2up", "2down", "2left", "2right", "3up",
               "3down", "3left", "3right"]


def color_seed():
    global eSeed
    global r
    global isRandSeed
    isRandSeed = not (randseedCheck.getVar())
    r = int(eSeed.get())
    random.seed(int(eSeed.get()))
    seedWindow.withdraw()


def confirm_controls():
    global listEntries
    global configs
    global configsKeys
    key_list = []
    for i in range(0, len(listEntries)):
        j: str = listEntries[i].get().lower()
        if j is not "":
            if j == "space":
                key_list.append(pygame.K_SPACE)
            elif j == "backquote":
                key_list.append(pygame.K_BACKQUOTE)
            elif j == "up":
                key_list.append(pygame.K_UP)
            elif j == "down":
                key_list.append(pygame.K_DOWN)
            elif j == "left":
                key_list.append(pygame.K_LEFT)
            elif j == "right":
                key_list.append(pygame.K_RIGHT)
            else:
                key_list.append(ord(j))
    for i in range(0, len(key_list)):
        pass
    configs["up"] = key_list[0]
    configs["down"] = key_list[1]
    configs["left"] = key_list[2]
    configs["right"] = key_list[3]
    configs["2up"] = key_list[4]
    configs["2down"] = key_list[5]
    configs["2left"] = key_list[6]
    configs["2right"] = key_list[7]
    configs["player2"] = key_list[8]
    configs["pause"] = key_list[9]
    configs["settings"] = key_list[10]
    configs["restart"] = key_list[11]
    configs["3up"] = key_list[12]
    configs["3down"] = key_list[13]
    configs["3left"] = key_list[14]
    configs["3right"] = key_list[15]
    controlsWindow.withdraw()


def confirm_settings():
    main.withdraw()
    main.quit()
    restart(r)


isRandSeed = True
# Setting main:
bFinishSettings = Button(main, text="Finish", command=confirm_settings)
bToSeed = Button(main, text="open seed window", command=seedWindow.deiconify)
bToControls = Button(main, text="Open controls", command=controlsWindow.deiconify)
bToColor = Button(main, text="Open Color", command=colorWindow.deiconify)
bToSeed.pack()
bToControls.pack()
bToColor.pack()
bFinishSettings.pack()
# Setting Color window:
bChangePlayerColor = Button(colorWindow, text="Change Player Color", command=lambda x=0: set_color_picker(x))
bChangePlayer2Color = Button(colorWindow, text="Change Player2 Color", command=lambda x=1: set_color_picker(x))
bChangeBlocksColor = Button(colorWindow, text="Change Blocks Color", command=lambda x=2: set_color_picker(x))
bChangeUpColor = Button(colorWindow, text="Change Upper Barrier Color", command=lambda x=4: set_color_picker(x))
bChangeDownColor = Button(colorWindow, text="Change Lower Barrier Color", command=lambda x=5: set_color_picker(x))
bChangeBgColor = Button(colorWindow, text="Change Background Color", command=lambda x=3: set_color_picker(x))
bChangePlayerColor.grid(column=0, row=0)
bChangePlayer2Color.grid(column=1, row=0)
bChangeBlocksColor.grid(column=0, row=1)
bChangeBgColor.grid(column=1, row=1)
bChangeUpColor.grid(column=0, row=2)
bChangeDownColor.grid(column=1, row=2)


# 2
def set_color_picker(x):
    global colorChange
    colorChange = x
    colorPicker.deiconify()


def return_color():
    global colors
    global player
    global player2
    global screen
    global blocks
    global colorChange
    a = (int(eR.get()), int(eG.get()), int(eB.get()))
    colorPicker.withdraw()
    colors[colorKeys[colorChange]] = a
    colorPicker.withdraw()
    colorWindow.withdraw()
    if colorChange == 4:
        upBarrier.color = a
    if colorChange == 5:
        downBarrier.color = a


# Setting color picker:
lcpTitle = Label(colorPicker, text="Choose the color: ")
lR = Label(colorPicker, text="R: ")
lG = Label(colorPicker, text="G: ")
lB = Label(colorPicker, text="B: ")
eR = Entry(colorPicker)
eG = Entry(colorPicker)
eB = Entry(colorPicker)
bConfirmColorPicker = Button(colorPicker, text="Confirm", command=return_color)
lcpTitle.grid(column=0, row=0, columnspan=2)
lR.grid(column=0, row=1)
lG.grid(column=0, row=2)
lB.grid(column=0, row=3)
eR.grid(column=1, row=1)
eG.grid(column=1, row=2)
eB.grid(column=1, row=3)
bConfirmColorPicker.grid(column=0, row=4, columnspan=2)
# Setting controls window:
spacer1 = Label(controlsWindow)
spacer2 = Label(controlsWindow)
bconfirm_controls = Button(controlsWindow, text="Confirm", command=confirm_controls)
eUp = Entry(controlsWindow)
eUp.insert(0, "up")
eDown = Entry(controlsWindow)
eDown.insert(0, "down")
eLeft = Entry(controlsWindow)
eLeft.insert(0, "left")
eRight = Entry(controlsWindow)
eRight.insert(0, "right")
e2Up = Entry(controlsWindow)
e2Up.insert(0, "w")
e2Down = Entry(controlsWindow)
e2Down.insert(0, "s")
e2Left = Entry(controlsWindow)
e2Left.insert(0, "a")
e2Right = Entry(controlsWindow)
e2Right.insert(0, "d")
e3Up = Entry(controlsWindow)
e3Up.insert(0, "y")
e3Down = Entry(controlsWindow)
e3Down.insert(0, "h")
e3Left = Entry(controlsWindow)
e3Left.insert(0, "g")
e3Right = Entry(controlsWindow)
e3Right.insert(0, "j")
eChangeP2 = Entry(controlsWindow)
eChangeP2.insert(0, "p")
ePause = Entry(controlsWindow)
ePause.insert(0, "r")
eSettings = Entry(controlsWindow)
eSettings.insert(0, "backquote")
eRestart = Entry(controlsWindow)
eRestart.insert(0, "space")
listEntries = [eUp, eDown, eLeft, eRight, e2Up, e2Down, e2Left, e2Right, eChangeP2, ePause, eSettings, eRestart, e3Up,
               e3Down, e3Left, e3Right]
lPlayer = Label(controlsWindow, text="Player1: ")
lPlayer2 = Label(controlsWindow, text="Player2: ")
lPlayer3 = Label(controlsWindow, text="Player3:")
lUp = Label(controlsWindow, text="Up: ")
lDown = Label(controlsWindow, text="Down: ")
lLeft = Label(controlsWindow, text="Left: ")
lRight = Label(controlsWindow, text="Right: ")
l2Up = Label(controlsWindow, text="Up: ")
l2Down = Label(controlsWindow, text="Down: ")
l2Left = Label(controlsWindow, text="Left: ")
l2Right = Label(controlsWindow, text="Right: ")
l3Up = Label(controlsWindow, text="Up: ")
l3Down = Label(controlsWindow, text="Down: ")
l3Left = Label(controlsWindow, text="Left: ")
l3Right = Label(controlsWindow, text="Right: ")
lChangeP2 = Label(controlsWindow, text="Change players: ")
lPause = Label(controlsWindow, text="Pause: ")
lRestart = Label(controlsWindow, text="Restart")
lSettings = Label(controlsWindow, text="Settings: ")
lPlayer.grid(row=0, column=0)
lUp.grid(row=1, column=0)
lDown.grid(row=2, column=0)
lLeft.grid(row=3, column=0)
lRight.grid(row=4, column=0)
spacer1.grid(row=5, column=0)
lChangeP2.grid(row=6, column=0)
lPause.grid(row=7, column=0)
eUp.grid(row=1, column=1)
eDown.grid(row=2, column=1)
eLeft.grid(row=3, column=1)
eRight.grid(row=4, column=1)
eChangeP2.grid(row=6, column=1)
ePause.grid(row=7, column=1)
lPlayer2.grid(row=0, column=2)
l2Up.grid(row=1, column=2)
l2Down.grid(row=2, column=2)
l2Left.grid(row=3, column=2)
l2Right.grid(row=4, column=2)
spacer1.grid(row=5, column=0)
lSettings.grid(row=6, column=2)
lRestart.grid(row=7, column=2)
e2Up.grid(row=1, column=3)
e2Down.grid(row=2, column=3)
e2Left.grid(row=3, column=3)
e2Right.grid(row=4, column=3)
eSettings.grid(row=6, column=3)
eRestart.grid(row=7, column=3)
bconfirm_controls.grid(column=0, columnspan=4, row=8)
lPlayer3.grid(row=0, column=4)
l3Up.grid(row=1, column=4)
l3Down.grid(row=2, column=4)
l3Left.grid(row=3, column=4)
l3Right.grid(row=4, column=4)
e3Up.grid(row=1, column=5)
e3Down.grid(row=2, column=5)
e3Left.grid(row=3, column=5)
e3Right.grid(row=4, column=5)

# Seed window:
label = Label(seedWindow, text="Enter seed:")
eSeed = Entry(seedWindow)
randseedCheck = mycheckbox(seedWindow, "Randomize seed", True, False)
bSeed = Button(seedWindow, text="confirm", command=color_seed)
label.pack()
eSeed.pack()
randseedCheck.pack()
bSeed.pack()
main.withdraw()
isDebug = False
transition = pygame.display.set_mode((400, 400))
try:
    TransitionImage = pygame.image.load("TransitionLogo.png")
except pygame.error:
    print("NO LOGO!")
else:
    TransitionImage = ImageBackground(TransitionImage, (0, 0))
    TransitionImage.image = pygame.transform.scale(TransitionImage.image, (400, 400))
    transition.fill([255, 255, 255])
    transition.blit(TransitionImage.image, TransitionImage.rect)
    pygame.display.flip()
    tt = time()
    while time() - tt < 3:
        pygame.event.get()


# Define some colors
# An idea for the randomizer, do it in batches and lkimit the number of blocks.

def make_blocks(x, column_amount):
    new_blocks = []
    block_placements = []
    for i in range(0, column_amount):
        if i % 2 == 0:
            ry = random.randint(0, 10)
            rx = random.randint(x, x + column_amount)
            if ry != 0:
                block_placements.append((rx * 32, ry * 32))
    for i in range(0, len(block_placements)):
        new_blocks.append(
            Block(colors["blocks"], screen, block_placements[i][0], block_placements[i][1], 31.99, 31.99, False,
                  colors["bg"]))
    return new_blocks


def pause(pause_screen):
    global SCROLL_SPEED
    global PLAYER_SPEED
    global pSCROLL_SPEED
    global pPlayer_SPEED
    global isPause
    global pauseTime
    pauseTime = time()
    isPause = not isPause
    if isPause:
        pSCROLL_SPEED = SCROLL_SPEED
        pPlayer_SPEED = PLAYER_SPEED
        PLAYER_SPEED = 0
        SCROLL_SPEED = 0
    if not isPause:
        PLAYER_SPEED = pPlayer_SPEED
        SCROLL_SPEED = pSCROLL_SPEED
        pause_screen.fill(colors["bg"])
        downBarrier.draw(pause_screen)


def restart(seed=None):
    global player
    global player2
    global player3
    global player4
    global blocks
    global running
    global isDead
    global start
    global counter
    global r
    global SCROLL_SPEED
    global players
    global score
    global isPause
    global screen
    global isRandSeed
    players = []
    player = Block(colors["player"], screen, 0, 32, 28, 28, True, colors["bg"], players)
    player2 = Block(colors["player2"], screen, 0, 63, 28, 28, True, colors["bg"], players)
    player3 = Block(colors["player3"], screen, 0, 95, 28, 28, True, colors["bg"], players)
    player4 = Block(colors["player4"], screen, 0, 127, 28, 28, True, colors["bg"], players)
    players.append(player)
    if numPlayers > 1:
        players.append(player2)
    if numPlayers > 2:
        players.append(player3)
    if isPause:
        pause(screen)
    score = 0
    SCROLL_SPEED = 4
    if seed is not None:
        r = seed
    elif isRandSeed:
        r = random.randint(0, 1000)
    random.seed(r)
    counter = 0
    start = time()
    screen = pygame.display.set_mode((800, TOTAL_H))
    screen.fill(colors["bg"])
    blocks = []
    running = True
    isDead = False
    upBarrier.draw(screen)
    downBarrier.draw(screen)


numPlayers = 1
pauseTime = 0
failFont = pygame.font.SysFont('Arial', 52)
tFailed = failFont.render('GAME OVER!', True, (255, 0, 0))
TOTAL_H = 384
TOTAL_W = 2048
screen = pygame.display.set_mode((800, TOTAL_H))
players = []
player = Block(colors["player"], screen, 0, 32, 28, 28, True, colors["bg"])
player2 = Block(colors["player2"], screen, 0, 32, 28, 28, True, colors["bg"])
player3 = Block(colors["player3"], screen, 0, 32, 28, 28, True, colors["bg"])
player4 = Block(colors["player4"], screen, 0, 32, 28, 28, True, colors["bg"])
players.append(player)
isPause = False
running = True
isDead = False
start = time()
time_since_change = 0
blocks = []
upBarrier = Block(GRAY, screen, 0, 0, TOTAL_W)
downBarrier = Block(GRAY, screen, 0, TOTAL_H - 32, TOTAL_W)
upBarrier.draw(screen)
downBarrier.draw(screen)
timefont = pygame.font.SysFont('Consolas', 13)
tPause = failFont.render("PAUSE", True, RED)
counter = 0
score = 0
tTime = timefont.render("0", True, RED)
tScore = timefont.render("0", True, RED)

# Run loop:
while running:
    # Blitting "pause" if paused
    if isPause:
        screen.blit(tPause, (200, 150))
    # Getting pressed keys:
    keys = pygame.key.get_pressed()
    player.draw(screen)
    # Accelerating screen:
    if not isPause:
        SCROLL_SPEED += 0.001
    pygame.time.delay(16)
    if not isDead:
        upBarrier.draw(screen)
        screen.blit(tTime, (10, 10))
        screen.blit(tScore, (600, 10))
        # Making new blocks:
        if counter % 64 == 0:
            blocks.extend(make_blocks(33, 8))
        # Drawing upper borders:
        # Changing text of Score and Time and blitting them:
        tScore = timefont.render("Score: " + str(int(score / 500)), True, RED)
        tTime = timefont.render("seed: " + str(r) + ", Scroll Speed: " + str(int(SCROLL_SPEED * 10) / 10), True, RED)
        # Updating position of Blocks:
        for i in blocks:
            i.update(-SCROLL_SPEED, 0)
            if i.x == -32:
                blocks.remove(i)
            # Checking for collisions
            for j in players:
                if (i.shape.colliderect(j.shape)) and not isDebug:
                    screen.blit(tFailed, (200, 150))
                    isDead = True
        # Opening settings if needed
        if keys[configs["settings"]]:
            isPause = True
            screen.blit(tPause, (200, 150))
            main.deiconify()
            seedWindow.withdraw()
            controlsWindow.withdraw()
            colorWindow.withdraw()
            colorPicker.withdraw()
            main.mainloop()
        # Checking for pause and movement:
        if keys[configs["pause"]] and time() - pauseTime > 1:
            pause(screen)
        if keys[configs["up"]]:
            player.update(0, -PLAYER_SPEED)
        if keys[configs["down"]]:
            player.update(0, PLAYER_SPEED)
        if keys[configs["right"]]:
            player.update(PLAYER_SPEED, 0)
        if keys[configs["left"]]:
            player.update(-2 - PLAYER_SPEED, 0)
        # Adding/ Removing Second player:
        if keys[pygame.K_1] and time() - time_since_change > 1 and (not isPause):
            time_since_change = time()
            if player2 in players:
                players.remove(player2)
                player2.kill()
            if player3 in players:
                players.remove(player3)
                player3.kill()
            numPlayers = 1
        if keys[pygame.K_2] and time() - time_since_change > 1 and (not isPause):
            time_since_change = time()
            if numPlayers == 3:
                player3.kill()
                players.remove(player3)
            if numPlayers == 1:
                player2.x = 0
                player2.y = 32
                player2.updateShape()
                player2.draw(screen)
                players.append(player2)
            numPlayers = 2
        if keys[pygame.K_3] and time() - time_since_change > 1 and (not isPause):
            time_since_change = time()
            if numPlayers == 1:
                player2.x = 0
                player2.y = 32
                player2.updateShape()
                player2.draw(screen)
                players.append(player2)
            if numPlayers == 2:
                player3.x = 0
                player3.y = 32
                player3.updateShape()
                player3.draw(screen)
                players.append(player3)
            numPlayers = 3
        if numPlayers > 1 and not isDead:
            # Checking for p2 movement:
            player2.draw(screen)
            if keys[configs["2up"]]:
                player2.update(0, -PLAYER_SPEED)
            if keys[configs["2down"]]:
                player2.update(0, PLAYER_SPEED)
            if keys[configs["2right"]]:
                player2.update(PLAYER_SPEED, 0)
            if keys[configs["2left"]]:
                player2.update(-2 - PLAYER_SPEED, 0)
        if numPlayers > 2 and not isDead:
            player3.draw(screen)
            # Checking for p3 movement
            if keys[configs["3up"]]:
                player3.update(0, -PLAYER_SPEED)
            if keys[configs["3down"]]:
                player3.update(0, 2 + PLAYER_SPEED)
            if keys[configs["3right"]]:
                player3.update(PLAYER_SPEED, 0)
            if keys[configs["3left"]]:
                player3.update(-2 - PLAYER_SPEED, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[configs["restart"]] and not isPause:
        restart()
    if not isDead and not isPause:
        counter += 1
        score += len(blocks)
    pygame.display.flip()
