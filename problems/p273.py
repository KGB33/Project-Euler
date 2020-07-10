""""""


"""
Project Euler #273
https://projecteuler.net/problem=273

    Consider equations of the form: a^2 + b^2 = N, 0 ≤ a ≤ b, a, b and N integer.

    For N=65 there are two solutions:

    a=1, b=8 and a=4, b=7.

    We call S(N) the sum of the values of a of all solutions of a^2 + b^2 = N, 0 ≤ a ≤ b, a, b and N integer.

    Thus S(65) = 1 + 4 = 5.

    Find ∑S(N), for all squarefree N only divisible by primes of the form 4k+1 with 4k+1 < 150.

definitions:
    squarefree: no repeated factors IE 8 is not squarefree (2,2,2) where as 6 is (2,3)


"""
# import itertools
import math


def main():
    n = 1
    sN = ()
    # loop that iterates through all possiblities and generates N's
    for b in range(1, int(math.sqrt(5030362804658426121702685610))):
        for a in range(0, b):
            n = pow(a, 2) + pow(b, 2)
            print(n, b, a)
            if n > 5030362804658426121702685610:
                break
            if prime_factor_4k_1(n):
                sN = sN + (a,)
    print(sN)


def prime_factor_4k_1(number):
    # all primes of the form p = 4k+1 (from OEIS: http://oeis.org/A002313)
    ftPrimes = [2, 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149]
    n = 2
    factors = (1,)
    while n <= number:
        if number % n == 0:
            factors = factors + (n,)
            number = number / n
        else:
            n = n + 1
    for number in factors:
        if number not in ftPrimes:
            return False
    return True


main()
