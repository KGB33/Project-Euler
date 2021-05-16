"""
Multiples of 3 and 5
Problem 1


If we list all the natural numbers below `10` that are multiples of `3` or `5`, we get `3, 5, 6, 9`.
The sum of these multiples is `23`.

Find the sum of all the multiples of `3` or `5` below `1000`.
"""
import time

SOLUTION = 233168


def test_solution():
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta


def find_multiples():
    grand_sum = 0
    for n in range(1000):
        if n % 3 == 0:
            grand_sum += n
        elif n % 5 == 0:
            grand_sum += n
    return grand_sum


def array_way():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


def main():
    return find_multiples()
    # return array_way()
