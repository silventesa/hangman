#----- REQUIRED MODULES -----#

# to use regular expressions
import re

# to extract mutliple indices of a repeated item in a list
from more_itertools import locate

# to typing purposes
from typing import List


#----- CLASS DECLARATION -----#
class Hangman:
	def __init__(self, good_word):
		'''Definition of class properties (typed)'''

		# the searched word (target word)
		self.good_word: List[str] = [i for i in good_word]

		# the number of player's lifes (starts at 5)
		self.life: int = 5

		# list of guessed letters and remaining letters (shown by '_')
		self.well_guessed_letters: List[str] = ['_']*len(self.good_word)
		
		# list of failed letters 
		self.bad_guessed_letters: List[str] = []

		# number of turns played by the player
		self.turn_count: int = 0

		# number of errors made by the player
		self.error_count: int = 0

		# number of well guessed letters
		self.good_answers: int = 0

	def start_game(self):
		'''Method displayed at game start and at each new turn. 
		The function play() will be run until the game is over'''

		# While player still has lifes and the word is not guessed, play() is called
		while self.life > 0 and self.good_word != self.well_guessed_letters:
			return self.play()

		# If no lifes remain, the player looses and the game is over
		if self.life == 0:
			return self.game_over()
		
		# If the word is completed, the player wins and the game is over	
		elif self.good_word:
			return self.well_played()


	def play(self):
		'''Core game method to be displayed in each turn. 
		Conditions for incorrect inputs, guessed and failed letters included'''

		# Show spaces of letters to be guessed and guessed letters
		print(*self.well_guessed_letters)

		# Main loop. 
		# incorrect_input turns to False to change turn
		incorrect_input = True

		while incorrect_input:
			new_letter = input('\nEnter a new letter: \n')
			new_letter = new_letter.lower()
			
			# Conditions and outputs for incorrect (non-single letter) inputs
			if not re.match('^[a-zA-Z]', new_letter):
				print("Please enter a letter")
			elif len(new_letter) > 1:
				print("Please enter 1 single letter")

			# Conditions for repeated inputs
			elif new_letter in self.well_guessed_letters:
				print('You already found this letter!', self.well_guessed_letters, end = '\n')

			elif new_letter in self.bad_guessed_letters:
				print('You already tried this letter! \n Here are all your (bad) tries: ', *self.bad_guessed_letters, end = '\n')

			# Condition when input is correct and letter is in target word. 
			# Letter added in well_guessed_letters and displayed in the next turn
			elif new_letter in self.good_word:
				all_indices = list(locate(self.good_word, lambda a: a == new_letter))
				for i in all_indices:
					self.well_guessed_letters[i] = new_letter

				self.good_answers += 1
				print('Correct!')

				# Stop the loop and run a new turn 	
				incorrect_input = False
				self.start_game()
			
			# Condition when input is correct and letter is NOT in target word (failed)
			else:
				self.bad_guessed_letters.append(new_letter)
				self.error_count += 1
				self.turn_count += 1
				self.life -= 1
				if self.life > 0:
					print('Sorry! This letter is not in the word. You still have {} chance(s)'.format(self.life))
				
				# Stop the loop and run a new turn 
				incorrect_input = False
				self.start_game()


	def game_over(self):
		'''Player looses. Stop the game'''

		print("Game over...")

	def well_played(self):
		'''Player wins. Print performance summary and stop the game'''

		# Show target word as string (instead of list)
		good_word = ""
		for i in self.good_word:
			good_word += i

		print("You found the word '{}' in {} turn(s) with {} error(s)!".format(good_word, 
			self.turn_count,
			self.error_count))
