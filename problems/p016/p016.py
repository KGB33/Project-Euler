from PrimeTools import timer

"""
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""


@timer()
def p16():
    n = 1000
    x = str(pow(2, n))
    total = 0
    for digit in x:
        total += int(digit)
    print("Sum of {} is: {}".format(n, total))


p16()
