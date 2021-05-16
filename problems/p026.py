"""
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

            1/2	=   0.5
            1/3	=   0.(3)
            1/4	=   0.25
            1/5	=   0.2
            1/6	=   0.1(6)
            1/7	=   0.(142857)
            1/8	=   0.125
            1/9	=   0.(1)
            1/10=   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import math
import time

SOLUTION = 983


def main():
    maximum = 0
    for f in range(2, 1000):
        r_num = get_repeated(f)
        if r_num > maximum:
            # print('Calculating max: {}, {}'.format(maximum, r_num))
            maximum = r_num
            max_num = f
    return max_num


def get_repeated(num):
    r = []
    c_r = 0.1
    while True:
        c_r = (c_r * 10) % num
        if c_r not in r:
            r += [c_r]
        else:
            return len(r)


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
