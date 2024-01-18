#!/usr/bin/env python3


n = int(input("Pick a number"))

def prime_checker(number):
    counter_range = range(1, 17)
    # list of primes
    list_of_primes = [2,3]

    # Find primes
    for i in counter_range:
        minus_prime = ((6 * i) - 1)
        plus_prime = ((6 * i) + 1)
        list_of_primes.append(minus_prime)
        list_of_primes.append(plus_prime)

    if number in list_of_primes:
        print("Prime Number")
    else:
        print("Not Prime")

prime_checker(number=n)