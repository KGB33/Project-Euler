"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two
2-digit numbers is `9009 = 91 × 99`.

Find the largest palindrome made from the product
of two 3-digit numbers.
"""
import time

SOLUTION = 906609


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta


def main():
    winner = 0
    for n in range(999, 100, -1):
        for m in range(999, 100, -1):
            number = str(n * m)
            if number == number[::-1]:
                if int(number) > winner:
                    winner = int(number)
                    break

    return winner
