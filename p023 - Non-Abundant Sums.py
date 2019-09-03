"""
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from PrimeTools import timer, perfect_factors


class p023(object):
    """
    ~ 200ms to initalize abundants and abundants_set
    ~ 450ms to run program
    ~ 650ms total
    """

    @timer(message="Init Time")
    def __init__(self):
        self.abundants = [x for x in range(1, 28123 + 1) if p023.is_abundant(x)]
        self.abundants_set = set(self.abundants)
        # print(self.abundants)

    @timer(message="Call Time")
    def __call__(self):
        print(
            "\n\nSolution: {}".format(
                sum(x for x in range(1, 28123 + 1) if not self.is_abundant_sum(x))
            )
        )

    def is_abundant_sum(self, number):
        for i in self.abundants:
            if i > number:  # Assume ordered
                return False
            if (number - i) in self.abundants_set:
                return True
        return False

    @staticmethod
    def is_abundant(number):
        if number < 12:
            return False
        else:
            return sum(perfect_factors(number)) > number


@timer(message="Total Time")
def main():
    p = p023()
    p()


main()
