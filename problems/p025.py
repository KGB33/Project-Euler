"""
1000-digit Fibonacci number
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time

SOLUTION = 4782


def main():
    index = 2
    fn_1 = 1
    fn = 1
    while len(str(fn)) != 1000:
        hold = fn
        fn = next_fib(fn, fn_1)
        fn_1 = hold
        index += 1
    return index


def next_fib(fn_1, fn_2):
    return fn_1 + fn_2


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
