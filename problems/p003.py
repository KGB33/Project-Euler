"""
Largest prime factor
Problem 3

The prime factors of `13195` are `5, 7, 13, 29`.

What is the largest
prime factor of the number `600851475143`?

"""
from mttools.number_theory_tools.Primes import prime_factors

SOLUTION = 6857


def test_correctness():
    assert p003() == SOLUTION


def p003():
    number = 600851475143
    return max(prime_factors(number).keys())


if __name__ == "__main__":
    print(f"Solution for {p003()=}")
