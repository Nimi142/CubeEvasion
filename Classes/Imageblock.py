from Classes import Block
import io
import pygame
from urllib.request import urlopen


class ImageBlock:
    def __init__(self, image_url,location, bg, powerup):
        image_str = urlopen(image_url).read()
        # create a file object (stream)
        image_file = io.BytesIO(image_str)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.bg = bg
        self.powerUp = powerup
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def updatePos(self):
        pass
