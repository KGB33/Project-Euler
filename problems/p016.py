"""
Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import time

SOLUTION = 1366


def main():
    n = 1000
    x = str(pow(2, n))
    total = 0
    for digit in x:
        total += int(digit)
    return total


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
