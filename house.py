# House Class

class House:

	def __init__(self, x, y):
		self.location = (x, y)
		self.haunted = False

	def getX(self):
		return self.location[0]

	def getY(self):
		return self.location[1]

	def setX(self, newX):
		self.location[0]= newX

	def setY(self, newY):
		self.location[1]= newY

	def isHaunted(self):
		return self.haunted

	def setHaunted(self, isItHaunted):
		self.haunted = isItHaunted