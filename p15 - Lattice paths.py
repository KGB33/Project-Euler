# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:28:55 2018

@author: kelto
"""
"""
Lattice paths
Problem 15 
Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?
"""

"""
Note: this can be solved using Binomial Coefficients (nCk), aka n choose k. 

For the 2x2 example we have: 
     _ _ _ _  spots and R, R, D, D to choose from
     
however, once all the R's or all the D's are in place, the other must fill in
the blanks, thus we have 4C2

nCk =  ___(n!)___
       k!(n - k!)
"""

"""
Answer: 137846528820
"""
from scipy.special import comb
import time

def main():
    size = 20
    n = size * 2
    k = size
    print(comb(n, k, exact = True))
    
    

print("Running, do not shut off Computer...")
start_time = time.clock()
main()
print("Time: ", time.clock() - start_time)