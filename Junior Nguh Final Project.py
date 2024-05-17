# Junior Nguh Final Project 
# Word Guessing Game
import os 

# Importing required modules for random words from the word bank
import random

# Word bank with clues; what do all of these animals have in common? - The secret word
word_bank = {'lion': 'Known as the "king of beasts" or "king of the jungle',
    'panda': 'It is characterised by its bold black-and-white coat and rotund body; there is also a movie named after it',
    'tiger': 'Distinctive orange fur and black stripes, known as the big cat of the jungle',
    'chimp': 'We share 99.9 percent of our DNA with this animal',
    'turtle': 'Known for his race against a rabbit, it has a hard shell.',}

# Game variables
#Empty list to keep guesses
# Track the number of word and letter guesses
guesses = []
word_guesses = 0
letter_guesses = 0

# The secret word is mammal; set the secret word
secret_word = "mammal"

#Welcome message for the game & game instructions
print("Hello! Welcome to the Mammal Guessing Game! By Junior Nguh")
print("Guess the secret word to win the game and show off your knowledge!.")

while True: # Start a loop for the game
    guess = input("Guess a letter or the whole word to play the game; lower case letters only: ").lower() # Only use lower case letters in the game

    if len(guess) == 1:  # Chech if the guess is a single letter
        letter_guesses += 1 # 1 letter guess at a time
        if letter_guesses > 5: # Dont use more than 5 guesses in a given round of the games function
            print("Sorry you are out of letter guesses. Game over :(")
            break # End the loop
        if guess in secret_word: # See if the guessed letter is in the secret word
            print(f"That is one of the letters in the secret word. What are the others?")
            guesses.append(guess)
        else:
            print("Sorry, that letter is not in the secret word.")
    else:  
        word_guesses += 1
        if word_guesses > 2:
            print("You've reached the maximum number of word guesses. Game over.")
            break # End the loop
        if guess == secret_word: # Check if this matches the secret word
            print(f"Congratulations! You've guessed the secret word correctly after {word_guesses} word guesses. You won the game!") # Alert player that there guess is correct and they have won the game!
            break # End the loop
        else:
            print("Sorry, that's not the correct word.") # Notify player that the guess is wrong