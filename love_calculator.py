#!/usr/bin/env python3


print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is your name? ") 


def the_love_calculator():
    # -- Convert names to lowercase
    nameOneCoverted = name1.lower()
    nameTwoConverted = name2.lower()

    # -- Store combined names into a variable
    combinedNames = nameOneCoverted + nameTwoConverted

    # Letter counter placeholders (letterE variable counter is not required twice)
    letterT = 0
    letterR = 0
    letterU = 0 
    letterE = 0
    letterL = 0 
    letterO = 0
    letterV = 0

    # Letter counter
    for i in combinedNames:
        if 't' == i:
            letterT += 1
        if 'r' == i: 
            letterR += 1
        if 'u' == i:
            letterU += 1 
        if 'e' == i:
            letterE += 1
        if 'l' == i: 
            letterL += 1
        if 'o' == i:
            letterO += 1
        if 'v' == i: 
            letterV += 1
        else:
            pass

    # Sum of counts and convert the counters into strings
    true_counter = str(letterT + letterR + letterU + letterE)
    love_counter = str(letterL + letterO + letterV + letterE)

    # Convert back to integers
    true_love_counter_total = int(true_counter + love_counter)

    # If statement to calculate love
    if true_love_counter_total < 10 or true_love_counter_total > 90:
        return (f"Your score is {true_love_counter_total}, you go together like coke and mentos.")
    elif true_love_counter_total > 40 and true_love_counter_total < 50: 
        return (f"Your score is {true_love_counter_total}, you are alright together.")
    else:
        return (f"Your score is {true_love_counter_total}.")


print(the_love_calculator())
