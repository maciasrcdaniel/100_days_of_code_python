#!/usr/bin/env python3

import random
import time

# variables
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

chosen_word = random.choice(word_list)
welcome_ascii = """
                                               
  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
 / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
/ __  / (_| | | | | (_| | | | | | | (_| | | | |
\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       
"""

# Welcome message
print("Let's play... {}".format(welcome_ascii))

# Hangman ascii art
hang_man_images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Display list with empty spaces
display = []
# Missed letters list
missed_letters = []
# Life counter
remaining_lives = 6
# hangman counter
i = 0

# length of the chosen random word
word_length = len(chosen_word)

for _ in range(word_length): # for whatever item in the length of the word
    display += "_" # replace the item with _

# Allow to keep playing until the word is met
game_ends = False

# While true - variable instead of "while true" so it can be flipped
while not game_ends:

    # Time delay
    time.sleep(1)

    # User guesses a letter
    guess = input("Guess a letter: ").lower()

    for position in range(word_length): # for every number in length of the chosen_word (doesn't know the word)
        # The letter is used to replace the position of the chosen word
        letter = chosen_word[position]
        # If the letter matches the guess the display[position] is replaced by the letter
        if letter == guess:
            display[position] = letter

    # If the letter is not matched to guess and guess not already in display list
    if (letter != guess) and (guess not in display):
        # Add letter to the missed letters list
        missed_letters.append(guess)
        # Guessed incorrectly increment remaining lives by 1
        remaining_lives -= 1
        # Notify of wrong guess and lost life
        print("You lose a life for guessing incorrectly.")
        print("Wrong guesses: {}".format(missed_letters))
        # increment i counter by 1 to print the next image in the hang_man_images list
        i += 1
        print(hang_man_images[i])

    # For loop print until new condition is met
    print(display)
    print("You have {} lives remaining".format(remaining_lives))

    # Game over if remaining lives reaches 4
    if remaining_lives == 0:
        # Flipped to true so the game ends
        game_ends = True
        # Print game over message
        print("You have ran out of lives. Game over!")

    # Covert the list to string to verify win
    winning_word = ''.join(display)
    # Verify the win
    if winning_word == chosen_word:
        # Flip the variable to true to end the game
        game_ends = True
        # Join the string of letters to form the word
        winning_word = ''.join(display)
        print("You won! Word was '{}'.".format(winning_word))














