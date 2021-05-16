"""
Maximum path sum I
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers
 on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

 Triangle: p18 - data.txt

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force,
 and requires a clever method! ;o)
"""
import time

SOLUTION = 1074


def main():
    return find_max(make_array())


def make_array():
    final = []
    with open("data/p018 - data.txt") as f:
        for line in f:
            hold_int = []
            hold_str = line.split()
            for char in hold_str:
                hold_int = hold_int + [int(char)]
            final = final + [hold_int]
    return final


def is_greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def find_max(arrayIn):
    array = arrayIn
    numRows = len(array)
    for r in range(numRows - 2, -1, -1):
        for c in range(0, len(array[r])):
            array[r][c] = array[r][c] + is_greater(array[r + 1][c], array[r + 1][c + 1])
    return array[r]


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
