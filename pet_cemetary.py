#
# PET CEMETARY
# A Virtual Pet Game 
# With Python 2.7 / Pygame
# Marshall Ehlinger
# 10-30-15
#

import sys, pygame, time
import pushbutton
import ghost, food, house

def main():

	FRAMERATE = 60
	DEBOUNCE = 0.05
	clock = pygame.time.Clock()

	pygame.init()
	size = width, height = 320, 240
	black = 0, 0, 0
	white = 255, 255, 255

	RUNNING = True	#'constant' to keep loops running

	button24 = pushbutton.PushButton(24)
	button25 = pushbutton.PushButton(25)

	ghostPet = ghost.Ghost()
	eatableFood = food.Food((width/4)*3, (height/4)*3)
	hauntableHouse = house.House(width/4, (height/4)*3)

	speed = [1,1]

	screen = pygame.display.set_mode(size)

	ghostImg = pygame.image.load("assets/ghost00.bmp")
	ghostRect = ghostImg.get_rect()
	foodImg = pygame.image.load("assets/food.bmp")
	foodRect = foodImg.get_rect()
	houseImg = pygame.image.load("assets/house.bmp")
	houseRect = houseImg.get_rect()


	while RUNNING: 
		clock.tick(FRAMERATE)

		# If block with collision logic for both items
		#if () and ():

		if button24.isPressed() and (button24.timeElapsedSinceLastPress() > DEBOUNCE):
			food.setEaten(False)
			button24.setLastPressToNow()

		if button25.isPressed() and (button25.timeElapsedSinceLastPress() > DEBOUNCE):
			house.setHaunted(False)	
			button25.setLastPressToNow()

		for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

		ghostRect = ghostRect.move(speed)

		if ghostRect.left < 0 or ghostRect.right > width:
			speed[0] = -speed[0]
		if ghostRect.top < 0 or ghostRect.bottom > height:
			speed[1] = -speed[1]
			
		screen.fill(black)
		screen.blit(ghostImg, ghostRect)
		# If not eaten or haunted, blit the items
		pygame.display.flip()

def pseudorandomNewSpeed():
	newSpeed = random.randrange(-2,2)
	return (random.randrange(-2, 2), random.randrange(-2, 2))

if __name__ == "__main__":
	main()
