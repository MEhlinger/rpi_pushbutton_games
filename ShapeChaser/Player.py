#player object

import pygame 


class Player():
    def __init__(self, xPos, yPos, surface, sideLength):
        self.xPos = xPos
        self.yPos = yPos
        self.color = (0, 0, 255)
        self.sideLength = sideLength
        self.surface = surface
        pygame.draw.rect(surface, self.color, [150, 150, self.sideLength, self.sideLength], 0)


    def moveUp(self, speed):
        if self.yPos - speed <= 0:
            return
        else:
            self.yPos -= speed

    def moveDown(self, speed):
        if self.yPos + speed >= self.surface.get_height() - self.sideLength:
            return
        else:
            self.yPos += speed

    def moveLeft(self, speed):
        if self.xPos - speed <=0:
            return
        else:
            self.xPos -= speed

    def moveRight(self, speed):
        if self.xPos + speed >= self.surface.get_width()- self.sideLength:
            return
        else:
            self.xPos += speed

    def redraw(self):
        pygame.draw.rect(self.surface, self.color,[self.xPos, self.yPos, self.sideLength, self.sideLength],0)

