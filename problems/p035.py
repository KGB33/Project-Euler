"""
Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import random
import time

SOLUTION = 55


def main():
    cirPrimes = (2, 5)
    # iterate from 1 to 100 to start
    for number in range(3, 1000000, 2):
        numString = str(number)
        hasEvens = False
        beenTested = False

        # test if number has any evens in it
        for even in ["0", "2", "4", "5", "6", "8"]:
            if even in numString:
                hasEvens = True

        # tests if this number has already been tested
        if number in cirPrimes:
            beenTested = True

        # tests for cicPrimatlity
        if hasEvens == False and beenTested == False:
            isCirPrime = False
            for i in range(0, len(numString)):
                test = int(numString[i:] + numString[:i])
                isCirPrime = isPrime(test)  # can use isPrime or primeFactor
                if isCirPrime == False:
                    break

        # ADD ALL rotations to the tuple at the top
        if isCirPrime and not hasEvens:
            for i in range(0, len(numString)):
                if (int(numString[i:] + numString[:i])) not in cirPrimes:
                    cirPrimes = cirPrimes + (int(numString[i:] + numString[:i]),)
    return len(cirPrimes)


def isPrime(number):
    # Checks Carmicheal Numbers
    if number in [
        561,
        1105,
        1729,
        2465,
        2821,
        6601,
        8911,
        10585,
        15841,
        29341,
        41041,
        46657,
        52633,
        62745,
        63973,
        75361,
        101101,
        115921,
        126217,
        162401,
        172081,
        188461,
        252601,
        278545,
        294409,
        314821,
        334153,
        340561,
        399001,
        410041,
        449065,
        488881,
        512461,
    ]:
        return False
    # Fermats Little Therom
    for i in range(1, 2):
        base = random.randint(2, number - 1)
        if pow(base, number - 1) % number != 1:
            return False

    return True  # probably


def prime_factor(number):
    n = 2
    factors = (1,)
    while n <= number:
        if number % n == 0:
            factors = factors + (n,)
            number = number / n
        else:
            n = n + 1
    if len(factors) == 2:
        return True
    else:
        return False


def test_solution() -> (bool, int):
    start_time = time.time()
    pass_ = main() == SOLUTION
    time_delta = time.time() - start_time
    return pass_, time_delta
