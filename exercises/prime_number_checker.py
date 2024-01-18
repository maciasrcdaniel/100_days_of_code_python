#!/usr/bin/env python3


n = int(input("Pick a number\n"))

def prime_checker(number):
    number_prime = True
    for i in range(2, number):
        if number % i == 0:
            number_prime = False
    if number_prime:
        print("Prime")
    else:
        print("Not Prime")


prime_checker(number=n)