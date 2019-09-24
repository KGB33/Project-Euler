import time
from PrimeTools import sieve_of_eratosthenes
from math import log


def p007():
    guess_num = 10001
    while True:
        p_guess = int(guess_num * log(guess_num, 10))
        p = sieve_of_eratosthenes(p_guess)
        primes = [x for x in p if p[x]]
        if len(primes) > 10000:
            return primes[10000]
        else:
            guess_num *= 1.5


if __name__ == "__main__":
    start_time = time.perf_counter()
    print(p007())
    print(time.perf_counter() - start_time)
