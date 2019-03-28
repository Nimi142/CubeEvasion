from Classes import Block
<<<<<<< HEAD
<<<<<<< HEAD
import pygame
from urllib.request import urlopen
from Classes.Block import Block
from io import BytesIO
BLACK = (0,0,0)
class ImageBlock():
    def __init__(self, image, job, x, y, bg,location):
<<<<<<< HEAD
=======
=======
>>>>>>> parent of d621110... asyerert


class ImageBlock():
    def __init__(self,image,x,y,color,location):
<<<<<<< HEAD
>>>>>>> parent of d621110... asyerert
=======
>>>>>>> parent of d621110... asyerert
        self.image = image
=======
        self.image = pygame.image.load(BytesIO(urlopen(image).read()))
>>>>>>> parent of 28463f7... Started testing of slow blocks powerup
        self.x = x
        self.y = y
        self.resize()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.job = 1
        self.bg = bg
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def resize(self):
        self.image = pygame.transform.scale(self.image,(self.x,self.y))
    def update(self,screen,x_speed,y_speed):
        screen.fill(BLACK,self.rect)
        self.rect.left += x_speed
        self.rect.top += y_speed
        screen.blit(self.image,self.rect)