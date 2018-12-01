"""
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import time
from PrimeTools import divisionTest


def main():
    i = 2
    p = 3
    while i != 10001:
        p += 2
        if divisionTest(p):
            i += 1
    print(p)
        
    

start_time = time.clock()
main()
print(time.clock() - start_time)

    