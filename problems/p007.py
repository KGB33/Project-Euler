"""
10001st prime
Problem 7

By listing the first six prime numbers:
`2, 3, 5, 7, 11, and 13`, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
import time
from math import log
from mttools.number_theory_tools.Primes import sieve_of_eratosthenes

SOLUTION = 104743


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta


def main():
    guess_num = 10001
    while True:
        p_guess = int(guess_num * log(guess_num, 10))
        primes = sieve_of_eratosthenes(p_guess)
        if len(primes) > 10000:
            return primes[10000]
        else:
            guess_num *= 1.5
