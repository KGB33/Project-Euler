# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 12:53:50 2018

@author: kelto
"""

"""
Numbers of the form a2b3
Problem 634
Define F(n) to be the number of integers x≤n that can be written in the form
 x=a^2*b^3, where a and b are integers not necessarily different and both greater than 1.

For example, 32=2^2×2^3 and 72=3^2×2^3 are the only two integers less than
 100 that can be written in this form. Hence, F(100)=2.

Further you are given F(2×104)=130 and F(3×106)=2014.

Find F(9×1018).
"""

import time
import math


def main():
    n = 9 * pow(10, 18)
    fN = []
    for number in range((3 * pow(10, 6)), n):
        # case 1, a = b
        if pow(number, 0.2) % 1 == 0:
            fN = fN + [number]

        # case 2: a != b
        # step 1, assume a or b = 1
        if pow(number, 0.5) % 1 == 0 or pow(number, 1 / 3) % 1 == 0:
            continue
        # step 2, check b's for an a that is an Int
        for b in range(2, math.trunc(pow(number / 4, 1 / 3)) + 1):
            if pow(number / pow(b, 3), 0.5) % 1 == 0:
                fN = fN + [number]

    fN = list(set(fN))
    fN.sort()
    print("F(", n, ") = ", len(fN))

    print(fN)


startTime = time.clock()
main()
print("Time: ", time.clock() - startTime)


"""
Old way (not working)
def main():
    n = (3 * pow(10,6))
    a = 2
    b = 2
    product = 0
    fN = []
    while product <= n:
        product = pow(a,2) * pow(b,3)
        print(product)
        if product <= n:
            fN = fN + [product,]

        if a == b:
            a = 2
            b = b + 1
        else:
            a = a + 1

    a = 2
    b = 2
    product = 0
    while product <= n:
        product = pow(a,2) * pow(b,3)
        print(product)
        if product <= n:
            fN = fN + [product,]

        if a == b:
            a = a + 1
            b = 2
        else:
            b = b + 1


    fN = list(set(fN))
    fN.sort()
    print('F(',n,') = ', len(fN))

    print(fN)
"""
