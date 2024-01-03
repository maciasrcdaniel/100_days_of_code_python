#!/usr/bin/env python3

# User input - range 
target = int(input("Enter a number between 0 and 1000\n"))

# Running total of even numbers
even_total = 0

# For every number in target, starting at 0, add 1 
for i in range(0, target+1): 
    # If that number does not have remainder when divided, it is even and add it to the even_total
    if i % 2 == 0:
        even_total += i
    # If that number does have a remainder pass on the number and move onto the next one
    else:
        pass

# Print the running total 
print(even_total)

