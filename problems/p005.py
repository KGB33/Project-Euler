"""# Smallest Multiple
### Problem 5

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?


#### Solution: `232792560`
"""

from p005 import p005, gcd, lcm


SOLUTION = 232792560


def test_correctness():
    assert SOLUTION == p005()


def test_lcm():
    assert 11461 == lcm(157, 73)
    assert 15 == lcm(15, 5)
    assert 15 == lcm(5, 15)
    assert 32 == lcm(32, 32)
    assert 232 == lcm(58, 8)


def test_gcd():
    assert 1 == gcd(157, 73)
    assert 5 == gcd(15, 5)
    assert 5 == gcd(5, 15)
    assert 32 == gcd(32, 32)


import time


def p005():
    numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    winner = 11
    for element in numbers:
        winner = lcm(winner, element)
    return winner


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    start_time = time.clock()
    print(p005())
    print(time.clock() - start_time)
