# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 00:24:02 2018

@author: kelto
"""

"""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
import PrimeTools


@PrimeTools.timer()
def main():
    upperbound = 2000000
    total = 0
    sieve = PrimeTools.sieve_of_eratosthenes(upperbound)
    for entry in sieve:
        if sieve[entry]:
            total = total + entry
    print(total)


main()
