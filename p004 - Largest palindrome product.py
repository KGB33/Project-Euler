# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 17:44:18 2018

@author: kelto
"""

"""
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
import time


def main():
    winner = 0
    for n in range(999, 100, -1):
        for m in range(999, 100, -1):
            number = str(n * m)
            if number == number[::-1]:
                if int(number) > winner:
                    winner = int(number)
                    break

    print("Winner Winner Chx Dinner: ", winner)


start_time = time.clock()
main()
print(time.clock() - start_time)
