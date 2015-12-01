# Class for the falling sky chunks

import pygame

class SkyChunk:
    def __init__(self, surface, chunkSize, xCoordinate, yCoordinate, chunkColor, fallSpeed, score, height, objectList):
        self.chunkSize = chunkSize
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.chunkColor = chunkColor
        self.fallSpeed = fallSpeed
        self.score = 0
        self.surface = surface
        self.height = height
        self.objectList = objectList

    def fall(self):
        self.yCoordinate += self.fallSpeed
        pygame.draw.rect(self.surface, self.chunkColor, [self.xCoordinate, self.yCoordinate, self.chunkSize, self.chunkSize])
        if self.yCoordinate > self.height:
            self.objectList.remove(self)
            self.score += 100

    def returnScore(self):
        return self.score

    def collideWithPlayer(self, objectX, objectY, objectSize):
        if self.yCoordinate + self.chunkSize >= objectY and self.yCoordinate <= objectY + objectSize:
            if self.xCoordinate >= objectX and self.xCoordinate + self.chunkSize <= objectX + objectSize:
                return True
        if self.yCoordinate + self.chunkSize >= objectY and self.yCoordinate <= objectY + objectSize:
            if self.xCoordinate <= objectX + objectSize and self.xCoordinate + self.chunkSize >= objectX:
                return True
        else:
            return False
