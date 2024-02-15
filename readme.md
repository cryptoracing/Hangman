# Hangman Game

Hangman Game is a Python program that allows users to play the classic word guessing game. Players try to guess a word by suggesting letters within a limited number of attempts. 

## Features

- Play against another human or against the computer.
- Choose the number of rounds and hints before starting the game.
- View scores after each round.
- Clear screen and redraw UI after each turn.
- Human player can request a hint.
- Computer player's turn automatically triggered.
- Parse words from the Merriam-Webster website and allow user to approve them for addition to the game.

## File Structure

The project is structured as follows:
Hangman/<br>
│<br>
├── game.py             # Main script to start the game <br>
├── hangman_game.py     # HangmanGame class definition<br>
├── player.py           # Player and ComputerPlayer class definitions<br>
├── file_handler.py     # FileHandler class for file operations<br>
├── suggest_words.py    # Script to parse words from website and suggest for addition<br>
├── words.txt           # Text file containing words for the game<br>
└── README.md           # Project documentation in Markdown format<br>

## Usage

1. Run `game.py` to start the game.
2. Follow the on-screen instructions to play the game.

## Dependencies

- Python 3.x
- BeautifulSoup (for parsing website)
- Requests (for making HTTP requests)

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:

`pip install beautifulsoup4 requests`