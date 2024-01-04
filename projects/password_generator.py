#!/usr/bin/env python3

# import modules
import random
import string

# user input
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))


def password_generator():
    # list to store random letters
    new_password = []
    # run through the number of input letters and add them to the new_password list 
    for i in range(1, letters+1): 
        random_letters = random.choice(string.ascii_letters)
        new_password.append(random_letters)

    for i in range(1, symbols+1):
        random_symbols = random.choice(string.punctuation)
        new_password.append(random_symbols)

    for i in range(1, numbers+1):
        random_numbers = random.choice(string.digits)
        new_password.append(random_numbers)

    # shuffle the characters in the password
    random.shuffle(new_password)

    # convert the list into a string
    randomized_password = ''.join(new_password)

    # return the modified list
    return randomized_password

print(password_generator())



