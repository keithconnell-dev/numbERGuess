"""
Program: numberGuessGUI.py
8.12.24

***NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the number guessing game from chapter3"""

from breezypythongui import EasyFrame
import random
# Other imports can go here

# class header (class name will change project2project)
class GuessingGame(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Guessing Game 2.0", width = 260, height = 180, resizable = False)

		# Initialize the instance variable for this class
		self.magicNumber = random.randint(1, 100)
		self.count = 0

		# Create and add widgets to the window
		self.hintLabel = self.addLabel(text = "Guess a Number bewteen 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addLabel(text = "your guess:", row = 1, column = 0)
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1)
		self.nextButton = self.addButton(text = "Next", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, command = self.newGame) 

	# Defintion of the nextGuess() function
	def nextGuess(self):
		"""Process the user's next guess."""
		self.count += 1
		# Collect the user input from the integer field 
		guess = self.guessField.getNumber()
		# Logic that determines the game's outcome
		if guess == self.magicNumber:
			self.hintLabel["text"] = "Hooray! You got it in " + str(self.count) + " attempt(s)!" 
			self.nextButton["state"] = "disabled"
		elif guess < self.magicNumber:
			self.hintLabel["text"] = "Sorry! Your guess is too low!"
		else:
			self.hintLabel["text"] = "Whoops! Your guess is too high!"

	# Defintion of the newGame() functiuon 
	def newGame(self): 
		"""Resets the data and GUI to their original states."""
		self.magicNumber = random.randint(1, 100)
		self.count = 0
		self.hintLabel["text"] = "Guess a Number bewteen 1 and 100"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"


# Global defnition of the main() method
def main():
	# Instantiate an object from the class int0 mainloop()
	GuessingGame().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()

