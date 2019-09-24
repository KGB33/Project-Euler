from PrimeTools import sieve_of_eratosthenes


def p010():
    upperbound = 2000000
    total = 0
    sieve = sieve_of_eratosthenes(upperbound)
    for entry in sieve:
        if sieve[entry]:
            total = total + entry
    return total


if __name__ == "__main__":
    print(p010())
