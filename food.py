# Food Class

class Food:

	def __init__(self, x, y, spritePath):
		self.sprite = spritePath
		self.location = (x, y)
		self.eaten = False

	def getSprite(self):
		return self.sprite

	def setSprite(self, spritePath):
		self.sprite = spritePath

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self, newX):
		self.x = newX

	def setY(self, newY):
		self.y = newY

	def isEaten(self):
		return eaten

	def setEaten(self, isItEaten):
		self.eaten = isItEaten