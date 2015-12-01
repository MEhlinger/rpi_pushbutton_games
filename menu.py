#
# Raspberry Pi Pygame
# MAIN MENU
# Marshall Ehlinger
# Fall 2015
#

import pygame, sys
import gameButton
from pet_cemetary.pet_cemetary import main as petCemetaryGame
from fallingSkies.fallingSkies import main as fallingSkiesGame

def mainMenu():
	FRAMERATE = 60
	DEBOUNCE = 0.05
	BTN_WIDTH = 100
	BTN_HEIGHT = 50
	TITLECARD_HEIGHT = 50

	size = width, height = 320, 240
	clock = pygame.time.Clock()

	pygame.init()

	font = pygame.font.SysFont("monospace", 14)

	screen = pygame.display.set_mode(size)

	buttons = []
	selection = 0 # As index in buttons

	petCemetary_btn = gameButton.gameButton("Pet Cemetary", BTN_WIDTH, BTN_HEIGHT, petCemetaryGame)
	buttons.append(petCemetary_btn)

	fallingSkies_btn = gameButton.gameButton("Falling Skies", BTN_WIDTH, BTN_HEIGHT, fallingSkiesGame)
	buttons.append(fallingSkies_btn)

	spaceInvaded_btn = gameButton.gameButton("Space Invaded", BTN_WIDTH, BTN_HEIGHT, petCemetaryGame)
	buttons.append(spaceInvaded_btn)

	gameFour_btn = gameButton.gameButton("GAMEFORE", BTN_WIDTH, BTN_HEIGHT, petCemetaryGame)
	buttons.append(gameFour_btn)

	RUNNING = True

	while RUNNING:
		clock.tick(FRAMERATE)

		for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
					elif event.key == pygame.K_UP:
						if selection != 0:
							selection -= 1
						else:
							selection = len(buttons) - 1
					elif event.key == pygame.K_DOWN:
						if selection != len(buttons) - 1:
							selection += 1
						else:
							selection = 0
					elif event.key == pygame.K_RETURN:
						buttons[selection].runGame()

		screen.fill([0,0,0])

		for i in range (0, len(buttons)):
			if i == selection:
				buttons[i].renderButton(screen, True, (width/2 - buttons[i].width/2), ((height - TITLECARD_HEIGHT)/len(buttons) + (BTN_HEIGHT * i)))
			else:
				buttons[i].renderButton(screen, False, (width/2 - buttons[i].width/2), ((height - TITLECARD_HEIGHT)/len(buttons) + (BTN_HEIGHT * i)))
		
		pygame.display.flip()


if __name__=="__main__":
	mainMenu()	
