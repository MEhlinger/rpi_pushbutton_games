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
	timer = 0 

	pygame.init()
	size = width, height = 320, 240
	black = 0, 0, 0
	white = 255, 255, 255
	gray = 131, 131, 131

	RUNNING = True	#'constant' to keep loops running

	button24 = pushbutton.PushButton(24)
	button25 = pushbutton.PushButton(25)

	ghostPet = ghost.Ghost()
	eatableFood = food.Food(width/2, (height/4)*3)
	hauntableHouse = house.House(width/5, (height/4)*3)

	speed = [1,1]

	screen = pygame.display.set_mode(size)

	# Ghost images
	neutralNeutral = pygame.image.load("assets/neutralneutral.bmp")
	neutralSad = pygame.image.load("assets/neutralsad.bmp")
	neutralHappy = pygame.image.load("assets/neutralhappy.bmp")
	skinnySad = pygame.image.load("assets/skinnysad.bmp")
	skinnyHappy = pygame.image.load("assets/skinnyhappy.bmp")
	fatSad = pygame.image.load("assets/fatsad.bmp")
	fatHappy = pygame.image.load("assets/fathappy.bmp")

	ghostRect = neutralNeutral.get_rect()
	foodImg = pygame.image.load("assets/food.bmp")
	foodRect = foodImg.get_rect()
	houseImg = pygame.image.load("assets/house.bmp")
	houseRect = houseImg.get_rect()

	houseRect.x = hauntableHouse.getX()
	houseRect.y = hauntableHouse.getY()

	foodRect.x = eatableFood.getX()
	foodRect.y = eatableFood.getY()


	while RUNNING: 
		clock.tick(FRAMERATE)

		timer += 1
		if (timer >= FRAMERATE * 30):
			ghostPet.depleteDrives()
			timer = 0

		if ghostRect.colliderect(foodRect) and not eatableFood.isEaten():
			ghostPet.adjustNourishment(10)	
			eatableFood.setEaten(True)
		if ghostRect.colliderect(houseRect) and not hauntableHouse.isHaunted():
			ghostPet.adjustHappiness(10)
			hauntableHouse.setHaunted(True)


		if button24.isPressed() and (button24.timeElapsedSinceLastPress() > DEBOUNCE):
			eatableFood.setEaten(False)
			button24.setLastPressToNow()
		if button25.isPressed() and (button25.timeElapsedSinceLastPress() > DEBOUNCE):
			hauntableHouse.setHaunted(False)	
			button25.setLastPressToNow()


		for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()

		ghostRect = ghostRect.move(speed)

		if ghostRect.left < 0 or ghostRect.right > width:
			speed[0] = -speed[0]
		if ghostRect.top < 0 or ghostRect.bottom > height:
			speed[1] = -speed[1]
			
		screen.fill(gray)

		happy = ghostPet.getHappiness()
		nourish = ghostPet.getNourishment()

		# Replace this godawful block with a function, maybe switch
		if happy > 50 and nourish > 60:
			currentGhostImg = fatHappy
		elif happy > 50 and nourish <= 60 and nourish >= 40:
			currentGhostImg = neutralHappy
		elif happy > 50 and nourish < 40:
			currentGhostImg = skinnyHappy
		elif happy < 60 and happy > 40 and nourish <= 60 and nourish >= 40:
			currentGhostImg = neutralNeutral
		elif happy < 50 and nourish > 60:
			currentGhostImg = fatSad
		elif happy < 50 and nourish < 40:
			currentGhostImg = skinnySad
		elif happy <= 60 and nourish <= 60 and nourish >= 40:
			currentGhostImg = neutralSad

		screen.blit(currentGhostImg, ghostRect)

		if not eatableFood.isEaten():
			screen.blit(foodImg, foodRect)
		if not hauntableHouse.isHaunted():
			screen.blit(houseImg, houseRect)
		pygame.display.flip()

if __name__ == "__main__":
	main()
