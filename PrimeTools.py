# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:24:23 2018

@author: kelton
"""
import random
    
    
"""
Uses Femats little thearom to test for primeality
@param number: int that is being checked
@param trials: int that determans the number of bases used,
 the higher the number the more accurate (must be 2 or greater)
"""
def littleFermat(number, trials):
    #Checks Carmicheal Numbers up to ~ 500,000
    if number in [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461]:
        return False
    #Fermats Little Therom
    for i in range(1,trials):
        base = random.randint(2, number - 1)
        if pow(base, number - 1)%number != 1:
            return False

    return True #probably

"""
Uses division to test for primeality
@param number: int that is being checked
"""
def divisionTest(number):
    for divisor in range(2, int(number/2) + 1):
        if number%divisor == 0:
            return False
    return True


"""
Sieve of Eratosthenes
Creates, then returns, a dictionary: { X : Boolean} where X range from
2 to upperbound, and boolean is True if X is prime
@param upperbound - upper limit for the sieve
"""
def sieve_of_eratosthenes(upperbound):
   sieve = {x : True for x in range(2, upperbound)}
   for i in range(2, int(pow(upperbound, .5) + 1)):
       if sieve[i] == True:
           j = pow(i, 2)
       while j < upperbound:
           sieve[j] = False
           j = j + i
   return sieve
