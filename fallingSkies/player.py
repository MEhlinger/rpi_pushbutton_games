# Class for the player

import pygame

class Player:
    def __init__(self, surface, playerSize, xPosition, yPosition, playerColor, display_width):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.playerSize = playerSize
        self.playerColor = playerColor
        self.display_width = display_width
        self.surface = surface
        pygame.draw.rect(self.surface, self.playerColor, [self.xPosition, self.yPosition, self.playerSize, self.playerSize])

    def getPlayerSize(self):
        return self.playerSize

    def getPlayerX(self):
        return self.xPosition

    def getPlayerY(self):
        return self.yPosition

    def redrawPlayer(self, newXPosition):
        self.xPosition = newXPosition
        pygame.draw.rect(self.surface, self.playerColor, [self.xPosition, self.yPosition, self.playerSize, self.playerSize])

    def isOverLeftBound(self):
        if self.xPosition <= 0:
            return True
        else:
            return False

    def isOverRightBound(self):
        if self.xPosition >= self.display_width - self.playerSize:
            return True
        else:
            return False
