"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a
clockwise direction a 5 by 5 spiral is formed as follows:

                21 22 23 24 25
                20  7  8  9 10
                19  6  1  2 11
                18  5  4  3 12
                17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the
    diagonals in a 1001 by 1001 spiral formed in the same way?
"""
from PrimeTools import timer


@timer()
def p028():
    total = 1
    lap = 1
    current_num = 1
    while True:
        # See Notes:
        for _ in range(0, 4):  # 4 times
            current_num += lap * 2
            total += current_num
        lap += 1
        if current_num >= 1001 * 1001:
            break
    print("Solution: {}".format(total))
    # print('Current Num: ', current_num) # verify it stops at the correct number


p028()

"""
Notes:

    When the spiral is uncurled it looks as shown:

            * |    *   *   *   *  |          *           *           *           *
            1    2 3 4 5 6 7 8 9    10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

    Where * indicate diagonals, and | indicate a new layer or lap around the middle

        If we start counting Laps at 0,
    then the formula for the distance between the diagonals
    is:

            Distance = 2 * lap_number

        Then, starting at 1, we add the distance, then add the new number to the total.
    repeat a total of 4 times, then add one to the lap_number

    The If statement at the end will execute for any squared odd number. This is proven below:

            Take any Odd Number

                { 2 * k + 1 },

            Square it

                { 4 * k * k + 4 * k + 1 },

            Subtract 1 for the center

                { 4 * k * k + 4 * k },

            Next:

                { (4 * k * k + 4 * k) % 4 == 0 },

            Because the square of any odd number minus 1 is dividable by 4,
                any square spiral must end on the the odd number's square,
"""
