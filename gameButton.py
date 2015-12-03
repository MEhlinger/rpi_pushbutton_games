# Game Button class for menu
# Marshall Ehlinger

import pygame

class gameButton:

	GRAY = [131, 131, 131]
	PINK = [255, 55, 135]
	WHITE = [255, 255, 255]
	BLACK = [0, 0, 0]

	def __init__(self, label, buttonWidth, buttonHeight, importedGameFunction):
		self.label = label
		self.height = buttonHeight
		self.width = buttonWidth
		self.importedGameFunction = importedGameFunction
		self.font = pygame.font.SysFont("monospace", 15)
	def renderButton(self, surface, isSelected, origin_x, origin_y):
		label = self.font.render(self.label, True, self.BLACK)
		if isSelected:
			# pygame.draw.rect(surface, self.PINK, [origin_x, origin_y, self.width, self.height])
			surface.fill(self.PINK,[origin_x, origin_y, self.width, self.height])
		else:
			# pygame.draw.rect(surface, self.GRAY, [origin_x, origin_y, self.width, self.height])
			surface.fill(self.GRAY,[origin_x, origin_y, self.width, self.height])
		surface.blit(label,[origin_x + 5, origin_y + (.3 * self.height)])
	def runGame(self):
		self.importedGameFunction()

