from Classes import Block
import pygame
from urllib.request import urlopen
from io import BytesIO

class ImageBlock():
    def __init__(self,image,x,y,color,location):
        self.image = pygame.image.load(BytesIO(urlopen(image).read()))
        self.x = x
        self.y = y
        self.rect = image.get_rect()
        self.color = color
        self.rect.left,self.rect.right = location