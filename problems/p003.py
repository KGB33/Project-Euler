"""
Largest prime factor
Problem 3

The prime factors of `13195` are `5, 7, 13, 29`.

What is the largest
prime factor of the number `600851475143`?

"""
import time
from mttools.number_theory_tools.Primes import prime_factors

SOLUTION = 6857


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta


def main():
    number = 600851475143
    return max(prime_factors(number).keys())
