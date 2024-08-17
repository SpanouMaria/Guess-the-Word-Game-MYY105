# Guess the Word - Greek Edition

Welcome to "Guess the Word - Greek Edition," a fun word-guessing game implemented in Python using the Tkinter library. This game challenges you to guess a secret 5-letter Greek word within a limited number of attempts.


## Game Instructions
**Objective:** Guess the secret 5-letter Greek word.
**How to Play:**
    - Enter your guess in the input field.
    - Click the "Submit Guess" button.
    - The game will provide feedback indicating whether the letters in your guess are correct and in the right position.
    - You have a limited number of attempts to guess the word correctly.
**Feedback:**
    - Letters in the correct position will be indicated.
    - Letters that are in the word but not in the correct position will also be indicated.
    - You will receive a message if you guess the word correctly or if you run out of attempts.


## Implementation Details
- The game is implemented in Python using the Tkinter library for the graphical user interface.
- Words are read from a file (`5letterwords.txt`) containing valid 5-letter Greek words.
- The game handles file-related errors gracefully, providing a user-friendly error message if the word file is not found.
- User input is validated to ensure it is a 5-letter Greek word.


## How to Run
**Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/guessword-game.git
    cd guessword-game
    ```
**Ensure you have Python installed:** The game requires Python 3. Ensure you have it installed on your system.
**Install Tkinter:** Tkinter is required for the graphical user interface. It comes pre-installed with Python, but if you need to install it, use the following command:
    ```bash
    sudo apt-get install python3-tk
    ```
**Run the Game:**
    ```bash
    python guessword.py
    ```


## Collaboration
This project was a collaborative effort. Special thanks to [ChristosGkovaris](https://github.com/ChristosGkovaris) for their significant contributions to the development and improvement of the game.
