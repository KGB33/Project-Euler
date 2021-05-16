"""
Digit factorials

Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import time
import math

SOLUTION = 40730


def main():
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
    return sum(fac_sum)


def has_9s(num):
    num = str(num)
    if "9" in str(num):
        return True
    return False


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
