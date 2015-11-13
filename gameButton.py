# Game Button class for menu
# Marshall Ehlinger

import pygame

class gameButton:
	def __init__(self, label, buttonWidth, buttonHeight):
		self.label = label
		self.buttonHeight = buttonHeight
		self.buttonWidth = buttonWidth
	def renderButton(self, surface, color, isSelected, origin_x, origin_y):
		if isSelected:
			pygame.draw.rect(surface, color, [origin_x, origin_y, self.buttonWidth, self.buttonHeight])
		else:
			pygame.draw.rect(surface, [131, 131, 131], [origin_x, origin_y, self.buttonWidth, self.buttonHeight])
