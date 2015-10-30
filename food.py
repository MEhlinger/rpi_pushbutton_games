# Food Class

class Food:

	def __init__(self, x, y):
		self.location = (x, y)
		self.eaten = False

	def getX(self):
		return self.location[0]

	def getY(self):
		return self.location[1]

	def setX(self, newX):
		self.location[0] = newX

	def setY(self, newY):
		self.location[1] = newY

	def isEaten(self):
		return self.eaten

	def setEaten(self, isItEaten):
		self.eaten = isItEaten