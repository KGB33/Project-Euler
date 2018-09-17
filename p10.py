# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 02:37:56 2018

@author: kelto

Project Euler #10
Sum of primes below 2,000,000
"""
import numpy as np


def main():
    primes = [2,3,5]
    for number in range(7,100,2):
        primes = primes + test_prime(primes,number)
        print(primes,"\n")
            
def test_prime(primes,number):
    for k in range(len(primes)):
        if number%primes[k] == 0:
            break
    primes = primes + [number]
    return(primes)
    
main()