from word import Word
import os
from computer_player import ComputerPlayer


# Define HangmanGame class
class HangmanGame:
    def __init__(self, rounds, hints, players):
        self.rounds = rounds
        self.hints = hints
        self.players = players
        self.current_round = 0
        self.current_player_index = 0
        self.words = [
            {'word': 'hangman', 'category': 'Game'},
            {'word': 'swimming', 'category': 'Activity'},
            {'word': 'apple', 'category': 'Fruit'}
            # Add more words and categories as needed
        ]

    def play(self):
        while self.current_round < self.rounds:
            self.current_round += 1

            # Get word and category for the current round
            word_info = self.words[self.current_round - 1]
            word, category = word_info['word'], word_info['category']

            # Play the round
            winner, scores = self.play_round(word, category)

            # Update scores
            for player, score in scores.items():
                player.score += score

            # Display updated scores
            print("\nScores:")
            for player in self.players:
                print(f"{player.name}: {player.score}")

            # Determine current player for the next round
            if winner:
                next_player_index = (self.players.index(winner) + 1) % len(self.players)
            else:
                next_player_index = (self.players.index(self.players[-1]) + 1) % len(self.players)
            self.current_player_index = next_player_index

        # Determine the overall winner based on scores
        overall_winner = max(self.players, key=lambda x: x.score)
        print(f"\nGame over! Overall winner: {overall_winner.name} with a score of {overall_winner.score}.")

    def play_round(self, word, category):
        guessed_word = Word(word)
        guessed_letters = set()
        max_turns = len(word) + self.hints
        scores = {player: 0 for player in self.players}

        print(f"\nCategory: {category}")

        while True:
            self.clear_screen()  # Clear the screen
            self.display_hangman(
                len(guessed_letters.intersection(set(word))))  # Display hangman based on incorrect guesses
            print(f"\nWord: {guessed_word.display_word()}")
            print("\nAlphabet Letters:")
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter in guessed_letters:
                    print(f"\033[1;30m{letter.upper()}\033[0m", end=" ")
                else:
                    print(letter, end=" ")
            print("\n")

            current_player = self.players[self.current_player_index]
            if isinstance(current_player, ComputerPlayer):
                print("Computer's turn:")

            guess = current_player.make_guess(word, guessed_letters)

            if guess == 'hint':
                print(f"\nHint: {self.get_hint(word)}")
                continue
            elif len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter or 'hint'.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("\nCorrect guess!")
                guessed_word.guessed_letters.append(guess)
                scores[current_player] += 1
            else:
                print("\nIncorrect guess!")

            if guessed_word.display_word().replace(" ", "") == word:
                print(f"\n{current_player.name} guessed the word '{word}' correctly!")
                return current_player, scores

            if not isinstance(current_player, ComputerPlayer):
                input("Press Enter to continue...")

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

            # Check if maximum number of turns reached
            if len(guessed_letters) >= max_turns:
                print("\nMaximum number of turns reached. Game over!")
                return None, scores

    def get_hint(self, word):
        # Implement logic to generate a hint for the word
        pass

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_hangman(self, turns):
        hangman_stages = [
            """
               _________
              |         |
              |
              |
              |
              |
            __|________
            """,
            """
               _________
              |         |
              |         O
              |
              |
              |
            __|________
            """,
            """
               _________
              |         |
              |         O
              |         |
              |
              |
            __|________
            """,
            """
               _________
              |         |
              |         O
              |        /|
              |
              |
            __|________
            """,
            """
               _________
              |         |
              |         O
              |        /|\\
              |
              |
            __|________
            """,
            """
               _________
              |         |
              |         O
              |        /|\\
              |        /
              |
            __|________
            """,
            """
               _________
              |         |
              |         O
              |        /|\\
              |        / \\
              |
            __|________
            """
        ]

        print(hangman_stages[
                  min(turns, len(hangman_stages) - 1)])  # Display the hangman stage based on the number of turns
