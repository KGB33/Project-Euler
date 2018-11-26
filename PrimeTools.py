# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:24:23 2018

@author: kelton
"""
import random
from time import perf_counter_ns
import functools


def little_fermat(number, trials):
    """
    Uses Femats little thearom to test for primeality
    @param number: int that is being checked
    @param trials: int that determans the number of bases used,
     the higher the number the more accurate (must be 2 or greater)
    """
    # Checks Carmicheal Numbers up to ~ 500,000
    if number in [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461]:
        return False
    # Fermats Little Therom
    for i in range(1,trials):
        base = random.randint(2, number - 1)
        if pow(base, number - 1) % number != 1:
            return False

    return True # probably


def division_test(number):
    """
    Uses division to test for primeality
    @param number: int that is being checked
    """
    for divisor in range(2, int(number/2) + 1):
        if number%divisor == 0:
            return False
    return True


def sieve_of_eratosthenes(upperbound):
    """
    Sieve of Eratosthenes
    Creates, then returns, a dictionary: { X : Boolean} where X range from
    2 to upperbound, and boolean is True if X is prime
    @param upperbound - upper limit for the sieve
    """
    sieve = {x : True for x in range(2, upperbound)}
    for i in range(2, int(pow(upperbound, .5) + 1)):
        if sieve[i]:  # value is boolean
            j = pow(i, 2)
        while j < upperbound:
            sieve[j] = False
            j = j + i
    return sieve


def find_factors(number):
    """
    Creates a dic of prime factors, where the key is the prime,
    and the entry is the power they key is raised to
    @param number - number to be factored
    """
    n = 2
    dic = {}
    while n <= number:
        if number % n == 0:
            number = number/n
            if n in dic:
                dic[n] += 1
            else:
                dic.update({n: 1})
        else:
            n += 1
    return dic


def largest_prime_less_than(number):
    if number <= 2:
        print("No Primes Less than 2")
        return None
    for i in range((number - 1), 0, -1):
        if division_test(i):
            return i


class timer(object):

    # TODO: add optional param for number of trials, then average
    def __init__(self, unit='ms'):
        """
        Decorator that times the functions
        :param unit: Unit that the time is displayed in, default is ms
        prints time elapsed
        """
        self.unit = unit

    def __call__(self, f):
        """
        :param f: The function to be timed
        """
        def wrapper_timer(*args, **kwargs):
            # times and runs the function
            before = perf_counter_ns()
            rv = f(*args, **kwargs)
            after = perf_counter_ns()
            # Calculates total time and converts to chosen units
            if self.unit == 'ns':
                con = pow(10, 0)
            elif self.unit == 'us':
                con = pow(10, 3)
            elif self.unit == 'ms':
                con = pow(10, 6)
            elif self.unit == 's':
                con = pow(10, 9)
            elif self.unit == 'min':
                con = 6 * pow(10, 10)
            else:
                print("\n\nBad unit given to @timer, Valid units are:"
                      "\n\tns, us, ms, s, min"
                      "\n\tUsing default ms")
                con = pow(10, 6)
                self.unit = 'ms'
            time = '{:.3f}'.format((after - before) / con)
            # prints output
            print("\n\nTime Elapsed: {0}{1}".format(time, self.unit))
            return rv
        return wrapper_timer

