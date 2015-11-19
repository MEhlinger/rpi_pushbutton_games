# Game Button class for menu
# Marshall Ehlinger

import pygame

class gameButton:

	GRAY = [131, 131, 131]
	PINK = [255, 55, 135]

	def __init__(self, label, buttonWidth, buttonHeight, importedGameFunction):
		self.label = label
		self.height = buttonHeight
		self.width = buttonWidth
		self.importedGameFunction = importedGameFunction
	def renderButton(self, surface, isSelected, origin_x, origin_y):
		if isSelected:
			# pygame.draw.rect(surface, self.PINK, [origin_x, origin_y, self.width, self.height])
			surface.fill(self.PINK,[origin_x, origin_y, self.width, self.height])
		else:
			# pygame.draw.rect(surface, self.GRAY, [origin_x, origin_y, self.width, self.height])
			surface.fill(self.GRAY,[origin_x, origin_y, self.width, self.height])
	def runGame(self):
		self.importedGameFunction()

