#!/usr/bin/env python3

# IMPORT MODULES
import random

# CONSTANT VARIABLES
band_name_generator_banner = """
 ######                          #     #                          #####                                                         
 #     #   ##   #    # #####     ##    #   ##   #    # ######    #     # ###### #    # ###### #####    ##   #####  ####  #####  
 #     #  #  #  ##   # #    #    # #   #  #  #  ##  ## #         #       #      ##   # #      #    #  #  #    #   #    # #    # 
 ######  #    # # #  # #    #    #  #  # #    # # ## # #####     #  #### #####  # #  # #####  #    # #    #   #   #    # #    # 
 #     # ###### #  # # #    #    #   # # ###### #    # #         #     # #      #  # # #      #####  ######   #   #    # #####  
 #     # #    # #   ## #    #    #    ## #    # #    # #         #     # #      #   ## #      #   #  #    #   #   #    # #   #  
 ######  #    # #    # #####     #     # #    # #    # ######     #####  ###### #    # ###### #    # #    #   #    ####  #    # 
 """

# LIST OF ADJECTIVES
band_name_adjectives = ['dirty', 'smelly', 'crazy', 'wild']

# FUNCTION FOR BAND NAME GENERATOR
def band_name_generator():

    # WELCOME BANNER
    print(band_name_generator_banner)
    
    # USER INPUT - STREET NAME
    city_name = input("What city did you grow up in?\n")

    # USER INPUT - PET NAME
    pet_name = input("What is the name of your pet?\n")

    # # RANDOM ITEM FROM BAND_NAME_ADJECTIVES LIST
    # random_item = random(band)

    # CONCATENATE BAND NAME
    return (f"Your new bands name is {random.choice(band_name_adjectives)} {city_name} {pet_name}.")

# CALL YOUR FUNCTION 
print(band_name_generator())
    





