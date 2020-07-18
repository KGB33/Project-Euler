from mttools.number_theory_tools.Primes import sieve_of_eratosthenes


def p010():
    upperbound = 2000000
    return sum(sieve_of_eratosthenes(upperbound))


if __name__ == "__main__":
    print(p010())
