"""# Summation of Primes
### Problem 10

The sum of the primes below `10` is `2 + 3 + 5 + 7 = 17`.

Find the sum of all the primes below two million.

#### Solution: `142913828922`
"""

from p010 import p010

SOLUTION = 142913828922


def test_correctness():
    assert SOLUTION == p010()


from mttools.number_theory_tools.Primes import sieve_of_eratosthenes


def p010():
    upperbound = 2000000
    return sum(sieve_of_eratosthenes(upperbound))


if __name__ == "__main__":
    print(p010())
