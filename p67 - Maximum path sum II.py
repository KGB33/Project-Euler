from PrimeTools import timer
"""
Maximum path sum II
Problem 67 
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in "p67 - data.txt",
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem,
as there are 2^99 altogether! If you could check one trillion (10^12) routes
every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""


@timer()
def p18():
    print(find_max(make_array()))


def make_array():
    final = []
    with open("data/p67 - data.txt") as f:
        for line in f:
            hold_int = []
            hold_str = line.split()
            for char in hold_str:
                hold_int = hold_int + [int(char), ]
            final = final + [hold_int, ]
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


p18()