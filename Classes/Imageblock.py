from Classes import Block
import pygame
from urllib.request import urlopen
from Classes.Block import Block
from io import BytesIO

class ImageBlock():
    def __init__(self, image, x, y, location):
        self.image = pygame.image.load(BytesIO(urlopen(image).read()))
        self.resize()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def resize(self):
        self.image = pygame.transform.scale(self.image,(32,32))