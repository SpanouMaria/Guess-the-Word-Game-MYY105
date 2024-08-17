import tkinter as tk
from tkinter import messagebox
import random
import os

# Function to read words from the file
def read_words_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip().upper() for line in file]
    return words

# Function to select a random word from the list
def select_random_word(word_list):
    return random.choice(word_list)

# Function to check the validity of the word
def check_word_validity(word, valid_letters):
    return len(word) == 5 and all(letter.isalpha() and letter in valid_letters for letter in word)

# Main game class
class GuessWordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Word - Greek Edition")
        
        # Load words and select a random word
        file_path = 'C:\\GitHub\\Projects\\GuessWord\\5letterwords.txt'
        try:
            self.words = read_words_from_file(file_path)
        except FileNotFoundError as e:
            messagebox.showerror("File Not Found", str(e))
            self.root.destroy()
            return
        
        self.secret_word = select_random_word(self.words)
        self.attempts = 0
        self.max_attempts = 6
        self.used_letters = []
        
        # Create UI components
        self.create_widgets()
        
    def create_widgets(self):
        # Label for instructions
        self.instructions = tk.Label(self.root, text="Guess the 5-letter Greek word!")
        self.instructions.pack()
        
        # Entry widget for user input
        self.entry = tk.Entry(self.root, font=('Arial', 14))
        self.entry.pack()
        
        # Button to submit guess
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack()
        
        # Label to display feedback
        self.feedback = tk.Label(self.root, text="", font=('Arial', 14))
        self.feedback.pack()
        
    def submit_guess(self):
        guess = self.entry.get().upper()
        if check_word_validity(guess, greek_caps) and guess in self.words:
            self.attempts += 1
            self.used_letters.append(guess)
            self.provide_feedback(guess)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid 5-letter Greek word.")
        
    def provide_feedback(self, guess):
        if guess == self.secret_word:
            self.feedback.config(text=f"Congratulations! You guessed the word '{self.secret_word}' in {self.attempts} attempts.")
            self.submit_button.config(state=tk.DISABLED)
        else:
            feedback_text = f"Attempt {self.attempts}/{self.max_attempts}: {self.get_feedback_text(guess)}"
            self.feedback.config(text=feedback_text)
            if self.attempts >= self.max_attempts:
                self.feedback.config(text=f"Game Over! The word was '{self.secret_word}'.")
                self.submit_button.config(state=tk.DISABLED)
    
    def get_feedback_text(self, guess):
        feedback = []
        for i in range(5):
            if guess[i] == self.secret_word[i]:
                feedback.append(f"{guess[i]} (correct)")
            elif guess[i] in self.secret_word:
                feedback.append(f"{guess[i]} (present)")
            else:
                feedback.append(f"{guess[i]} (absent)")
        return ', '.join(feedback)

# Create the main window and run the game
if __name__ == "__main__":
    greek_caps = [chr(i) for i in range(913, 930)] + [chr(i) for i in range(931, 938)]
    root = tk.Tk()
    game = GuessWordGame(root)
    root.mainloop()