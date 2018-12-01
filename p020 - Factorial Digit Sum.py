from math import factorial
from PrimeTools import timer
"""
Factorial digit sum
Problem 20 
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


@timer()
def p20():
    n = 100
    x = str(factorial(n))
    total = 0
    for digit in x:
        total += int(digit)
    print("Sum of {} is: {}".format(n, total))


p20()