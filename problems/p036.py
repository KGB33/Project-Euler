"""
Double-base palindromes
    Problem 36


The decimal number,

    585_10 = 1001001001_2

is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import time

SOLUTION = 872187


def main():
    total = 0
    for i in range(0, 1_000_000):
        base_10 = str(i)
        base_10_reverse = get_reversed_string(base_10)
        if base_10 == base_10_reverse:
            base_2 = str(bin(i))[2:]
            if base_2 == base_2[::-1]:
                total += i
    return total


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
