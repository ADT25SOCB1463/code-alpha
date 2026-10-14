"""
CodeAlpha Python Internship - Task 4: Hangman Game
A simple text-based Hangman game.
"""

import random

WORDS = ["python", "computer", "programming", "keyboard", "developer",
         "database", "function", "variable", "algorithm", "internet"]

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("=== HANGMAN GAME ===")
    print("Guess the hidden word one letter at a time.")

    while wrong_guesses < max_wrong_guesses:
        display_word = " ".join(
            letter if letter in guessed_letters else "_" for letter in word
        )
        print("\nWord:", display_word)
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")

    print("\nYou ran out of guesses. The word was:", word)

if __name__ == "__main__":
    play_hangman()
