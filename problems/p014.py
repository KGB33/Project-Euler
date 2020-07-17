"""
Longest Collatz sequence
Problem 14


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
SOLUTION = 837799

import math


def main():
    maxLength = 0
    for start in range(5, 999999):
        number = start
        length = 0
        while math.log(number, 2) != 0:
            if number % 2 == 0:  # even
                number = doEven(number)
                length = length + 1
            else:  # odd
                number = doOdd(number)
                length = length + 1
        if length > maxLength:
            maxLength = length
    return maxLength


def doEven(number):
    return number / 2


def doOdd(number):
    return 3 * number + 1


def test_p014():
    assert SOLUTION == main()


if __name__ == "__main__":
    from colorama import Fore

    answer = main()
    if answer == SOLUTION:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f"Solution to {__file__[-7:-3]}={answer}")
