# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:57:07 2018

@author: kelto
"""

"""
Goldbach's other conjecture
Problem 46 
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

Solved! 5777, 
Slight problem with carmickal numbers messing up the prime test
"""
import math
import random

def main():
    soFarSoGood = True
    number = 3
    primes = [2,3,5,7]
    while soFarSoGood:
        
        #checks number for composateness
        if isPrime(number):
            print("Is Prime: ", number)
            number = number + 2   
        
        else:
            #checks to make sure primes array has all possible primes within range
            if primes[len(primes) - 1] < number:
                primes = nextPrime(primes, number)
                #print("Primes: ", primes, " Number: ", number)
                
            #takes some prime, and sees if any solution is avalable
            default = False
            for prime in primes:
                if math.sqrt((number-prime)/2)%1 == 0:
                    #Conjecture holds for Number
                    print("Conjt. Holds: ", number)
                    default = True
                    number = number + 2
                    break
            #does not hold
            soFarSoGood = default
    print("FAIL!!!: ", number)
        
        
def isPrime(number):
        #Checks Carmicheal Numbers
    if number in [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461]:
        return False
    #Fermats Little Therom
    for i in range(1,10):
        base = random.randint(2, number - 1)
        if pow(base, number - 1)%number != 1:
            return False
    return True #probably 

def nextPrime(primes, endNum):
    for i in range(primes[len(primes) - 1] + 1, endNum):
        if isPrime(i):
            primes = primes + [i,]
    return primes
    

main()