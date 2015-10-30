# Ghost class

import random

class Ghost:

	

	def __init__(self):
		self.MAX_NOURISHMENT = 100
		self. MAX_HAPPINESS = 100	
		self.nourishment = self.MAX_NOURISHMENT
		self.happiness = self. MAX_HAPPINESS
		self.alive = True

	def depleteDrives(self):
		self.nourishment = self.nourishment - 1
		self. happiness = self.happiness - 1

	def adjustNourishment(self, adjustment):
		self.nourishment = self.nourishment + adjustment
		if self.nourishment > self.MAX_NOURISHMENT:
			self.nourishment = self.MAX_NOURISHMENT
		elif self.nourishment < 0:
			self.nourishment = 0
			self.alive = False

	def adjustHappiness(self, adjustment):
		self.happiness = self.happiness + adjustment
		if self.happiness > self.MAX_HAPPINESS:
			self.happiness = self.MAX_HAPPINESS
		elif self.happiness < 0:
			self.happiness = 0


	def getNourishment(self):
		return self.nourishment

	def getHappiness(self):
		return self.happiness

	def isAlive(self):
		return self.alive

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