import pygame
from pygame import Rect
BLACK = (0,0,0)
class Block(pygame.sprite.Sprite):
    def __init__(self, color, screen, x, y, x0=32, y0=32, isPlayer = False, bg = BLACK, *groups):
        super().__init__(*groups)
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y = y
        self.color = color
        self.shape = Rect(self.x, self.y, self.x0, self.y0)
        self.screen = screen
        self.player = isPlayer
        self.__g = groups
        self.bg = bg
    def updateShape(self):
        self.shape = Rect(self.x,self.y,self.x0,self.y0)
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.shape)
        # pygame.display.flip()
    def update(self, x_speed,y_speed):
        pygame.draw.rect(self.screen,self.bg,self.shape)
        self.x += x_speed
        if self.x < 0 and self.player:
             self.x = 0
        self.y += y_speed
        self.shape = Rect(self.x, self.y, self.x0, self.y0)
        pygame.draw.rect(self.screen,self.color,self.shape)
    def kill(self):
        pygame.draw.rect(self.screen,self.bg,self.shape)
        print(self.groups)
        for i in self.__g:
            print(self.groups)
            if not self.player:
                i.remove(self)