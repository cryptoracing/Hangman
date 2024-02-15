# Create a new file named computer_player.py

# Import necessary modules
from player import Player
import random

# Define ComputerPlayer class inheriting from Player
class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")


    def make_guess(self, word, guessed_letters):
        # Choose a letter to guess
        remaining_letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in guessed_letters]
        guess = random.choice(remaining_letters)
        print(f"{self.name} guesses: {guess}")
        return guess
