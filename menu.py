#
# Raspberry Pi Pygame
# MAIN MENU
# Marshall Ehlinger
# 11-13-15
#

import pygame
import gameButton
from pet_cemetary.pet_cemetary import main as petCemetary

def mainMenu():
	FRAMERATE = 60
	DEBOUNCE = 0.05
	PINK = 255, 55, 135
	GRAY = 131, 131, 131
	size = width, height = 320, 240
	clock = pygame.time.Clock()

	pygame.init()

	font = pygame.font.SysFont("monospace", 14)

	RUNNING = True


	screen = pygame.display.set_mode(size)

	buttons = []

	petCemetary_btn = gameButton.gameButton("Pet Cemetary", 100, 50)
	buttons.append(petCemetary_btn)
	petCemetary_btn_rect = petCemetary_btn.renderButton(screen, PINK, False, 100, 100)

	while RUNNING:
		clock.tick(FRAMERATE)

		for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
		# Listen for input
		# Potentially change what is selected,
		# or load the chosen game
		
		pygame.display.flip()


if __name__=="__main__":
	mainMenu()	
