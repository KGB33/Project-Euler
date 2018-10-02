# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:08:02 2018

@author: kelto
"""

"""
Highly divisible triangular number
Problem 12 
The sequence of triangle numbers is generated by adding the natural numbers.
 So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
 The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

"""
Answer: 76576500
(25.5 secs)
"""


import time

def main():
    condition = False
    n = 4
    tri_num = 6
    while condition == False:
        factors = FindFactors(tri_num)
        #print(factors)
        if len(factors) > 500:
            print(tri_num)
            condition = True
        tri_num = tri_num + n
        n = n + 1
        
    
def FindFactors(number):
    i = 1
    factors = []
    while i not in factors:
        if number%i == 0:
            factors = factors + [i, int(number/i)]
        i = i + 1
    factors.sort()
    return factors

        
        
start_time = time.clock()
main()
print("Time: ", time.clock() - start_time)