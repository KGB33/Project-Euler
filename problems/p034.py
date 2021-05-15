""""""


"""
Digit factorials

Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from PrimeTools import timer
import math


@timer()
def p034():
    fac_sum = []
    valid_nums = []
    for num in range(144, 50000):
        """
        This upper-bound was found by increasing
        the upper-bound until the answer was accepted
        """
        if has_9s(num):
            continue
        sol = sum([math.factorial(int(x)) for x in str(num)])
        if sol == num:
            fac_sum += [sol]
            valid_nums += [num]
    print(fac_sum)
    print(sum(fac_sum))


def has_9s(num):
    num = str(num)
    if "9" in str(num):
        return True
    return False


if __name__ == "__main__":
    p034()
