# Word Game

## Description

This Python project implements a word game where players attempt to guess a randomly selected five-letter word. The game provides feedback on each guess, indicating the correctness of letters and their positions.

## Features

- **Word Dictionary Initialization:**
  - Reads a dictionary file (`word_game5.txt`) to initialize a word game dictionary.
  - Allows customization of word size.

- **Guess Validation:**
  - Checks if user input is a valid five-letter word.
  - Provides informative error messages for invalid inputs.

- **Gameplay:**
  - Players have seven attempts to guess the word.
  - Feedback is provided after each guess, highlighting correct letters and their positions.

- **End of Game:**
  - Game ends when the word is correctly guessed or when the maximum attempts (7) are reached.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/pyhn/word-game.git
   cd word-game
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Follow the prompts to make your guesses.

## Dependencies

- Python 3.x
