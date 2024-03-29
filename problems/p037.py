"""
Truncatable primes
Problem 37


The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


Limits:
    Cannot Have Even Digits
    Must Start and End with a Prime Digit (Cannot end with a 2)
"""
from mttools.number_theory_tools.Primes import (
    division_primality_test,
    sieve_of_eratosthenes,
)
import time

SOLUTION = 748317


def main():
    solutions = []
    p = 7
    primes = [str(x) for x in range(2, 10) if division_primality_test(x)]
    while len(solutions) < 11:
        p += 2
        if str(p)[0] in primes and str(p)[-1] in primes:
            if is_left_truncatable(str(p)):
                if is_right_truncatable(str(p)):
                    solutions += [p]
                    print(p)

    return sum(solutions)


def is_right_truncatable(num):
    for i, digit in enumerate(num):
        if division_primality_test(int(num[: i + 1])):
            continue
        else:
            return False
    return True


def is_left_truncatable(num):
    for i, digit in enumerate(num):
        if division_primality_test(int(num[i:])):
            continue
        else:
            return False
    return True


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
