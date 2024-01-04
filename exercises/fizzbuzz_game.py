#!/usr/bin/env python3



# Hold the number 100 variable
starting_number = 100

# For Loop - Print each number 1 to 100
for i in range(0, starting_number+1):
    # If divided by 3 and 5 and there is no remainder print the string
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0: 
        print("Buzz")
    # If it does not match any of the clauses then print the number
    else:
        print(i)


