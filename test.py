#
# PYGAME TEST
# Python 2.7 / Pygame
# Marshall Ehlinger
# 10-28-15
#

import sys, pygame, time
import pushbutton

def main():

	FRAMERATE = 60
	DEBOUNCE = 0.05
	clock = pygame.time.Clock()

	pygame.init()
	size = width, height = 320, 240
	baseSpeed = 1
	speed = [baseSpeed, baseSpeed]
	black = 0, 0, 0
	white = 255, 255, 255

	RUNNING = True	#'constant' to keep loops running

	button24 = pushbutton.PushButton(24)
	button25 = pushbutton.PushButton(25)

	screen = pygame.display.set_mode(size)
	ball = pygame.image.load("assets/ball.bmp")
	ballrect = ball.get_rect()

	while RUNNING: 
		clock.tick(FRAMERATE)

		if button24.isPressed() and (time.clock() - button24.getLastPress() > DEBOUNCE):
			baseSpeed = baseSpeed * 2
			speed = [baseSpeed, baseSpeed]
			button24.setLastPressToNow()

		if button25.isPressed() and (time.clock() - button25.getLastPress() > DEBOUNCE):
			baseSpeed = baseSpeed / 2
			speed = [baseSpeed, baseSpeed]
			button25.setLastPressToNow()

		for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						speed[0]  = -1 * baseSpeed 
					if event.key == pygame.K_d:
						speed[0] = 1 * baseSpeed
					if event.key == pygame.K_s:
						speed[1] = 1 * baseSpeed
					if event.key == pygame.K_w:
						speed[1] = -1 * baseSpeed
		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]

		screen.fill(white)
		screen.blit(ball, ballrect)
		pygame.display.flip()


if __name__ == "__main__":
	main()
