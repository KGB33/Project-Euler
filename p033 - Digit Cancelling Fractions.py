"""
Digit cancelling fractions
Problem 33


The fraction 49/98 is a curious fraction,
    as an inexperienced mathematician in attempting
    to simplify it may incorrectly believe that

        49/98 = 4/8,

    which is correct, is obtained by cancelling the 9s.


We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
    less than one in value, and containing two digits in the numerator and denominator.


If the product of these four fractions is given in
    its lowest common terms, find the value of the denominator.
"""
from PrimeTools import timer
from itertools import product



@timer()
def p033():
    solutions = ()

    # Generate Numerators and Denominators
    for d_arr in product(range(1, 10), repeat=2):
        d = concatenate(d_arr)
        for n_arr in product(range(1, 10), repeat=2):
            n = concatenate(n_arr)

            # Breaks if the Frac is not less than 1
            if n/d >= 1:
                break

            # Checks to see if the numerators and denominators share digits
            for a in n_arr:
                if a in d_arr:
                    r_d = list(d_arr)
                    r_d.remove(a)
                    r_d = sum(r_d)

                    r_n = list(n_arr)
                    r_n.remove(a)
                    r_n = sum(r_n)

                    if r_n/r_d == n/d:
                        solutions += ({'n': n, 'd': d, 'r_n': r_n, 'r_d': r_d},)


    p_n = 1
    p_d = 1
    for i, sol in enumerate(solutions):
        print('Solution {}:\n\t{}/{} = {}\n\t{}/{} = {}'.format(i+1, sol['n'], sol['d'], sol['n'] / sol['d'], sol['r_n'], sol['r_d'], sol['r_n'] / sol['r_d']))
        p_n *= sol['n']
        p_d *= sol['d']

        p_n, p_d = simplify_fraction(p_n, p_d)

    print('Grand Solution: {}/{}'.format(p_n, p_d))


def simplify_fraction(numerator, denomonator):
    n_fac = prime_factors(numerator)
    d_fac = prime_factors(denomonator)

    for factor in n_fac:
        if factor in d_fac:
            if n_fac[factor] > d_fac[factor]:
                n_fac[factor] -= d_fac[factor]
                d_fac[factor] = 0
            else:
                d_fac[factor] -= n_fac[factor]
                n_fac[factor] = 0

    return build_num_from_prime_factors(n_fac), build_num_from_prime_factors(d_fac)


def concatenate(num):
    result = ''
    for digit in num:
        result += str(digit)
    return int(result)


def prime_factors(num):
    """
    Creates a dictionary of prime factors where:
        {factor: power}

    :param num: (int)
        Number to be factored

    :return: (dict)
        Dictionary of prime factors
    """
    n = 2
    dic = {}
    while n <= num:
        if num % n == 0:
            num = num / n
            if n in dic:
                dic[n] += 1
            else:
                dic.update({n: 1})
        else:
            n += 1
    return dic


def build_num_from_prime_factors(factors):
    num = 1
    for f in factors:
        num *= pow(f, factors[f])
    return num


p033()

