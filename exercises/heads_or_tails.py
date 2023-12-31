#!/usr/bin/env python3

# import random module
import random

# random number function
def random_number_func(): 

    # random number generator
    num_list = [0, 1]
    random_int = random.choice(num_list)
    
    # return int
    return random_int

# function - heads or tails
def heads_or_tails(): 

    # if statement to verify heads or tails
    if random_number_func() == 0:
        return "heads"
    else:
        return "tails"
    
# function - verify win
def verify_win():

    # user input - selects heads or tails
    user_heads_or_tails = input("Select: heads or tails\n")
    # if statement to verify win
    if heads_or_tails() == user_heads_or_tails:
        return ("You win!")
    elif heads_or_tails() != user_heads_or_tails:
        return ("You lose!")

print(verify_win())

    









