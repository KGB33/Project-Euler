"""
Summation of Primes
Problem 10

The sum of the primes below `10` is `2 + 3 + 5 + 7 = 17`.

Find the sum of all the primes below two million.
"""
import time
from mttools.number_theory_tools.Primes import sieve_of_eratosthenes

SOLUTION = 142913828922


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta


def main():
    upperbound = 2000000
    return sum(sieve_of_eratosthenes(upperbound))
