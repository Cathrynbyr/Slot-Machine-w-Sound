""" 
Program: SlotMachineGUI2.py
Author: Cathryn Byrnes 11-18-21

*** Note: the 
files "breezypythongui.py", image file "slots.jpg" and sound files "slots-machine.wav", "sad.mp3" and "gameover.mp3" MUST be in the same directory as the file in order for the application to work.***
"""

from breezypythongui import EasyFrame
import random
from tkinter.font import Font
from PIL import ImageTk
import pygame

class SlotMachine(EasyFrame):


	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Test Your Luck", width = 400, height = 600, background = "limegreen", resizable = True)
		# Title label
		self.addLabel(text = "Lucky Slots!", row = 0, column = 0, columnspan = 3, background = "limegreen", foreground = "yellow", font = Font(family = "Impact", size = 28), sticky = "NSEW")

		imageLabel = self.addLabel(text = "", sticky = "NSEW", background  = "limegreen", row = 3, column = 0, columnspan = 3)
		self.image = ImageTk.PhotoImage(file = "slots.jpg")
		imageLabel["image"] = self.image

		# Funds and label field
		self.addLabel(text = "Available funds", row = 2, column = 0, columnspan = 3, background = "limegreen", foreground = "yellow", font = Font(family = "Impact", size = 18), sticky = "NSEW")

		self.fundsField = self.addIntegerField(value = 100, row = 1, column = 1, sticky = "NSEW", state = "readonly")

		# Fields for the random numbers to appear
		self.numField1 = self.addIntegerField(value = 0, row = 4, column = 0, sticky = "NSEW")
		self.numField2 = self.addIntegerField(value = 0, row = 4, column = 1, sticky = "NSEW")
		self.numField3 = self.addIntegerField(value = 0, row = 4, column = 2, sticky = "NSEW")

		# Command Button
		self.playButton = self.addButton(text = "**Spin**", row = 5, column = 0, columnspan = 3, command = self.slots)
		self.playButton["background"] = "yellow"

		# Label for the output message
		self.outputLabel = self.addLabel(text = "", row = 6, column = 0, columnspan = 3, sticky = "NSEW", background = "limegreen", foreground = "yellow", font = Font(family = "Georgia", size = 18))

	#Event Handling Method
	def slots(self):
		# Variables and constants
		num1 = random.randint(1, 9)
		num2 = random.randint(1, 9)
		num3 = random.randint(1, 9)


		# Grab the current funds value from the FundField component
		fundsLeft = self.fundsField.getNumber()

		#soundbites 
		pygame.mixer.init()
		youWin = pygame.mixer.Sound("slots-machine.wav")
		looser = pygame.mixer.Sound("sad.mp3")
		youLoose = pygame.mixer.Sound("gameover.mp3")



		# Determine the outcome of the game
		if num1 == num2 == num3:
			result = "JACKPOT!!!!"
			youWin.play()
			fundsLeft += 30
		elif num1 == num2 or num2 == num3 or num3 == num1:
			result = "Two of a Kind!"
			youWin.play()
			fundsLeft += 20
		else:
			result = "Sorry, you loose..."
			looser.play()
			fundsLeft -= 10

		# Determine if there are any funds left
		if fundsLeft == 0:
			result = "You lose and GAME OVER"
			youLoose.play()
			self.playButton["state"] = "disabled"

		# Output phase
		self.numField1.setNumber(num1)
		self.numField2.setNumber(num2)
		self.numField3.setNumber(num3)
		self.outputLabel["text"] = result

		# Update the fundsField value before this function is triggered again
		self.fundsField.setNumber(fundsLeft)


#definition of the main()function for program entry
def main():
	"""Instantiation and pops up the window."""
	SlotMachine().mainloop()

# global call to trigger the main()function
if __name__	== "__main__":
	main()

