#EnemyBlock, by Francis King

import pygame, random

class Enemy():
    def __init__(self, surface):
        self.xPos = random.randint(0,320)
        self.yPos = random.randint(0,240)
        self.sideLength = 20
        self.color = (255, 0, 0)
        self.surface = surface
        self.isHit = False
        pygame.draw.rect(self.surface, self.color, [self.xPos, self.yPos, self.sideLength, self.sideLength], 0)


    def redraw(self):
        pygame.draw.rect(self.surface, self.color, [self.xPos, self.yPos, self.sideLength, self.sideLength], 0)

    def checkIfPlayerTouched(self, player):
        if self.xPos < player.xPos + player.sideLength and self.xPos + self.sideLength > player.xPos and self.yPos < player.yPos + player.sideLength and self.yPos + self.sideLength > player.yPos:
            self.isHit = True
            player.sideLength -= 10