from Classes import Block


class ImageBlock():
    def __init__(self,image,x,y,color,location):
        self.image = image
        self.x = x
        self.y = y
        self.rect = image.get_rect()
        self.color = color
        self.rect.left,self.rect.right = location