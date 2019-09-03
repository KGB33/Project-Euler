"""
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

        n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,

        40^2 + 40 + 41 = 40(40 + 1) + 41

is divisible by 41, and certainly when n=41,

        41^2 + 41 + 41

is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered,
which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n

    e.g. |11| = 11 and |−4| = 4


Find the product of the coefficients, a and b,
    for the quadratic expression that produces the maximum number of
    primes for consecutive values of n, starting with n=0.
"""
from PrimeTools import timer, division_test


@timer(unit="s")
def p027():
    maximum = 0
    # Check all possible b's
    for b in [x for x in range(0, 1001) if division_test(x)]:

        # Check all possible a's
        for a in range(-999, 1000, 2):

            # find length of a b combo
            length = get_length(a, b)

            # Compare lengths
            if length > maximum:
                maximum = length
                max_a = a
                max_b = b

    # Print solutions
    print(
        "A: {} B: {}"
        "\n\tSolution: {}"
        "\n\tLength: {}".format(max_a, max_b, max_a * max_b, maximum)
    )


def get_length(a, b):
    n = 0
    while True:
        if division_test((n * n) + (n * a) + b):
            n += 1
        else:
            return n


p027()
