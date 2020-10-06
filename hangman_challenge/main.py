#----- REQUIRED MODULES -----#

# import class containing game
from utils.game import Hangman

# import random word generator
from random_words import RandomWords

#----- GAME START -----#

# 1. Set a unique word (e.g. 'paper') to test the code and have all possible outputs

hangman = Hangman("paper")
hangman.start_game()


# 2. Set a random word (comment 1.)

'''r = RandomWords()
word = r.random_word()


hangman = Hangman(word)
hangman.start_game()'''

