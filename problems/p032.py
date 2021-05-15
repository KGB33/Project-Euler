""""""


# Pandigital products
# Problem 32
"""
    We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity,

        39 × 186 = 7254

    containing multiplicand, multiplier, and product is 1 through 9 pandigital.


    Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
"""
from PrimeTools import timer
from itertools import permutations


@timer(message="By Multiplication")
def p032_by_multiplication():
    TBD = 10000
    products = []
    for a in range(1, TBD):
        for b in range(1, TBD):
            num = str(a * b) + str(a) + str(b)
            if len(num) > 9:
                break
            if (a * b) in products:
                continue
            if is_pandigital(num):
                print("{} * {} = {}".format(a, b, a * b))
                products.append(a * b)
    print("\n\nSolution: {}".format(sum(products)))


@timer(message="By Permutation")
def p032_by_permutations():
    digits = [str(x) for x in range(1, 10)]  # digits 1 - 9
    products = []
    for f in permutations(digits):
        c = int(f[5] + f[6] + f[7] + f[8])
        if c in products:
            continue
        if f[0] != "1":
            # when the first digit is not a 1 then the 1st digit can be its own number
            a = int(f[0])
            b = int(f[1] + f[2] + f[3] + f[4])
            if a * b == c:
                products.append(c)
                print(c)
                continue
        a = int(f[0] + f[1])
        b = int(f[2] + f[3] + f[4])
        if a * b == c:
            products.append(c)
            print(c)
    print("\n\nSolution: {}".format(sum(products)))


def is_pandigital(num):
    """
    :param num: String
    :return: Boolean
    """
    digits = [str(x) for x in range(1, 10)]  # digits 1 - 9
    if len(num) != 9:
        return False
    for digit in digits:
        if digit not in num:
            return False
    return True


p032_by_multiplication()
p032_by_permutations()
