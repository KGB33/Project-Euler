"""
Smallest Multiple
Problem 5

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?
"""
from mttools.number_theory_tools import lcm, gcd

SOLUTION = 232792560


def test_correctness():
    assert SOLUTION == p005()


def p005():
    numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    winner = 11
    for element in numbers:
        winner = lcm(winner, element)
    return winner


if __name__ == "__main__":
    from colorama import Fore

    answer = p005()
    if answer == SOLUTION:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f"Solution to {p005()=}")
