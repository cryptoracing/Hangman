class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def make_guess(self, word, guessed_letters):
        guess = input("Enter your guess (or 'hint' for a hint): ").lower()
        return guess

