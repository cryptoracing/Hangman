# word.py

class Word:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word.strip()
