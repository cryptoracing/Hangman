from hangman_game import HangmanGame
from word import Word
from player import Player

from computer_player import ComputerPlayer

from file_handler import FileHandler
# game.py

# Update the main() function in game.py

def main():
    print("Welcome to Hangman!")
    print("Rules: Guess the word before the hangman is fully drawn to win the round.")

    # Prompt user for settings
    num_rounds = int(input("Enter the number of rounds: "))
    num_hints = int(input("Enter the number of hints: "))
    player_mode = input(
        "Enter 'human' to play against another human or 'computer' to play against the computer: ").lower()

    # Create players
    player1_name = input("Enter Player 1's name: ")
    player1 = Player(player1_name)
    if player_mode == 'human':
        player2_name = input("Enter Player 2's name: ")
        player2 = Player(player2_name)
    else:
        player2 = ComputerPlayer()

    # Initialize Hangman game
    hangman_game = HangmanGame(num_rounds, num_hints, [player1, player2])

    # Start the game
    hangman_game.play()


if __name__ == "__main__":
    main()
