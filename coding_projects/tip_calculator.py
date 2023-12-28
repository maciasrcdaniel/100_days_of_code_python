#!/usr/bin/env python3

# Store user input into variables
bill = float(input("What is your bill total? "))
split = int(input("Split between how many people? "))
tip_percentage_input = int(input("What's the tip percentage? "))

# Function for calculating the tip
def tip_calculator():
    bill_split = (bill/split)
    tip_percentage_bill = (((tip_percentage_input/100) * bill) / split)
    divided_split = (bill_split + tip_percentage_bill)
    dec_places = "{:.2f}".format(divided_split)
    return dec_places

# Print the returned value with fstrings
print(f"Each person should pay ${tip_calculator()}.") 