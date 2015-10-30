#!/usr/bin/python3.4

import random

class Ghost:

	MAX_NOURISHMENT = 100
	MAX_HAPPINESS = 100

	def __init__(self, startx, starty, startSpritePath):
		self.speed = (1, 1)
		self.nourishment = MAX_NOURISHMENT
		self.happiness = MAX_HAPPINESS
		self.alive = True
		self.sprite = startSpritePath

	def randomlyChangeDirection(self):
		newSpeed = random.randrange(-2,2)
		self.speed = (random.randrange(-2, 2), random.randrange(-2, 2))

	def depleteDrives(self):
		self.nourishment = self.nourishment - 1
		self. happiness = self.happiness - 1

	def adjustNourishment(self, adjustment):
		self.nourishment = self.nourishment + adjustment
		if self.nourishment > MAX_NOURISHMENT:
			self.nourishment = MAX_NOURISHMENT
		elif self.nourishment < 0:
			self.nourishment = 0
			self.alive = False

	def adjustHappiness(self, adjustment):
		self.happiness = self.happiness + adjustment
		if self.happiness > MAX_HAPPINESS:
			self.happiness = MAX_HAPPINESS
		elif self.happiness < 0:
			self.happiness = 0


	def getNourishment(self):
		return self.nourishment

	def getHappiness(self):
		return self.happiness

	def isAlive(self):
		return self.alive

	def getSprite(self):
		return self.sprite

	# DO NOT USE THE SETTERS TO REPRESENT EATING OR OTHER SMALL ADJUSTMENTS.
	# THESE ALLOW FOR VALUES OUTSIDE OF MAX_CONSTANTS AND 0
	# If these are used to adjust manually for a special reason outside of
	# those boundaries, then the new values will be legal until
	# adjust<drive> is called for that <drive>.

	def setNourishment(self, newNourishment):
		self.nourishment = newNourishment

	def setHappiness(self, newHappiness):
		self.happiness = newHappiness

	def setAlive(self, isItAliveNow):
		self.alive = isItAliveNow

	def setSprite(self, spritePath):
		self.sprite = spritePath