#!/usr/bin/env python3

# Import module for sleep functions
import time

# Pizza function 
def total_pizza_order():
    # Welcome message for pizza app
    print("""
    ______            _                    _      ______ _              
    |  _  \          | |                  ( )     | ___ (_)             
    | | | |__ _ _ __ | | ___ __   ___  ___|/ ___  | |_/ /_ __________ _ 
    | | | / _` | '_ \| |/ / '_ \ / _ \/ _ \ / __| |  __/| |_  /_  / _` |
    | |/ / (_| | | | |   <| | | |  __/  __/ \__ \ | |   | |/ / / / (_| |
    |___/ \__,_|_| |_|_|\_\_| |_|\___|\___| |___/ \_|   |_/___/___\__,_|
                                                                   
    """)

    # Sleep timer for 2 seconds
    time.sleep(2)     

    # Running total of pizza cost
    final_total = 0

    # Inputs from user
    size = input("What size pizza would you like? S, M, L\n") # What size pizza do you want? S, M, or L
    add_pepperoni = input("Do you want pepperoni? Y or N\n") # Do you want pepperoni? Y or N
    extra_cheese = input("Do you want extra cheese? Y or N\n") # Do you want extra cheese? Y or N

    # Format all letters to lowercase
    pizza_size = size.lower()
    adding_pepperoni = add_pepperoni.lower()
    Add_extra_cheese = extra_cheese.lower()

    # Cost of pizza per size
    small = 15
    medium = 20
    large = 25

    # Add pepperoni as a topping
    small_pep = 2
    large_medium_pep = 3

    # Add extra cheese
    x_cheese = 1

    # Add pizza cost by size to final_total
    if pizza_size == "s":
        final_total += small
    elif pizza_size == "m":
        final_total += medium
    elif pizza_size == "l":
        final_total += large
    else: 
        pass
        
    # Add topping(pepperoni) to final_total
    if adding_pepperoni == "y": 
        if pizza_size == "s":
            final_total += small_pep
        else: 
            final_total += large_medium_pep

    # Adding extra cheese
    if Add_extra_cheese == "y": 
        final_total += x_cheese

    # Format grand total output
    grand_total = "{:.2f}".format(final_total)

    # Show delay for processing
    print("Proccessing your order!")
    print("""
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        """)

    # Additional sleep timer
    time.sleep(2)

    return grand_total

# Print the grand total with currency formatting 
print(f"Thank you for choosing Danknee's Pizza! Your final bill is: ${total_pizza_order()}.") 

