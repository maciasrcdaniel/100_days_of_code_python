#!/usr/bin/env python3

# import module
import time

# -- Constant variables
island_ascii = """
            88           88                                 88  
            ""           88                                 88  
                         88                                 88  
            88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
            88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
            88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
            88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
            88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
            """

hole_ascii = """You fell in a
        
        88                      88             
        88                      88             
        88                      88             
        88,dPPYba,   ,adPPYba,  88  ,adPPYba,  
        88P'    "8a a8"     "8a 88 a8P_____88  
        88       88 8b       d8 88 8PP"""""""  
        88       88 "8a,   ,a8" 88 "8b,   ,aa  
        88       88  `"YbbdP"'  88  `"Ybbd8"'  
        """

fish_ascii = """ You were eaten alive by a
                                                    888 .d888d8b        888      
                                                    888d88P" Y8P        888      
                                                    888888              888      
            .d8888b 888  888  888 .d88b. 888d888 .d88888888888888.d8888b 88888b.  
            88K     888  888  888d88""88b888P"  d88" 888888   88888K     888 "88b 
            "Y8888b.888  888  888888  888888    888  888888   888"Y8888b.888  888 
                 X88Y88b 888 d88PY88..88P888    Y88b 888888   888     X88888  888 
             88888P' "Y8888888P"  "Y88P" 888     "Y88888888   888 88888P'888  888 
            """

fire_ascii = """You were burned by 
                     __ _          
                    / _(_)         
                    | |_ _ _ __ ___ 
                    |  _| | '__/ _ \
                    | | | | | |  __/
                    |_| |_|_|  \___|   
                    """

monster_ascii = """You were killed by a
                                                        888                   
                                                        888                   
                                                        888                   
                    88888b.d88b.  .d88b. 88888b. .d8888b 888888 .d88b. 888d888 
                    888 "888 "88bd88""88b888 "88b88K     888   d8P  Y8b888P"   
                    888  888  888888  888888  888"Y8888b.888   88888888888     
                    888  888  888Y88..88P888  888     X88Y88b. Y8b.    888     
                    888  888  888 "Y88P" 888  888 88888P' "Y888 "Y8888 888  
                    """

party_ascii = """You win! Let's
                                                        88                 
                    8b,dPPYba,  ,adPPYYba, 8b,dPPYba, MM88MMM 8b       d8  
                    88P'    "8a ""     `Y8 88P'   "Y8   88    `8b     d8'  
                    88       d8 ,adPPPPP88 88           88     `8b   d8'   
                    88b,   ,a8" 88,    ,88 88           88,     `8b,d8'    
                    88`YbbdP"'  `"8bbdP"Y8 88           "Y888     Y88'     
                    88                                            d8'      
                    88                                           d8' 
                        
                    """

# -- Function to restart the game 
def restart_game(): 

    restart_game_input = input("Play again? YES OR NO\n").lower()

    if restart_game_input == 'yes': 
        return treasure_island()
    else:
        return ("Game Over.")
    
# -- Treasure Island Game Function
def treasure_island():
    
    # -- Welcome message
    print("Welcome to Treasure Island.")
    time.sleep(1)
    print(island_ascii) 
    time.sleep(1)
    print("Your mission is to find the treasure.\n")


    # -- User decides to go left or right
    leftRightInput = input("Let's start trying to find the treasure. Select one: LEFT or RIGHT?\n").lower()

    # -- If statement to proceed past hole level
    if leftRightInput != "left":
        # -- Print the ascii for hole
        print(hole_ascii)
        # -- restart the game
        return restart_game() 

    else:
        
        # -- User input for swim or wait level
        swimOrWait = input("You didn't fall into the hole, but now you have to decided. Select one: SWIM or WAIT\n").lower()

        # -- If statement for the swim or wait level
        if swimOrWait != "wait": 
            print(fish_ascii)
            return restart_game()

        else:

            # -- User input for encountering a door
            colorDoor = input("Three doors magically appear. Select one: RED OR YELLOW OR BLUE\n").lower()

            # -- If statement for yellow door selection else proceed
            if colorDoor == "red":
                print(fire_ascii)
                return restart_game()
                        
            elif colorDoor == "blue":
                print(monster_ascii)
                return restart_game()
                        
            elif colorDoor == "yellow": 
                print(party_ascii)
                return restart_game()
            
            else:
                # -- Ask user to play again
                print("Game Over.")
                return restart_game()

# -- Call your function
print(treasure_island())
        
        









