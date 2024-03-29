"""
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import time
import math
from mttools.number_theory_tools.Primes import division_primality_test


SOLUTION = 5777


def main():
    soFarSoGood = True
    number = 3
    primes = [2, 3, 5, 7]
    while soFarSoGood:

        # checks number for composites
        if division_primality_test(number):
            number = number + 2

        else:
            # checks to make sure primes array has all possible primes within range
            if primes[len(primes) - 1] < number:
                primes = next_prime(primes, number)

            # takes some prime, and sees if any solution is avalable
            default = False
            for prime in primes:
                if math.sqrt((number - prime) / 2) % 1 == 0:
                    # Conjecture holds for Number
                    default = True
                    number = number + 2
                    break
            # does not hold
            soFarSoGood = default
    return number


def next_prime(primes, end_num):
    for i in range(primes[len(primes) - 1] + 1, end_num):
        if division_primality_test(i):
            primes = primes + [i]
    return primes


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
