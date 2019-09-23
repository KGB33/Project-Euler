"""
Square prime factors
Problem 632
For an integer n, we define the square prime factors of n to be the primes whose square divides n.
For example, the square prime factors of 1500=22×3×53 are 2 and 5.

Let Ck(N) be the number of integers between 1 and N inclusive with exactly k square prime factors.
You are given some values of Ck(N) in the table below.


Find the product of all non-zero Ck(1016). Give the result reduced modulo 1000000007.
"""

from PrimeTools import timer, find_factors


def problem_632_take_num_find_factors():
    upper_bound = pow(10, 3)
    k = 1
    modulo = 1000000007
    total = 0
    product = 1
    for number in range(1, upper_bound + 1):
        if has_k_square_prime_factors(number, k):
            total += 1
            product = product * number
            product = product % modulo
    print(
        "With Upperbound: {0}"
        "\n\tThere are {1} Numbers"
        "\n\tWith exactry {2} Square Factors"
        "\n\tThe product of those numbers is: {3}".format(
            upper_bound, total, k, product
        )
    )


def has_k_square_prime_factors(number, k):
    """
    :param number: Number to Be factored
    :param k: Number Must have exactly k square prime factors
    :return: True if num has K SPF, else false
    """
    # print("\n\nHKSPF: {0}, {1}".format(number, k))
    factors = find_factors(number)
    # print("\tFactors of {0}: {1}".format(number, factors))
    num_squared_factors = 0
    for key in factors:
        if factors[key] >= 2:
            num_squared_factors += 1
    # print("\tNum SF: {0}".format(num_squared_factors))
    if num_squared_factors == k:
        # print("\tReturned: True")
        return True
    else:
        # print("\tReturned: False")
        return False


problem_632()
