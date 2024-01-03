#!/usr/bin/env python3

# import module
import random

# ASCII art
rock = '''
    _______
---'   ____)
      (_____)
Rock  (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
Paper     _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
Scissors   ______)
       __________)
      (____)
---.__(___)
'''


# Assign values to 0/1/2
def user_selection_function(): 
    
    # User input - user input for rock/paper/scissors
    user_input_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    # Random number generator
    random_list = [0, 1, 2]
    random_number = random.choice(random_list)

    # Assign value to the numbers
    if user_input_rps == 0 and random_number == 0:
        return (f"This is a draw.")
    elif user_input_rps == 0 and random_number == 1:
        return (f"{paper} \nbeats {rock} \nYou win.")
    elif user_input_rps == 0 and random_number == 2:
        return (f"{rock} \nbeats {scissors} \nYou win.")
    elif user_input_rps == 1 and random_number == 0: 
        return (f"{paper} \nbeats {rock} \nYou lose.")
    elif user_input_rps == 1 and random_number == 1:
        return (f"This is a draw")
    elif user_input_rps == 1 and random_number == 2:
        return (f"{scissors} \nbeats {paper} \nYou lose")
    elif user_input_rps == 2 and random_number == 0: 
        return (f"{rock} \nbeats {scissors} \nYou lose.")
    elif user_input_rps == 2 and random_number == 1:
        return (f"{scissors} \nbeats {paper} \nYou win.")
    elif user_input_rps == 2 and random_number == 2:
        return (f"This is a draw")
    else:
        return ("Please select 0, 1 or 2.")

# Call the function
print(user_selection_function())


