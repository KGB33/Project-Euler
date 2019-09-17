"""
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
import time


def count_fibonacci():
    e = 1
    p = 1
    sum_even = 0
    while e < 4000001:
        e_hold = e
        e = p + e
        p = e_hold
        if e % 2 == 0:
            sum_even += e
    print(sum_even)


start_time = time.clock()
count_fibonacci()
print(time.clock() - start_time)
