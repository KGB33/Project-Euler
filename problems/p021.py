"""
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time

SOLUTION = 31626


def main():
    total = 0
    upper_bound = 10000
    for n in range(0, upper_bound):
        if n == sum_of_proper_divisors(n):
            # d(n) = n, do nothing
            pass
        elif n == sum_of_proper_divisors(sum_of_proper_divisors(n)):
            # d(n) = a and d(a) = n Hence a and n are amicable
            total += n
        else:
            pass
    return total


def sum_of_proper_divisors(number):
    total = 1
    for i in range(2, number):
        if number % i == 0:
            total += i
    return total


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
