"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to
do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on
a century unless it is divisible by 400.

How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import calendar
import time

SOLUTION = 171


def main():
    num_sundays = 0
    for year in range(1901, 2001):  # note: range goes from start to end - 1
        for month in range(1, 13):
            c = calendar.monthcalendar(year, month)
            if c[0][6] == 1:
                num_sundays = num_sundays + 1

    return num_sundays


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
