"""
Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time
from PrimeTools import find_factors, timer

@timer()
def main():
    number = 600851475143
    print(find_factors(number))
    

main()