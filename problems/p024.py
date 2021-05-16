"""
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects.

For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.

If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.


The lexicographic permutations of 0, 1 and 2 are:

        012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

---------------------------
aka, what is the 1,000,000th number that has the all the digits 0-9
"""
import time
from itertools import permutations

SOLUTION = 2783915460


def main():
    counter = 0
    for p in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if counter == 999999:  # 1,000,000th element
            return int("".join(str(digit) for digit in p))
        counter += 1


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
