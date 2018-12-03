from PrimeTools import timer
"""
Large sum
Problem 13 
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
 --->>> p13 - data <<<---
"""


@timer()
def p13():
    total = 0
    with open('data/p013 - data.txt') as f:
        for line in f:
            total += int(line[:11])
    print("Total: ", str(total)[:10])


p13()
