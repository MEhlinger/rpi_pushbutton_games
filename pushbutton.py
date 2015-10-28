# GPIO Capactive Sensor Input Module
# For Raspberry Pi
# by Marshall Ehlinger, Oct 2015

import time
import RPi.GPIO as GPIO

class PushButton:

	def __init__(self, pinNum):
		self.pinNumber = pinNum
		self.lastPress = 0.00
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pinNumber, GPIO.IN)

	def isPressed(self):
		return not GPIO.input(self.pinNumber) # Pushbutton defaults open

	def getPinNumber(self):
		return self.pinNumber

	def getLastPress(self):
		return self.lastPress

	def setLastPressToNow(self):
		self.lastPress = time.clock()

	def setLastPressAsArg(self, lastPressTime):
		self.lastPress = lastPressTime 

	def timeElapsedSinceLastPress(self):
		return time.clock() - self.getLastPress()