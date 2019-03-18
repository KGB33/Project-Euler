"""
Multiples of 3 and 5
Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from PrimeTools import timer


@timer(unit='ns')
def find_multiples():
    grand_sum = 0
    for n in range(1000):
        if n % 3 == 0:
            grand_sum += n
        elif n % 5 == 0:
            grand_sum += n
    print(grand_sum)


find_multiples()


@timer(unit='ns')
def array_way():
    print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))

array_way()
